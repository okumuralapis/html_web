import sqlalchemy
from sqlalchemy import orm, Integer
from sqlalchemy.ext.mutable import MutableList


from .db_session import SqlAlchemyBase


class Department(SqlAlchemyBase):
    __tablename__ = 'department'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chief = sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.ForeignKey('users.id'))
    members = sqlalchemy.Column(MutableList.as_mutable(sqlalchemy.ARRAY(Integer)))
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    user = orm.relationship('User')
