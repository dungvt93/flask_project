from model.db_helper.db_type import DBType
from abc import *


class BaseModel:
    @abstractmethod
    def __init__(self, conn, db_type):
        self.db_type = db_type
        self.conn = conn

    def query(self, query_string, param_list):
        result = None
        if self.db_type == DBType.MYSQL:
            try:
                cursor = self.conn.cursor()
                cursor.execute(query_string, param_list)
                result = cursor.fechall()
            except Exception as e:
                self.conn.rollback()
                raise e

        return result

    @abstractmethod
    def create_instance(self, data):
        pass
