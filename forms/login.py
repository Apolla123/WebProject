# испортируем библиотеки
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField, StringField
from wtforms.validators import DataRequired


# форма для логина
class LoginForm(FlaskForm):
    # параметры
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])

    # переменная "запомнить меня"
    remember_me = BooleanField('Запомнить меня')

    # кнопка
    submit = SubmitField('Войти')
