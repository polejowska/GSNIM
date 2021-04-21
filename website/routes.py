from flask import render_template, redirect, url_for, flash, request
from website import app, db
from website.forms import EntranceForm, Form
from website.models import Respondent, Question, Option, Answer, Experience, Fears, Knowledge, Expectations
import os

TEMPLATE_DIR = os.path.abspath('../templates')
STATIC_DIR = os.path.abspath('../static')

# FETCH ALL QUESTIONS AND OPTIONS FROM DATABASE
questions_objects_list = Question.query.all()
options_objects_list = Option.query.all()

submit_flag = False

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    entrance_form = EntranceForm()

    if entrance_form.validate_on_submit() and not submit_flag:         
        respondent = Respondent(age=entrance_form.age.data, gender=entrance_form.gender.data, 
                                med_education=entrance_form.med_education.data,
                                place=entrance_form.place.data
                                )
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
    age_list = []

    women_count = 0
    men_count = 0

    age_min = 0
    age_max = 0
    age_total = 0

    for respondent in respondents:
        age_list.append(respondent.age)
        age_total += respondent.age
        if respondent.gender == 1:
            women_count = women_count + 1
        if respondent.gender == 2:
            men_count = men_count + 1

    age_average = age_total/len(respondents)
    age_min = min(age_list)
    age_max = max(age_list)

    for id in range(1, 21):
        if id == 1: 
            db.session.add(
                Experience(respondent_id=respondent_id,
                 udzial_zaawansowane_badanie=(
                     Option.query.filter_by(
                         question_id=id, 
                         number=(
                             Answer.query.filter_by(
                                 respondent_id=respondent_id, question_id=id).first()).option_number).first()).option_text,
                 stosowanie_urzadzen = (
                     Option.query.filter_by(
                         question_id=id+1, number=(
                             Answer.query.filter_by(
                                 respondent_id=respondent_id, question_id=id+1).first()).option_number).first()).option_text,
                 vr = (Option.query.filter_by(
                     question_id=id+2, number=(
                         Answer.query.filter_by(
                             respondent_id=respondent_id, question_id=id+2).first()).option_number).first()).option_text
                 )
            )
            db.session.commit()
            
        if id == 4:
            db.session.add(
                 Fears(respondent_id=respondent_id,
                 wspomaganie_innowacji = (Option.query.filter_by(question_id=id, number=(Answer.query.filter_by(respondent_id=respondent_id, question_id=id).first()).option_number).first()).option_text,
                 ai_zastapienie_lekarzy = (Option.query.filter_by(question_id=id+1, number=(Answer.query.filter_by(respondent_id=respondent_id, question_id=id+1).first()).option_number).first()).option_text,
                 operacja_robot_chirurg = (Option.query.filter_by(question_id=id+2, number=(Answer.query.filter_by(respondent_id=respondent_id, question_id=id+2).first()).option_number).first()).option_text
                 )
            )
            db.session.commit()
        if id == 7:
            db.session.add(
                 Knowledge(respondent_id=respondent_id,
                 predyspozycje_genetyczne = (Option.query.filter_by(question_id=id, number=(Answer.query.filter_by(respondent_id=respondent_id, question_id=id).first()).option_number).first()).option_text,
                 swiadomosc_korzysci_ai = (Option.query.filter_by(question_id=id+1, number=(Answer.query.filter_by(respondent_id=respondent_id, question_id=id+1).first()).option_number).first()).option_text,
                 liczba_daVinci = (Option.query.filter_by(question_id=id+2, number=(Answer.query.filter_by(respondent_id=respondent_id, question_id=id+2).first()).option_number).first()).option_text,
                 przewidywanie_stan_zdrowia = (Option.query.filter_by(question_id=id+3, number=(Answer.query.filter_by(respondent_id=respondent_id, question_id=id+3).first()).option_number).first()).option_text,
                 telemedycyna = (Option.query.filter_by(question_id=id+4, number=(Answer.query.filter_by(respondent_id=respondent_id, question_id=id+4).first()).option_number).first()).option_text
                 )
            )
            db.session.commit()
        if id == 12:
            db.session.add(
                 Expectations(respondent_id=respondent_id,
                 wieksza_zaplata_zabieg = (Option.query.filter_by(question_id=id, number=(Answer.query.filter_by(respondent_id=respondent_id, question_id=id).first()).option_number).first()).option_text,
                 leczenie_leki_genetyczne = (Option.query.filter_by(question_id=id+1, number=(Answer.query.filter_by(respondent_id=respondent_id, question_id=id+1).first()).option_number).first()).option_text,
                 ingerencja_geny = (Option.query.filter_by(question_id=id+2, number=(Answer.query.filter_by(respondent_id=respondent_id, question_id=id+2).first()).option_number).first()).option_text,
                 dane_czujniki_spersonalizowanie = (Option.query.filter_by(question_id=id+3, number=(Answer.query.filter_by(respondent_id=respondent_id, question_id=id+3).first()).option_number).first()).option_text,
                 opiekun_robot_czlowiek = (Option.query.filter_by(question_id=id+4, number=(Answer.query.filter_by(respondent_id=respondent_id, question_id=id+4).first()).option_number).first()).option_text,
                 koszulka_smart = (Option.query.filter_by(question_id=id+5, number=(Answer.query.filter_by(respondent_id=respondent_id, question_id=id+5).first()).option_number).first()).option_text,
                 tatuaz_smart = (Option.query.filter_by(question_id=id+6, number=(Answer.query.filter_by(respondent_id=respondent_id, question_id=id+6).first()).option_number).first()).option_text,
                 chip = (Option.query.filter_by(question_id=id+7, number=(Answer.query.filter_by(respondent_id=respondent_id, question_id=id+7).first()).option_number).first()).option_text
                 )
            )
            db.session.commit()

    db.session.commit()

    return render_template('end.html',
                            women_count=women_count, 
                            men_count=men_count, 
                            number=len(list(respondents)),
                            age_average=round(age_average),
                            age_max=age_max,
                            age_min=age_min
                            )


@app.route("/results", methods=['GET', 'POST'])
def results():
    return render_template('results.html')