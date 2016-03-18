from flask import render_template, flash, redirect,request
from app import app
from app.models import User
from .forms import LoginForm
from app import db
import os
from werkzeug import secure_filename



@app.route('/')
@app.route('/index',methods=['GET', 'POST'])
def index():
    form = LoginForm()
    error = None
    return render_template('index.html',
                           title='Index',
                           form=form,
                           error=error)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    error = None
    success = None
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data,last_name=form.last_name.data,email=form.email.data)
        filePath = os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(form.email.data + ".pdf"))
        file = request.files['resume']
        if file and allowed_file(form.resume.data):
            f.save(filePath)
            db.session.add(user)
            db.session.commit()
            success = "Application Complete, Thank You"
            return render_template('index.html',
                           title='Index',
                           form=form,
                           error=error,
                           success=success)
        error = "Resume must be a pdf"
    else:
        error = "Failed to Validate. Check your information"
    return render_template('index.html',
                           title='Index',
                           form=form,
                           error=error)
