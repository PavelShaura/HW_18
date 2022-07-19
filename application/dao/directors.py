from application.dao.models.models import Director
from lib.dao import BaseDAO


class DirectorsDAO(BaseDAO):
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, uid: int):
        return self.session.query(Director).filter(Director.id == uid).first()

