import os

DATABASE_NAME = os.environ.get('DATABASE_NAME', 'mobula')
DATABASE_HOST = os.environ.get('DATABASE_HOST', 'locahost')
DATABASE_USER = os.environ.get('DATABASE_USER', 'mobula-user')
DATABASE_PASS = os.environ.get('DATABASE_PASS', 'mobula-user-pw')

DATABASE_URI = 'mysql+pymysql://' + DATABASE_USER + ':' + DATABASE_PASS + '@' + DATABASE_HOST + '/' + DATABASE_NAME

DALAI_HOST = os.environ.get('DALAI_HOST', 'localhost')
DALAI_PORT = os.environ.get('DALAI_PORT', '3000')
DALAI_MODEL = os.environ.get('DALAI_MODEL', 'alpaca.7B')

DALAI_URI = 'http://' + DALAI_HOST + ':' + DALAI_PORT