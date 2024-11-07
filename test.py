import json
from os import getenv
# from app.handler import profile
# from app.database import UserVar
# from base import code
# from app.database_phys import DBStudents
# from app.config import AWSConfig

# from boto_orm.db_manager import DynamodbManage
# from boto_orm.models.db_model import DBModel, KeySchema

# from app.data_model import DBModel
from app.database import db_termex, db_phys
from app.config import configure
from boto_orm.models.db_model import KeySchema, PARAMS_REVERSE
from boto_orm.db_manager import DynamodbManage
from app.rate_maker import handler, get_rate
from boto_orm.s3_manager import S3Manager

# s3 = S3Manager(bucket_name='termex-bot', config=configure.s3_config, session_aws=configure.session)
response = get_rate('НТТС', 'termex-bot')
# response = s3.upload_file(file_path='static/ranger.json', name_file='range.json')
# message = handler(bucket_name='phys-bot', db=db_phys)
# print(message)

# data = DB(table_name='User_Var', config=configure.phys_db, session_aws=configure.session)
# key_schema = KeySchema(HASH='user_id')
# print(db_phys.get_user(708978847))
# print(db_phys.all_user())

# print(data.get_item(key_schema(980314213)))
# db = {'profile': {'S': 'Преподаватель'}, 'user_id': {'N': '980314213'}, 'bonus': {'M': {'kinematic': {'M': {'f2': {'N':'0'}, 'f1': {'N':'0'}, 'f3': {'N':'0'}}}, 'static': {'N': '0'}, 'dynamic': {'N': '0'}}}, 'tasks': {'M': {'L11': {'S': '7'}, 'L12': {'S': '7'}, 'L15': {'S': '7'}, 'L16': {'S': '7'}, 'L17': {'S': '7'}, 'L10': {'S': '7'}, 'L13': {'S': '7'}, 'L14': {'S': '7'}, 'S0': {'N': '0'}}}, 'fine': {'N': '0'}, 'group': {'S': '1-1'}, 'name': {'S': 'Солдатов Юрий Игоревич'}, 'prize': {'N': '0'}}




# class Table(DBModel):
#     name: str
#     user_id: int
#     create: float

# key_schema = KeySchema(HASH='name', RANGE='user_id')

# # response = DynamodbManage(resource_name='Table_unit', config=config_db).create_table(key_scheme, attribute=Table, provisioned_throughput=prov)
# data = Table(name='Yur', user_id=238, create=19.97)
# db = DynamodbManage(table_name='Table_test')

# response = db.get_item(key_schema('Yur', 238))
print(response)


def json_data(data):
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)