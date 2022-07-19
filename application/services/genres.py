from lib.service import BaseService


class GenresService(BaseService):
    def get_all(self):
        return self.schema.dump(self.dao.get_all(), many=True)

    def get_one(self, uid: int):
        return self.schema.dump(self.dao.get_one(uid))