import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy_serializer import SerializerMixin

from .db import db


class Container(db.Model, SerializerMixin):
    __tablename__ = 'container'

    _db = db

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    code = sa.Column(sa.String, nullable=False, unique=True, index=True)
    title = sa.Column(sa.String, nullable=True, index=True)

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id={self.id}, code={self.code}, title={self.title})'
