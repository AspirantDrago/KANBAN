import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy_serializer import SerializerMixin

from .db import db


class SupplyCard(db.Model, SerializerMixin):
    __tablename__ = 'supply_card'

    _db = db

    _id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    product_id = sa.Column(sa.Integer, sa.ForeignKey('product._id'), nullable=False)
    container_id = sa.Column(sa.Integer, sa.ForeignKey('container.id'), nullable=False)
    count = sa.Column(sa.Integer, nullable=False, default=0)
    warehouse_to_id = sa.Column(sa.Integer, sa.ForeignKey('warehouse.id'), nullable=False)

    warehouse_to = orm.relationship('Warehouse', backref=orm.backref('supply_cards'))
    product = orm.relationship('Product', backref=orm.backref('supply_cards'))
    container = orm.relationship('Container', backref=orm.backref('supply_card'), uselist=False, cascade='all, delete-orphan', single_parent=True)

    @property
    def code(self) -> str:
        return str(self._id).zfill(6)

    def __str__(self) -> str:
        return self.code

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id={self.id}, product_id={self.product_id}, container_id={self.container_id}, warehouse_to_id={self.warehouse_to_id}, count={self.count})'
