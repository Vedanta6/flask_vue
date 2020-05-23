import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET>_KEY') or "my_secret_key"
