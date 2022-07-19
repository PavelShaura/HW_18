from flask_restx import Resource, Namespace


from application.container import genres_service
from application.services.schemas.genre import GenreSchema

genres_ns = Namespace('genres')
genre_schema = GenreSchema()


@genres_ns.route('/<int:uid>')
class GenreView(Resource):

    def get(self, uid):
        return genres_service.get_one(uid)


@genres_ns.route('/')
class GenresView(Resource):

    def get(self):
        return genres_service.get_all()

