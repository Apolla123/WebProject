# испортируем библиотеки
import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash
from .db_session import SqlAlchemyBase
from flask_login import UserMixin


# класс user
class User(SqlAlchemyBase, UserMixin):
    # название
    __tablename__ = 'users'

    # пишем параметры
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer)
    login = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    # функция поставить пароль
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # функция проверить пароль
    def check_password(self, password):
        return check_password_hash(self.password, password)
