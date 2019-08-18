from flask import Blueprint
from flask_restplus import Resource, Api

user_blueprint =Blueprint('users',__name__)

api = Api(user_blueprint)

class UserReaource(Resource):
  def get(self):
    return{
      'Ping': 'pong',
      'ding': 'dong'
    }

api.add_resource(UserReaource, '/users/ping')