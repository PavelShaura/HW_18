from typing import Any, Dict

from marshmallow import ValidationError

from application.dao.models.models import Movie
from lib.dao import BaseDAO


class MoviesDAO(BaseDAO):

    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, uid: int):
        return self.session.query(Movie).filter(Movie.id == uid).first()

    def post(self, data: Dict[str, Any]):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def patch(self, uid, data: Dict[str, Any]):
        result = self.session.query(Movie).filter(Movie.id == uid).update(data)

        if result != 1:
            self.session.rollback()
            raise ValidationError(f'Movie with id {uid} not found')

        self.session.commit()

    def delete(self, uid: int):
        deleted_rows = self.session.query(Movie).filter(Movie.id == uid).delete()

        if deleted_rows != 1:
            return None, 400

        self.session.commit()
        return None, 200

    def get_by_director_id(self, director_id: int):
        return self.session.query(Movie).filter(Movie.director_id == director_id)

    def get_by_genre_id(self, genre_id: int):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id)

    def get_by_year(self, year: int):
        return self.session.query(Movie).filter(Movie.year == year)