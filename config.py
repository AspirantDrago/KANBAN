import pathlib

HOST = '127.0.0.1'                  # Адрес хоста
PORT = 8080
DEBUG = True

DB_NAME = str(pathlib.Path().resolve().parent) + '/api/data/db.sqlite'
SECRET_KEY = 'secret_key'
