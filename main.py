from flask import Flask, render_template, redirect
from flask_babelex import Babel
from flask_restful import Api
from waitress import serve
import logging

from admin.main_admin import setup_admin
from config import *
from models.db import open_db, create_session
from models.card import SupplyCard

has_alembic = False
try:
    from flask_alembic import Alembic
    has_alembic = True
except ImportError:
    pass

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
db = open_db(app)
api = Api(app)
babel = Babel(app, default_locale='ru')
if has_alembic:
    alembic = Alembic()
    alembic.init_app(app)


@babel.localeselector
def get_locale():
    '''
    Функция для определения языка
    :return: Язык интерфейса пользователя
    '''
    return 'ru'


@app.route('/<int:card_id>')
def card(card_id: int):
    '''
    Функция для отображения карточки товара
    :param card_id: ID карточки товара
    :return: HTML страница с карточкой товара
    '''
    session = create_session()
    card = session.get(SupplyCard, card_id)
    url_card = f'/supplycard/details/?id={card._id}'
    url_provider = f'/provider/details/?id={card.product.provider_id}'
    url_container = f'/container/details/?id={card.container_id}'
    url_warehouse = f'/warehouse/details/?id={card.warehouse_to_id}'
    url_product = f'/product/details/?id={card.product_id}'
    if not card:
        return 'Карточка товара не найдена', 404
    return render_template(
        'card.html',
        card=card,
        fullhost=HOST_FULL_URL,
        url_card=url_card,
        url_provider=url_provider,
        url_container=url_container,
        url_warehouse=url_warehouse,
        url_product=url_product
    )


@app.route('/')
def main_page():
    return redirect('/supplycard')


if __name__ == '__main__':
    logging.info('Подключение к базе данных прошло успешно')
    if has_alembic:
        with app.app_context():
            try:
                operations = alembic.compare_metadata()
                if operations:
                    alembic.stamp('heads')
                    alembic.revision('heads')
                    alembic.upgrade()
                    logging.info('Миграция базы данных прошла успешно')
            except Exception as e:
                logging.error(f'Ошибка миграции базы данных: {e}')
    admin = setup_admin(app, db)
    if DEBUG:
        app.run(port=PORT, host=HOST, debug=DEBUG)
    else:
        serve(app, host=HOST, port=PORT)
