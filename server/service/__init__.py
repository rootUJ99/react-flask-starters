import os
from flask import Flask
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
# instantiate the db
db = SQLAlchemy()  


def create_app():
# flask app config
  app = Flask(__name__)

  # setting up config
  app_settings = os.getenv('APP_SETTINGS') 
  app.config.from_object(app_settings)

  # set up extensions
  db.init_app(app)

  # import blueprint
  from .api.users import user_blueprint
  # register blueprint
  app.register_blueprint(user_blueprint)

  @app.shell_context_processor
  def ctx():
    return {'app': app, db:'db'}
  
  return app