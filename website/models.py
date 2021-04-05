from website import db
#from datetime import datetime


class Respondent(db.Model):
    #__tablename__ = 'respondents'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    age = db.Column(
        db.Integer,
        nullable=False
    )
    gender = db.Column(
        db.Integer,
        nullable=False  # ?
    )
    med_education = db.Column(
        db.Boolean,
        nullable=False
    )

    #answers = db.relationship('Answer', backref='respondent', lazy=True)

    def __repr__(self):
        return f"Respondent('{self.id}', '{self.age}', '{self.gender}')"


class Question(db.Model):
    #__tablename__ = 'questions'
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    text = db.Column(
        db.String(255),
        nullable=False
    )
    options = db.relationship('Option' , backref='question_assigned')

    def __repr__(self):
        return f"Question('{self.id}', '{self.text}')"


class Option(db.Model):
    #__tablename__ = 'options'
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    question_id = db.Column(
        db.Integer,
        db.ForeignKey('question.id'),
        unique=False
    )
    number = db.Column(
        db.Integer
    )
    option_text = db.Column(
        db.Text,
        nullable=False
    )

    def __repr__(self):
        return f"Option('{self.question_id}', '{self.number}', '{self.option_text}')"


class Answer(db.Model):
    #__tablename__ = 'answers'
    respondent_id = db.Column(
        db.Integer,
        db.ForeignKey('respondent.id'),
        primary_key=True,
        nullable=True
    )
    question_id = db.Column(
        db.Integer,
        db.ForeignKey('question.id'),
        primary_key=True
    )
    option_number = db.Column(
        db.Integer,
        db.ForeignKey('option.number'),
        primary_key=True
    )

    def __repr__(self):
        return f"Answer('{self.respondent_id}', '{self.question_id}', '{self.option_number}')"


