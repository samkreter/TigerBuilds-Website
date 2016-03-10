from flask.ext.wtf import Form
from wtforms import BooleanField, TextField, PasswordField, validators
from wtforms.validators import DataRequired

class LoginForm(Form):
    first_name = TextField('first_name', validators=[DataRequired()])
    last_name = TextField('first_name', validators=[DataRequired()])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    remember_me = BooleanField('remember_me', default=False)