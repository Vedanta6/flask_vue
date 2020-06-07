import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET>_KEY') or "my_secret_key"
    # MONGO_URI = "mongodb://0.0.0.0:27017/shoppingList"
    MONGODB_DB = 'shoppingList'
    MONGODB_HOST = '0.0.0.0'
    MONGODB_PORT = 27017
    ENV = 'development'
    SERVER_NAME = '0.0.0.0:5000'
    DEBUG = True
