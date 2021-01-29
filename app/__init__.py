import os

from flask import Flask
from .routes import auth, views
from .shared import db, hasher

#
def create_app():
  app = Flask(__name__, instance_relative_config=True)

  app.config.from_pyfile('config.py', silent=True)

  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  with app.app_context():
    db.init_db_controller(app)
    hasher.init_hash_controller(app)

  app.register_blueprint(auth.auth_bp)
  app.register_blueprint(views.views_bp)


  return app
