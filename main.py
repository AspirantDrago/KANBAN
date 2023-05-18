from flask import Flask
from flask_alembic import Alembic
from flask_babelex import Babel
from flask_restful import Api
from waitress import serve
import logging

from admin.main_admin import setup_admin
from config import *
from models.container import Container
from models.db import open_db, db

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
db = open_db(app)
api = Api(app)
babel = Babel(app, default_locale='ru')
alembic = Alembic()
alembic.init_app(app)


@babel.localeselector
def get_locale():
    '''
    Функция для определения языка
    :return: Язык интерфейса пользователя
    '''
    return 'ru'


if __name__ == '__main__':
    logging.info('Подключение к базе данных прошло успешно')
    with app.app_context():
        try:
            alembic.stamp('heads')
            alembic.revision('heads')
            alembic.upgrade()
        except Exception as e:
            logging.error(f'Ошибка миграции базы данных: {e}')
    admin = setup_admin(app, db)
    if DEBUG:
        app.run(port=PORT, host=HOST, debug=DEBUG)
    else:
        serve(app, host=HOST, port=PORT)
