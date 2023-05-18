import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy_utils import PhoneNumberType

from .db import db


class Provider(db.Model, SerializerMixin):
    __tablename__ = 'provider'

    _db = db

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String, nullable=False, unique=True, index=True)
    description = sa.Column(sa.Text, nullable=True, index=True)
    address = sa.Column(sa.String, nullable=True, index=True)
    phone = sa.Column(PhoneNumberType(country_code='RU'), nullable=True)
    email = sa.Column(sa.String, nullable=True)
    site = sa.Column(sa.String, nullable=True)

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id={self.id}, title={self.title}, description={self.description}, address={self.address}, phone={self.phone}, email={self.email})'
