from flask import render_template, redirect, url_for, flash
from app import app
from forms import LoginForm


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for {form.username.data}')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)
