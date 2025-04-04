from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired


class RegisterForm_dep(FlaskForm):
    title = StringField('Department Title', validators=[DataRequired()])
    chief = StringField("Chief's name", validators=[DataRequired()])
    members = StringField('Members', validators=[DataRequired()])
    email = EmailField('Login/email', validators=[DataRequired()])
    submit = SubmitField('Submit')
