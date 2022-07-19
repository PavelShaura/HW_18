from application.dao.models.models import Genre
from lib.dao import BaseDAO


class GenresDAO(BaseDAO):
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_one(self, uid: int):
        return self.session.query(Genre).filter(Genre.id == uid).first()

