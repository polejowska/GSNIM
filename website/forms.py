from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, SubmitField
from wtforms.validators import NumberRange, DataRequired
from website import db
from website.models import Respondent, Question, Option, Answer


class EntranceForm(FlaskForm):
    age = IntegerField('Wiek', validators=[NumberRange(min=10, max=110), DataRequired()])
    gender = RadioField('Płeć', choices=[(1, 'Kobieta'), (2, 'Mężczyzna')], validators=[DataRequired()], coerce=int)
    med_education = RadioField('Wykształcenie medyczne', choices=[(False, 'Nie'), (True, 'Tak')], validators=[DataRequired()], coerce=bool)
    submit = SubmitField('Rozpocznij ankietę!')


class Form(FlaskForm):
    question_options = RadioField('Odpowiedź', choices=[], validators=[DataRequired()], coerce=int)
    submit = SubmitField('Następne pytanie')