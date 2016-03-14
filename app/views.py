from flask import render_template, flash, redirect
from app import app
from app.models import User
from .forms import LoginForm
from app import db



@app.route('/')
@app.route('/index')
def index():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('index.html',
                           title='Sign In',
                           form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data,last_name=form.last_name.data,email=form.email.data
        db.sessoin.add(user)
        db.session.commit()
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)
