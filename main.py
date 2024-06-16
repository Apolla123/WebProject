# испортируем библиотеки
from flask import Flask, redirect, render_template, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from data import db_session

from data.jobs import Jobs
from data.users import User

# формы
from forms.login import LoginForm
from forms.job_form import JobsForm
from forms.register import RegisterForm

from get.get_weather import get_weather
from get.get_city import get_city, make_city
from get.get_random_number import get_number


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


# добавить работу
@app.route('/addjob', methods=['GET', 'POST'])
def add_job():
    try:
        form = JobsForm()

        if form.validate_on_submit():
            db_sess = db_session.create_session()

            job = Jobs(
                team_leader=form.team_leader.data,
                job=form.job.data,
                work_size=form.work_size.data,
                collaborators=form.collaborators.data,
            )

            db_sess.add(job)
            db_sess.commit()
            return redirect('/')

        return render_template('add_job.html',
                               title='Добавить работу',
                               form=form)

    except Exception as err:
        return render_template('error.html',
                               err=err,
                               message='Совет: приверьте, правильно ли вы заполнили все поля')


# начало
@app.route('/')
def start():
    db_sess = db_session.create_session()

    if current_user.is_authenticated:
        job = db_sess.query(Jobs)
        return render_template('index.html',
                               jobs=job,
                               img1=f'sky{get_number(1, 5)}.jpg',
                               img2=f'sky{get_number(6, 10)}.jpg')

    return render_template('money.html', )


# получаем температуру
@app.route('/temperature', methods=['GET', 'POST'])
def temperature():

    if request.method == 'GET':
        return render_template('get_temperature.html')

    elif request.method == 'POST':
        try:
            city = request.form['city']
            feel_like = request.form.get('accept')
            temp = get_weather(make_city(city))
            return render_template('temperature.html',
                                   city=get_city(city),
                                   feel_like=feel_like,
                                   temperature=temp[0],
                                   temperature_feel_like=temp[1])

        except Exception as err:
            return render_template('error.html',
                                   err=err,
                                   message='Подсказка: '
                                           'проверьте, правильно ли написан город/страна, обязательно на русском',
                                   img=f'sad_smile{get_number(1, 5)}.jpg')


# выйти
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


# успешное отправление формы
@app.route('/success')
def success():
    return render_template('success.html',
                           img=f'smile{get_number(1, 5)}.jpg')


# вход
@app.route('/login', methods=['GET', 'POST'])
def login():
    try:

        form = LoginForm()

        if form.validate_on_submit():
            db_sess = db_session.create_session()
            jobs = db_sess.query(User).filter(User.login == form.login.data).first()

            if jobs and jobs.check_password(form.password.data):
                login_user(jobs, remember=form.remember_me.data)
                return redirect("/")

            return render_template('login.html',
                                   message="Неправильный логин или пароль",
                                   form=form)

        return render_template('login.html',
                               title='Авторизация',
                               form=form)

    except Exception as err:
        return render_template('error.html',
                               err=err,
                               message='Совет: приверьте, правильно ли вы заполнили все поля',
                               img=f'sad_smile{get_number(1, 5)}.jpg')


# регистрация
@app.route('/register', methods=['GET', 'POST'])
def reqister():
    try:

        form = RegisterForm()

        if form.validate_on_submit():
            db_sess = db_session.create_session()

            if form.password.data != form.repeat_password.data:
                return render_template('register.html',
                                       title='Регистрация',
                                       form=form,
                                       message="Пароли не совпадают")

            if db_sess.query(User).filter(User.login == form.login.data).first():
                return render_template('register.html',
                                       title='Регистрация',
                                       form=form,
                                       message="Такой пользователь уже есть")

            user = User(
                login=form.login.data,
                surname=form.surname.data,
                name=form.name.data,
                age=form.age.data
            )

            user.set_password(form.password.data)
            db_sess.add(user)
            db_sess.commit()

            return redirect('/success')

        return render_template('register.html',
                               title='Регистрация',
                               form=form)

    except Exception as err:
        return render_template('error.html',
                               err=err,
                               message='Совет: приверьте, правильно ли вы заполнили все поля',
                               img=f'sad_smile{get_number(1, 5)}.jpg')


# функция запуска программы
def main():
    db_session.global_init("db/project.db")
    app.run(port=8080, host='127.0.0.1', debug=True)


# запуск программы
if __name__ == '__main__':
    main()
