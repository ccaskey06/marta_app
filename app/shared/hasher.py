from flask import g
from app.controllers.HashController import HashController

#
def init_hash_controller(app):
  app.teardown_appcontext(clear_hash_controller)
  get_hash_controller()

#
def get_hash_controller():
  if 'hasher' not in g:
    g.hasher = HashController()

  return g.hasher

#
def clear_hash_controller(e=None):
  g.pop('hasher', None)
