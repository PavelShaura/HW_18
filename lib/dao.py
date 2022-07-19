from typing import Dict, Any


class BaseDAO:

    def get_all(self):
        raise NotImplementedError

    def get_one(self, uid: int):
        raise NotImplementedError

    def post(self, data: Dict[str, Any]):
        raise NotImplementedError

    def patch(self, uid: int, data: Dict[str, Any]):
        raise NotImplementedError

    def delete(self, uid: int):
        raise NotImplementedError


