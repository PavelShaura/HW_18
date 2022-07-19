from flask import request
from flask_restx import Resource, Namespace
from marshmallow import ValidationError

from application.services.schemas.movie import MovieSchema
from application.container import movies_service

movies_ns = Namespace('movies')
movie_schema = MovieSchema()


@movies_ns.route('/<int:uid>')
class MovieView(Resource):

    def get(self, uid):
        return movies_service.get_one(uid)

    def put(self, uid):
        try:
            return movies_service.patch(uid, request.json), 204
        except ValidationError as e:
            return {'errors': e.normalized_messages()}, 400

    def delete(self, uid):
        return movies_service.delete(uid), 204


@movies_ns.route('/')
class MoviesView(Resource):

    def get(self):
        args = request.args

        if 'director_id' in args:
            return movies_service.get_by_director_id(args['director_id']), 200

        if 'genre_id' in args:
            return movies_service.get_by_genre_id(args['genre_id']), 200

        if 'year' in args:
            return movies_service.get_by_year(args['year']), 200

        return movies_service.get_all()

    def post(self):
        return movies_service.post(request.json)