import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy import ColumnElement, type_coerce
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin

from .db import db
from .db_tools import DefaultComparator


class SupplyCard(db.Model, SerializerMixin):
    __tablename__ = 'supply_card'

    _db = db

    _id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    product_id = sa.Column(sa.Integer, sa.ForeignKey('product._id'), nullable=False)
    container_id = sa.Column(sa.Integer, sa.ForeignKey('container.id'), nullable=False)
    count = sa.Column(sa.Integer, nullable=False, default=0)
    warehouse_to_id = sa.Column(sa.Integer, sa.ForeignKey('warehouse.id'), nullable=False)
    created_datetime = sa.Column(sa.DateTime, nullable=True, default=datetime.datetime.now, server_default=sa.func.now())
    completed_datetime = sa.Column(sa.DateTime, nullable=True, server_default=None)

    warehouse_to = orm.relationship('Warehouse', backref=orm.backref('supply_cards'))
    product = orm.relationship('Product', backref=orm.backref('supply_cards'))
    container = orm.relationship('Container', backref=orm.backref('supply_card'), uselist=False, cascade='all, delete-orphan', single_parent=True)

    @hybrid_property
    def code(self) -> str:
        return str(self._id).zfill(6)

    @hybrid_property
    def url(self) -> str:
        return '/' + self.code

    @hybrid_property
    def completed(self) -> bool:
        return self.completed_datetime is not None

    @completed.inplace.expression
    @classmethod
    def _completed_expression(cls) -> ColumnElement[bool]:
        return type_coerce(cls.completed_datetime, sa.Boolean)

    @completed.inplace.setter
    def _completed_setter(self, value: bool) -> None:
        if self.completed == value:
            return
        if value:
            self.completed_datetime = datetime.datetime.now()
        else:
            self.completed_datetime = None

    def __str__(self) -> str:
        return self.code

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id={self.id}, product_id={self.product_id}, container_id={self.container_id}, warehouse_to_id={self.warehouse_to_id}, count={self.count})'
