import logging
from boto_orm.db_manager import DynamodbManage
from boto_orm.models.db_model import KeySchema

from app.config import configure

logger = logging.getLogger(__name__)


class DBManage:
    def __init__(self, db: DynamodbManage):
        self.db = db
        self.key_schema = KeySchema(HASH='user_id')

    def get_user(self, user_id: int) -> dict:
        return self.db.get_item(self.key_schema(user_id))['Item']

    def all_user(self):
        return self.db.scan(need_args=['name', 'profile', 'tasks', 'fine', 'prize', 'bonus'])['Items']



db_phys = DBManage(db = DynamodbManage(table_name='User_Var',
                                       config=configure.phys_db,
                                       session_aws=configure.session))
db_termex = DBManage(db = DynamodbManage(table_name='User_Var',
                                       config=configure.termex_db,
                                       session_aws=configure.session))