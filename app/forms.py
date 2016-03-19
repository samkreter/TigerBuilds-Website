from flask.ext.wtf import Form
from wtforms import BooleanField, TextField, PasswordField, validators
from wtforms.validators import DataRequired
from flask_wtf.file import FileField

class LoginForm(Form):
    first_name = TextField('first_name', validators=[DataRequired()])
    last_name = TextField('first_name', validators=[DataRequired()])
    email = TextField('Email Address', [validators.required(),validators.Length(min=6, max=35)])
    resume = FileField()
    remember_me = BooleanField('remember_me', default=False)