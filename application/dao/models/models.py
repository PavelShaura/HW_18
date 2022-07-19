from sqlalchemy.orm import relationship

from application.dao.models.base import BaseModel
from application.database import db


class Director(BaseModel):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Genre(BaseModel):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Movie(BaseModel):
    __tablename__ = 'movie'

    title = db.Column(db.String(255))
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)

    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))

    director = relationship('Director')
    genre = relationship('Genre')
