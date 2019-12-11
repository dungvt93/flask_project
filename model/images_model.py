from model.base_model import *
from model.db_helper.db_type import *
from model.db_helper.mysql_connection import *
from model.entity.images import *


class ImagesModel(BaseModel):
    def create_instance(self, data):
        return Images(data['id'], data['path'], data['category_id'], data['is_public'])

    def __init__(self, connect, db_type=DBType.MYSQL):
        BaseModel.__init__(self, connect, db_type)

    def get_by_id(self, id):
        query = "SELECT * FROM images WHERE id = %s"
        data = self.query(query, (id,))
        return self.create_instance(data)

    def insert_by_entity(self, images_entity):
        query = "INSERT INTO images (path, category_id, is_public) VALUE(%s, %s ,%s)"
        data = self.insert(query,(images_entity.path, images_entity.category_id, images_entity.is_public))
        return data
