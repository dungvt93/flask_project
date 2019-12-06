import mysql.connector
from db_helper import config


class MySQLConnection:
    def __init__(self, ):
        self.database_info = config.database_info

    def __enter__(self):
        self.connect = None
        self.connect = mysql.connector.connect(
            db=self.database_info["database"],
            host=self.database_info["host"],
            user=self.database_info["user"],
            passwd=self.database_info["password"],
            charset="utf8")
        self.connect.autocommit(False)
        return self.connect

    def __exit__(self, exc_type, exc_val, exc_tb):
        # pass
        self.connect.commit()
        self.connect.close()
