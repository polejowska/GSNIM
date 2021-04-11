from website import db


class Respondent(db.Model):
    __tablename__ = 'respondent'
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
        nullable=False 
    )
    med_education = db.Column(
        db.Boolean,
        nullable=False
    )
    place = db.Column(
        db.Integer,
        nullable=False
    )

    def __repr__(self):
        return f"Respondent('{self.id}', '{self.age}', '{self.gender}')"


class Question(db.Model):
    __tablename__ = 'question'
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
    __tablename__ = 'option'
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
    __tablename__ = 'answer'
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


class Experience(db.Model):
    __tablename__ = 'experience'
    __table_args__ = {'extend_existing': True}
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    respondent_id = db.Column(
        db.Integer
    )
    udzial_zaawansowane_badanie = db.Column(
        db.Text,
        nullable=True
    )
    stosowanie_urzadzen = db.Column(
        db.Text,
        nullable=True
    )
    vr = db.Column(
        db.Text
    )
    

class Fears(db.Model):
    __tablename__ = 'fears'
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    respondent_id = db.Column(
        db.Integer
    )
    wspomaganie_innowacji = db.Column(
        db.Text,
        nullable=True
    )
    ai_zastapienie_lekarzy = db.Column(
        db.Text,
        nullable=True
    )
    operacja_robot_chirurg = db.Column(
        db.Text,
        nullable=True
    )

class Knowledge(db.Model):
    __tablename__ = 'knowledge'
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    respondent_id = db.Column(
        db.Integer
    )
    predyspozycje_genetyczne = db.Column(
        db.Text,
        nullable=True
    )
    swiadomosc_korzysci_ai = db.Column(
        db.Text,
        nullable=True
    )
    liczba_daVinci = db.Column(
        db.Text,
        nullable=True
    )
    przewidywanie_stan_zdrowia = db.Column(
        db.Text,
        nullable=True
    )
    telemedycyna = db.Column(
        db.Text,
        nullable=True
    )