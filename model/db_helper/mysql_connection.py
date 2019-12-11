from model.db_helper import config
import mysql.connector as connector


class MySQLConnection:
    def __init__(self, ):
        self.database_info = config.database_info

    def __enter__(self):
        self.conn = None
        self.conn = connector.connect(
            db=self.database_info["database"],
            host=self.database_info["host"],
            user=self.database_info["user"],
            passwd=self.database_info["password"],
            charset="utf8")
        print(self.conn)
        #self.conn.autocommit(False)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        # pass
        self.conn.commit()
        self.conn.close()
