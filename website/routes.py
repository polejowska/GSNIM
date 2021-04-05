from flask import render_template, redirect, url_for, flash, request
from website import app, db
from website.forms import EntranceForm, Form
from website.models import Respondent, Question, Option, Answer
import os

TEMPLATE_DIR = os.path.abspath('../templates')
STATIC_DIR = os.path.abspath('../static')

# FETCH ALL QUESTIONS AND OPTIONS FROM DATABASE
questions_objects_list = Question.query.all()
options_objects_list = Option.query.all()


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    entrance_form = EntranceForm()
    if entrance_form.validate_on_submit():
        respondent = Respondent(age=entrance_form.age.data, gender=entrance_form.gender.data, med_education=entrance_form.med_education.data)
        db.session.add(respondent)
        db.session.commit()
        if respondent.gender == 2:
            flash('Wprowadzone dane zostały zatwierdzone. Zapraszamy Pana do udzielania odpowiedzi.', 'success')
        elif respondent.gender == 1:
            flash('Wprowadzone dane zostały zatwierdzone. Zapraszamy Panią do udzielania odpowiedzi.', 'success')
        return redirect(url_for('question', id=1, respondent_id=respondent.id))
    flash('W celu przystąpienia do ankiety należy wprowadzić dane zgodne z rzeczywistością. ') 
    return render_template("index.html", entrance_form=entrance_form)


@app.route("/question/<int:respondent_id>/<int:id>/", methods=['GET', 'POST'])
def question(id, respondent_id):
    form = Form()

    options_1_question = []

    # READ ALL OPTIONS FROM DATABASE MATCHING QUESTION ID
    for option in options_objects_list:
        if option.question_id == id:
            options_1_question.append(option)

    # UPDATE OPTIONS (RADIOBUTTONS)
    form.question_options.choices = [(option.number, option.option_text) for option in options_1_question]
    form.question_options.coerce = int

    if form.validate_on_submit(): 
        # WHEN SUBMITTED -> SAVE TO DATABASE, GO TO THE NEXT QUESTION
        answer =  Answer(respondent_id=respondent_id, question_id=id, option_number=form.question_options.data)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('question', id=id+1, respondent_id=respondent_id))
    # IF THE LAST QUESTION -> END
    if id-1 >= len(questions_objects_list):
        return redirect(url_for('end', respondent_id=respondent_id))
    return render_template('form.html', form=form, question=questions_objects_list[id-1].text)


@app.route("/end/<int:respondent_id>", methods=['GET', 'POST'])
def end(respondent_id):
    respondents = Respondent.query.all()
    women_count = 0
    men_count = 0

    for respondent in respondents:
        if respondent.gender == 1:
            women_count = women_count + 1
        if respondent.gender == 2:
            men_count = men_count + 1
    sumup_respondent_answers = Answer.query.filter_by(respondent_id=respondent_id)
    respondents = Respondent.query.order_by(Respondent.id)
    answers = Answer.query.order_by(Answer.respondent_id)
    return render_template('end.html', answers=sumup_respondent_answers,
                            women_count=women_count, men_count=men_count, number=len(list(respondents)))

