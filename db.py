from website import db
from website.models import Respondent, Question, Option, Answer


questions_options = [
    ['Czy Pan(i) obawia się, że sztuczna inteligencja zastąpi lekarzy?', ['Tak', 'Nie', 'Mam neutralne odczucia']],
    ['Czy byłby/byłaby Pana(i) gotowa w przypadku wymaganego leczenia na podjęcie leczenia lekami, które zostały wytworzone według Pana(i) kodu genetycznego?', ['Tak', 'Nie', 'Trudno powiedzieć']],
    ['Czy byłaby Pan(i) w stanie zapłacić więcej na badanie wykorzystujące nowsze technologie?', ['Tak', 'Nie', 'Trudno powiedzieć']],
    ['W razie wymaganego zabiegu chirurgicznego byłby(/byłaby Pan(i) w stanie być operowanym przez:', ['Tylko przez robota medycznego (w przypadku 100% pewności jego prawidłowego działania)', 'Jedynie przez wykształconego chirurga', 'Przez wykształconego chirurga i robota medycznego']]
]

# WARNING! DELETING ENTIRE DATABASE
db.drop_all()

db.create_all()

# CONSTANT DATA IN DATABASE

q1 = Question(text=questions_options[0][0])
q2 = Question(text=questions_options[1][0])
q3 = Question(text=questions_options[2][0])
q4 = Question(text=questions_options[3][0])

o1 = Option(number=1, option_text=questions_options[0][1][0], question_assigned=q1)
o1_1 = Option(number=2, option_text=questions_options[0][1][1], question_assigned=q1)
o1_2 = Option(number=3, option_text=questions_options[0][1][2], question_assigned=q1)


o2 = Option(number=1, option_text=questions_options[1][1][0], question_assigned=q2)
o2_1 = Option(number=2, option_text=questions_options[1][1][1], question_assigned=q2)
o2_2 = Option(number=3, option_text=questions_options[1][1][2], question_assigned=q2)

o3 = Option(number=1, option_text=questions_options[2][1][0], question_assigned=q3)
o3_1 = Option(number=2, option_text=questions_options[2][1][1], question_assigned=q3)
o3_2 = Option(number=3, option_text=questions_options[2][1][2], question_assigned=q3)

o4 = Option(number=1, option_text=questions_options[3][1][0], question_assigned=q4)
o4_1 = Option(number=2, option_text=questions_options[3][1][1], question_assigned=q4)
o4_2 = Option(number=3, option_text=questions_options[3][1][2], question_assigned=q4)


# ADD TO DATABASE

db.session.add(q1)
db.session.add(o1)
db.session.add(o1_1)
db.session.add(o1_2)

db.session.add(q2)
db.session.add(o2)
db.session.add(o2_1)
db.session.add(o2_2)

db.session.add(q3)
db.session.add(o3)
db.session.add(o3_1)
db.session.add(o3_2)

db.session.add(q4)
db.session.add(o4)
db.session.add(o4_1)
db.session.add(o4_2)


# DYNAMIC DATA (EXAMPLE)

r1 = Respondent(age=22, gender=1, med_education=True)
r2 = Respondent(age=20, gender=2, med_education=False)

db.session.add(r1)
db.session.add(r2)

db.session.commit()

a1 = Answer(respondent_id=r1.id, question_id=q1.id, option_number=o1_1.number)
a2 = Answer(respondent_id=r2.id, question_id=q1.id, option_number=o1_1.number)

db.session.add(a1)
db.session.add(a2)

db.session.commit()