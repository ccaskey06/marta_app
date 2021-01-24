# from flask import Flask
# app = Flask(__name__)
# app.secret_key = 'coreyiscute'
# from app import views

import os

from flask import Flask

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

  # register templates / blueprints here ...
  #
  #

  return app
