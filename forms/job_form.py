# испортируем библиотеки
from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, StringField
from wtforms.validators import DataRequired


# форма для работы
class JobsForm(FlaskForm):
    # параметры
    team_leader = StringField("Имя", validators=[DataRequired()])
    job = StringField('Работа', validators=[DataRequired()])

    # доп параметры
    work_size = IntegerField("Время работы (часы в день)")
    collaborators = StringField("Сайт/Место работы")

    # кнопка
    submit = SubmitField("Отправить")
