import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_secret_key')

    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'flaskuser')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'password123')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'flask_auth')