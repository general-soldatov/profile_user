import json
from os import getenv
from app.handler import profile
from app.database import UserVar
from base import code
from dataclasses import dataclass, is_dataclass
from app.database_phys import DBStudents
from app.db_students import DynamodbManage, KeySchema, ProvisionedThroughput, AWSManage
from app.config import AWSConfig

@dataclass
class Table:
    name: str
    user_id: int
    create: float


config_db = AWSConfig(service_name='dynamodb', endpoint_url=getenv('TEST_END'))
key_scheme = KeySchema(HASH='name', RANGE='user_id')
prov = ProvisionedThroughput(ReadCapacityUnits=1, WriteCapacityUnits=1)

# response = DynamodbManage(resource_name='Table_test', config=config_db).create_table(key_scheme, attribute=Table, provisioned_throughput=prov)
data = Table(name='Yur', user_id=236, create=19.57)
response = DynamodbManage(resource_name='Table_test', config=config_db).scan() #put_item_table(data)

print(response['Items'])


# print(UserVar().get_user(980314213))
# var = '1814265390'

# for i in code:
#     UserVar().put_item(user_id=int(i['user_id']), name=i['name'], profile=i['profile'], group=i['group'], var=i['var']['var_all'], var_d1=i['var']['var_d1'])

# print(UserVar().all_users())

# print(response)
