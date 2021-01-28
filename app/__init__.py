import os

from flask import Flask
from .routes import auth
from .shared import hasher

#
def create_app():
  app = Flask(__name__, instance_relative_config=True)

  # load the instance config, if it exists
  app.config.from_pyfile('config.py', silent=True)

  # ensure the instance folder exists
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  with app.app_context():
    hasher.init_hash_controller(app)

  # register templates / blueprints here ...
  app.register_blueprint(auth.auth_bp)

  #

  return app
