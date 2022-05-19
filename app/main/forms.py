from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField,SelectField,BooleanField
from wtforms.validators import InputRequired,Email,EqualTo
from wtforms import ValidationError
from ..models import User

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[InputRequired()],render_kw={"placeholder":"Comment"})
    submit = SubmitField('Comment')


class BookingForm(FlaskForm):
    fullname = StringField('Fullname',validators=[InputRequired()],render_kw={"placeholder":"Fullname"})
    email=StringField('Email',validators=[InputRequired()],render_kw={"placeholder":"email"})
    phone=StringField('Phone',validators=[InputRequired()],render_kw={"placeholder":"Phone"})
    submit = SubmitField('Book')
