import boto3
import logging
from abc import ABC, abstractmethod
import botocore

import boto3.session
import botocore.client
import botocore.session
from botocore.session import Session
from app.config import AWSSession, AWSConfig, db_config
from typing import Union, Dict, Optional, List, Any
from dataclasses import dataclass, is_dataclass

from pydantic import BaseModel
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

PARAMS = {
            int: 'N',
            float: 'N',
            str: 'S',
            bool: 'BOOL',
            None: 'NULL',
            list: 'L',
            tuple: 'L',
            dict: 'M'
        }

@dataclass
class ProvisionedThroughput:
    ReadCapacityUnits: int
    WriteCapacityUnits: int

@dataclass
class KeySchema:
    HASH: str
    RANGE: Optional[str] = None

    def __call__(self, HASH_VALUE, RANGE_VALUE = None):
        data = {self.HASH: HASH_VALUE}
        if RANGE_VALUE:
            data[self.RANGE] = RANGE_VALUE
        return data


class AWSClient:
    """Родительский класс для инициализации клиента для управления AWS-service. Оптимизирован для работы в YandexCloud.
        :param resource_name: str - название таблицы или бакета
        :param config: Union[AWSConfig, dict] - конфигурация ресурсного клиента: service_name: Any['dynamodb', 's3'], endpoint_url: str
        :param session_aws: Union[AWSSession, dict] - конфигурация сессии boto3: region_name: str, aws_access_key_id: str, aws_secret_access_key
    """
    def __init__(self, resource_name: str, config: Union[AWSConfig, dict] = db_config, session_aws: Union[AWSSession, dict] = AWSSession()):
        config = self._check_type_models(config, AWSConfig)
        session_aws = self._check_type_models(session_aws, AWSSession)
        _aws: Session = botocore.session.get_session()
        _aws.set_credentials(**session_aws)
        self.resource_name = resource_name
        self.client = _aws.create_client(**config)

    @staticmethod
    def _check_type_models(arg: Union[dict, BaseModel], dataclass_name: type = None):
        if dataclass_name and isinstance(arg, dataclass_name):
            return arg.__dict__
        if isinstance(arg, BaseModel):
            return arg.model_dump()
        if isinstance(arg, dict):
            return arg


class DynamodbManage(AWSClient):
    """Дочерний класс управления таблицами DynamoDB в облачных сервисах YandexCloud.
    """
    @staticmethod
    def _table_params(resource_name: str, key_schema: Dict[str, str], attribute: Dict[str, str],
                      provisioned_throughput: Optional[Dict[str, str]] = None):
        table_creation_params = {
            'TableName': resource_name,
            'KeySchema': [
                {
                    'AttributeName': value,
                    'KeyType': key
                }
                for key, value in key_schema.items() if value
            ],
            'AttributeDefinitions': [
                {
                    'AttributeName': key,
                    'AttributeType': value
                }
                for key, value in attribute.items()
            ]
        }
        if provisioned_throughput:
            table_creation_params["ProvisionedThroughput"] = provisioned_throughput

        return table_creation_params


    @staticmethod
    def _check_arg_models(arg: Union[BaseModel, Dict[str, dict]]):
        condition = lambda x: type(x) not in [str, int, float]
        if isinstance(arg, BaseModel):
            return {key: {PARAMS[arg.__annotations__[key]]: value
                          if condition(value) else str(value)}
                for key, value in arg.model_dump().items()}
        elif isinstance(arg, dict):
            return {key: {PARAMS[type(value)]: value
                          if condition(value) else str(value)}
                for key, value in arg.items()}
        else:
            assert TypeError('Uncorrect type param "arg"')


    @staticmethod
    def _check_param_models(attribute: Union[Dict[str, str], BaseModel], key_schema: Union[Dict[str, str], KeySchema]):
        if isinstance(key_schema, KeySchema):
            key_schema = {key: value for key, value in key_schema.__dict__.items() if value}
        if isinstance(attribute, BaseModel):
            attribute = {key: PARAMS[value] for key, value in
                            attribute.__annotations__.items() if key in key_schema.values()}
        return key_schema, attribute

    @staticmethod
    def _error_handler(response: dict):
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return response
        else:
            assert ConnectionError(response['ResponseMetadata'])

    def create_table(self, key_schema: Union[Dict[str, str], KeySchema],
                      attribute: Union[Dict[str, str], BaseModel],
                      provisioned_throughput: Union[Dict[str, str], ProvisionedThroughput, None] = None):
        """Метод создания таблицы.
            :type key_schema: Union[Dict[str, str], KeySchema]
            :param key_schema: Рекомендуется использование dataclass для установки ключей партицирования
                                'HASH' и сортировки 'RANGE'
            :type attribute: Union[Dict[str, str], BaseModel]
            :param attribute: Рекомендуется использование модели Pydantic с аргументами arg: type = 'value'
            :type provisioned_throughput: Union[Dict[str, str], ProvisionedThroughput, None] = None)
            :param provisioned_throughput: Предусмотренные параметры пропускной способности для глобального
                                        вторичного индекса, состоящие из единиц пропускной способности чтения и записи.
        """
        key_schema, attribute = self._check_param_models(attribute, key_schema)
        if provisioned_throughput:
            provisioned_throughput = self._check_type_models(provisioned_throughput, ProvisionedThroughput)
        table_creation_params = self._table_params(self.resource_name, key_schema, attribute, provisioned_throughput)
        response = self.client.create_table(**table_creation_params)
        return self._error_handler(response)


    def put_item(self, data: type):
        """Метод добавления данных в таблицу. Автоматически определяет тип и значение переменных
            из экземпляра dataclass
            :type data: dataclass
            :param data: принимает в качестве аргумента экземпляр dataclass
        """
        data = self._check_arg_models(data)
        response = self.client.put_item(TableName=self.resource_name, Item=data)
        return self._error_handler(response)

    def get_item(self, keys: KeySchema, need_args: Optional[List[str]] = None):
        """Метод запроса значения из таблицы по значению ключа / ключей.
            :type need_args: Optional[List[str]] = None
            :param need_args: список требуемых параметров для вызова
            :type keys: Dict[str, str | int ] или экземпляр датакласса KeySchema keys(HASH_VALUE, RANGE_VALUE)
            :param keys: ключи доступа в формате {'key': 'value'}
        """
        data = {
            'TableName': self.resource_name,
            'Key': self._check_arg_models(keys)
        }
        if need_args:
            data['ProjectionExpression'] = ', '.join(need_args)
        return self.client.get_item(**data)

    def delete_item(self, keys: KeySchema):
        """Метод удаления значения из таблицы по значению ключа / ключей.
            :type keys: Dict[str, str | int ] или экземпляр датакласса KeySchema keys(HASH_VALUE, RANGE_VALUE)
            :param keys: {'key': 'value'}
        """
        keys = self._check_arg_models(keys)
        return self.client.delete_item(TableName=self.resource_name, Key=keys)

    def scan(self, need_args: Optional[List[str]] = None, filters: Union[type, Dict[str, Any]] = None, **kwargs):
        data = {
            'TableName': self.resource_name
        }
        if need_args:
            data['ProjectionExpression'] = ', '.join(need_args)
        if filters:
            data['FilterExpression']='',
            data['ExpressionAttributeValues'] = ''
        if kwargs:
            data.update(kwargs)
        return self.client.scan(**data)

    def query(self, keys: KeySchema):
        keys = self._check_arg_models(keys)
        ### error Key Schema
        return self.client.query(TableName=self.resource_name, KeyConditions=keys)

    def delete_table(self):
        """Метод удаления таблицы из базы данных. Название таблицы берётся из resource_name экземпляра класса
        """
        return self.client.delete_table(TableName=self.resource_name)