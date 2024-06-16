# испортируем библиотеки
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


# класс jobs
class Jobs(SqlAlchemyBase):
    # название
    __tablename__ = 'jobs'

    # пишем параметры
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("users.id"))
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    user = orm.relationship('User')