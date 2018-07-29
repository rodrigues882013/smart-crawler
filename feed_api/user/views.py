from flask import request, jsonify, Blueprint
from feed_api.auth.service import requires_auth
from flask_restful import Resource, Api
from .service import UserService as service

user_bp = Blueprint('user_bp', __name__)
api = Api(user_bp)


class User(Resource):

    @requires_auth
    def get(self, id):
        return jsonify(service.find_one(id))

    @requires_auth
    def put(self, id):
        return jsonify(service.update(request, id)), 200


api.add_resource(User, '/users/<int:id>')
