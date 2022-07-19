from typing import Dict, Any

from marshmallow import Schema

from lib.dao import BaseDAO


class BaseService:

    def __init__(self, dao: BaseDAO, schema: Schema):
        self.dao = dao
        self.schema = schema

    def get_all(self):
        return self.schema.dump(self.dao.get_all(), many=True)

    def get_one(self, uid: int):
        return self.schema.dump(self.dao.get_one(uid))

    def post(self, data: Dict[str, Any]):
        self.dao.post(data=self.schema.load(data))

    def patch(self, uid: int, data: Dict[str, Any]):
        self.dao.patch(uid, self.schema.load(data))

    def delete(self, uid: int):
        return self.schema.dump(self.dao.delete(uid))