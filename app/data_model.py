from pydantic import BaseModel
from datetime import datetime
from typing import Any

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

class DBModel(BaseModel):
    def dump_dynamodb(self):
        return {key:
                {self._params_convert(self.__annotations__[key]): value}
                for key, value in self.model_dump().items()}

    @staticmethod
    def _params_convert(arg: type):
        if arg not in PARAMS or arg in [str, int, float]:
            return PARAMS[str]
        return PARAMS[arg]