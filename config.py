import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    POSTGRES_DB = {
        'host': os.environ.get('DB_HOST'),
        'user': os.environ.get('DB_USER'),
        'database': os.environ.get('DB_NAME'),
        'password': os.environ.get('DB_PASSWORD'),
        }
    SQL_DIR = os.path.join(basedir, 'sql')
