import uuid
import hashlib

from werkzeug.security import generate_password_hash, check_password_hash

class HashController(object):

  #
  def generate_hash(self, str_to_be_hashed):
    salt = str(uuid.uuid4().hex)[0:23]

    return hashlib.sha256(salt.encode() + str_to_be_hashed.encode()).hexdigest()[0:24] + ':' + salt
  
  #
  def check_hash(self, hash_str, input_str):
    hashed_val, salt = hash_str.split(':')

    return hashed_val == hashlib.sha256(salt.encode() + input_str.encode()).hexdigest()[0:24]
