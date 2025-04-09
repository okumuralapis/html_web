from tkinter.ttk import Separator

import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Department(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'department'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String,
                              sqlalchemy.ForeignKey('users.id'),
                              nullable=True)
    chief = sqlalchemy.Column(sqlalchemy.Integer)
    members = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    user = orm.relationship('User')
