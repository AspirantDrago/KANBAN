import logging
from typing import Optional

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DB_NAME


def open_db(app: Flask) -> SQLAlchemy:
    global db
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}?check_same_thread=False'
    logging.info(f'Подключение к базе данных {DB_NAME}')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import __all_models

    db.init_app(app)
    with app.app_context():
        db.create_all()
    return db


def db_factory():
    global db
    if db:
        return
    db = SQLAlchemy()


db: Optional[SQLAlchemy] = None
db_factory()
