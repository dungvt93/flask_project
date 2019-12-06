from base_model import *
from db_helper.db_type import *
from db_helper.mysql_connection import *
from entity.images import *


class ImagesModel(BaseModel):
    def create_instance(self, data):
        return Images(data['id'], data['path'], data['category_id'], data['is_public'])

    def __init__(self, connect, db_type=DBType.MYSQL):
        BaseModel.__init__(self, connect, db_type)

    def get_by_id(self, id):
        data = self.query(query_string="select * from images where id = {}".format(id))
        return self.create_instance(data)


with MySQLConnection() as provider:
    imagesModel = ImagesModel(provider)
    imagesModel.get_by_id(1)
