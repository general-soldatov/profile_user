import boto3
import logging
from abc import ABC, abstractmethod

import boto3.session
from app.config import AWSSession, AWSConfig, db_config
from typing import Union, Dict, Optional
from dataclasses import dataclass, is_dataclass

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

class AWSManage:
    """Родительский класс для инициализации клиента для управления AWS-service.
            resource_name: str - название таблицы или бакета
            config: Union[AWSConfig, dict] - конфигурация ресурсного клиента: service_name: Any['dynamodb', 's3'], endpoint_url: str
            session_aws: Union[AWSSession, dict] - конфигурация сессии boto3: region_name: str, aws_access_key_id: str, aws_secret_access_key
    """
    def __init__(self, resource_name: str, config: Union[AWSConfig, dict] = db_config, session_aws: Union[AWSSession, dict] = AWSSession()):
        if isinstance(config, AWSConfig):
            config = config.__dict__
        if isinstance(session_aws, AWSSession):
            session_aws = session_aws.__dict__
        self.aws = boto3.session.Session(**session_aws)
        self.resource_name = resource_name
        self.client = self.aws.client(**config)
        self.resource = self.aws.resource(**config)


class DynamodbManage(ABC, AWSManage):
    def _table_params(self,
                      key_schema: Dict[str, str], attribute: Dict[str, str],
                      provisioned_throughput: Optional[Dict[str, str]] = None):
        table_creation_params = {
            'TableName': self.resource_name,
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
    def check_type_dataclass(arg: Union[dict, type], dataclass_name: type = None):
        if is_dataclass(arg) or isinstance(arg, dataclass_name):
            return arg.__dict__
        if isinstance(arg, dict):
            return arg

    @staticmethod
    def check_arg_dataclass(arg: Union[type, Dict[str, dict]]):
        condition = lambda x: type(x) not in [str, int, float]
        if is_dataclass(arg):
            return {key: {PARAMS[arg.__annotations__[key]]: value
                          if condition(value) else str(value)}
                for key, value in arg.__dict__.items()}
        return arg


    @staticmethod
    def check_param_dataclass(attribute: Union[Dict[str, str], type], key_schema: Union[Dict[str, str], KeySchema]):
        if isinstance(key_schema, KeySchema):
            key_schema = {key: value for key, value in key_schema.__dict__.items() if value}
        if isinstance(attribute, type):
            attribute = {key: PARAMS[value] for key, value in
                            attribute.__annotations__.items() if key in key_schema.values()}
        return key_schema, attribute

    @staticmethod
    def error_handler(response: dict):
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return response
        else:
            assert ConnectionError(response['ResponseMetadata'])

    def create_table(self, key_schema: Union[Dict[str, str], KeySchema],
                      attribute: Union[Dict[str, str], type],
                      provisioned_throughput: Union[Dict[str, str], ProvisionedThroughput, None] = None):
        key_schema, attribute = self.check_param_dataclass(attribute, key_schema)
        if provisioned_throughput:
            provisioned_throughput = self.check_type_dataclass(provisioned_throughput, ProvisionedThroughput)
        table_creation_params = self._table_params(key_schema, attribute, provisioned_throughput)
        response = self.client.create_table(**table_creation_params)
        return self.error_handler(response)


    def put_item_table(self, data: type):
        data = self.check_arg_dataclass(data)
        response = self.client.put_item(TableName=self.resource_name, Item=data)
        return self.error_handler(response)

    def scan(self):
        return self.client.scan(TableName=self.resource_name)