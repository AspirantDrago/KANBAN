from __future__ import annotations

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy_serializer import SerializerMixin

from .db import db


class Product(db.Model, SerializerMixin):
    __tablename__ = 'product'

    _db = db

    _id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    product_code = sa.Column(sa.Integer, index=True, nullable=False, unique=True)
    title = sa.Column(sa.String, nullable=False, index=True)
    description = sa.Column(sa.Text, nullable=True, index=True)
    provider_id = sa.Column(sa.Integer, sa.ForeignKey('provider.id'), nullable=False)

    provider = orm.relationship('Provider', backref=orm.backref('products'))

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id={self.id}, title={self.title}, description={self.description}, provider_id={self.provider_id})'
