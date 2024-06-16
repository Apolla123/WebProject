# испортируем библиотеки
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired


# форма для регистрации
class RegisterForm(FlaskForm):
    # параметры
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    repeat_password = PasswordField('Повтор пароль', validators=[DataRequired()])

    # доп параметры
    surname = StringField('Фамилия')
    name = StringField('Имя')
    age = IntegerField('Возраст')

    # кнопка
    submit = SubmitField('Войти')
