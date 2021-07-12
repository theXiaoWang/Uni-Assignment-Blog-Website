from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
    validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email',
    validators=[DataRequired(), Email()])

    password = PasswordField('Password',
    validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password',
    validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username exists.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email exists.')


class LoginForm(FlaskForm):
    email = StringField('Email',
    validators=[DataRequired(), Email()])

    password = PasswordField('Password',
    validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

# code to enable update info for user
# refered from CoreyMSchafer Python/Flask_Blog/07-User-Account-Profile-Pic/flaskblog/forms.py /
# accessed 16-02-2021
# https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Flask_Blog/07-User-Account-Profile-Pic/flaskblog/forms.py
class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
    validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email',
    validators=[DataRequired(), Email()])

    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')
# end of referenced code.
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username exists.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email exists.') 


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Post comment')


class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])

# code to reset password through email links
# refered from CoreyMSchafer Python/Flask_Blog/10-Password-Reset-Email/flaskblog/forms.py /
# accessed 17-02-2021
# https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Flask_Blog/10-Password-Reset-Email/flaskblog/forms.py
class RequestResetForm(FlaskForm):
    email = StringField('Email',
    validators=[DataRequired(), Email()])
    submit = SubmitField('Continue')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('No account links to this email. Please register first.')
# end of referenced code.

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password',
    validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password',
    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')