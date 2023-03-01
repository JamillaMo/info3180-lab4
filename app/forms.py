from flask_wtf import FlaskForm, FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    image = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'You can only upload an image!')
    ])