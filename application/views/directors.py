from flask_restx import Resource, Namespace

from application.services.schemas.director import DirectorSchema
from application.container import directors_service

directors_ns = Namespace('directors')
director_schema = DirectorSchema()


@directors_ns.route('/<int:uid>')
class DirectorView(Resource):

    def get(self, uid):
        return directors_service.get_one(uid)


@directors_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        return directors_service.get_all()

