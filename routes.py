from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from app import app, login
from forms import LoginForm
from models import User


@login.user_loader
def load_user(id):
    return User.query.get(id)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/secret')
@login_required
def secret():
    return render_template('secret.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # если юзер вошел, не пускаем его на страницу логина
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data.lower()).first()
        if user is None or not user.check_password_hash(form.password.data):
            flash('Invalid username or password.')
            return redirect(url_for('login'))

        login_user(user, remember=form.rememberMe.data)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))