from website import db
from website.models import Respondent, Question, Option, Answer


questions_options = [
    ['Czy byłby/byłaby Pana(i) gotowa w przypadku wymaganego leczenia na podjęcie leczenia lekami, które zostały wytworzone według Pana(i) kodu genetycznego?', ['Tak', 'Nie', 'Trudno powiedzieć']],
    ['Czy byłaby Pan(i) w stanie zapłacić więcej na badanie wykorzystujące nowsze technologie?', ['Tak', 'Nie', 'Trudno powiedzieć']],
    ['W razie wymaganego zabiegu chirurgicznego byłby(/byłaby Pan(i) w stanie być operowanym przez:', ['Tylko przez robota medycznego (w przypadku 100% pewności jego prawidłowego działania)', 'Jedynie przez wykształconego chirurga', 'Przez wykształconego chirurga i robota medycznego']]
]

questions_options_experience = [
    ['Czy Pan(i) brała udział w badaniu lub zabiegu, w którym wykorzystywane były zaawansowane technologie? (Przykład: tomografia komputerowa, MRI, .....)', ['Tak', 'Nie', 'Nie wiem']]
]

questions_options_fears = [
    ['Czy Pan(i) byłby/byłaby w stanie wspomóc innowacje technologiczne związane ze zdrowiem poprzez anonimowe udostępnienie własnych danych medycznych? (np. zdjęcia rentgenowskie, przebiegi chorób, wyniki badań)', ['Tak', 'Nie']],
    ['Czy Pan(i) byłby/byłaby w stanie wspomóc innowacje technologiczne związane ze zdrowiem poprzez anonimowe udostępnienie własnych danych medycznych? (np. zdjęcia rentgenowskie, przebiegi chorób, wyniki badań)', ['Tak', 'Nie']],
    ['Czy Pan(i) byłby/byłaby w stanie wspomóc innowacje technologiczne związane ze zdrowiem poprzez anonimowe udostępnienie własnych danych medycznych? (np. zdjęcia rentgenowskie, przebiegi chorób, wyniki badań)', ['Tak', 'Nie']]
]

questions_options_knowledge = [
    ['Czy byłby/byłaby Pan(i) zainteresowana badaniem predyspozycji genetycznych?', ['Tak', 'Nie']],
    ['Czy jest Pan(i) świadomy korzyści jakie przynosi sztuczna inteligencja medycynie?', ['Tak', 'Nie']],
    ['Da Vinci jest zaawansowanym robotem medycznym, z użyciem tego systemu wykonano już ponad 7,2 mln operacji na świecie. Liczba aparatów da Vinci w Polsce wynosi ... (Stan na czerwiec 2020)', ['2 sztuki', 'około 10 sztuk', 'około 100 sztuk', 'około 1000 sztuk']],
    ['Czy uważa Pan(i), że sztuczna inteligencja potrafi przewidzieć stan zdrowia pacjenta na podstawie odpowiednich danych?', ['Tak', 'Nie']],
    ['Telemedycyna to rozwiązanie, które jest wykorzystywane:', ['Jako uzupełnienie tradycyjnych form opieki medycznej', 'Zamiast tradycyjnej opieki medycznej', 'Tylko ze względu na epidemię COVID-19']]
]

# WARNING! DELETING ENTIRE DATABASE
db.drop_all()

db.create_all()

# CONSTANT DATA IN DATABASE

q1 = Question(text=questions_options_experience[0][0])
q2 = Question(text=questions_options[1][0])
q3 = Question(text=questions_options_fears[0][0])
q4 = Question(text=questions_options_fears[1][0])
q5 = Question(text=questions_options_fears[2][0])

q6 = Question(text=questions_options_knowledge[0][0])
q7 = Question(text=questions_options_knowledge[1][0])
q8 = Question(text=questions_options_knowledge[2][0])
q9 = Question(text=questions_options_knowledge[3][0])
q10 = Question(text=questions_options_knowledge[4][0])
#q4 = Question(text=questions_options[3][0])

o1 = Option(number=1, option_text=questions_options[0][1][0], question_assigned=q1)
o1_1 = Option(number=2, option_text=questions_options[0][1][1], question_assigned=q1)
o1_2 = Option(number=3, option_text=questions_options[0][1][2], question_assigned=q1)

o2 = Option(number=1, option_text=questions_options[1][1][0], question_assigned=q2)
o2_1 = Option(number=2, option_text=questions_options[1][1][1], question_assigned=q2)
o2_2 = Option(number=3, option_text=questions_options[1][1][2], question_assigned=q2)

o3 = Option(number=1, option_text=questions_options[0][1][0], question_assigned=q3)
o3_1 = Option(number=2, option_text=questions_options[0][1][1], question_assigned=q3)

o4 = Option(number=1, option_text=questions_options_fears[1][1][0], question_assigned=q4)
o4_1 = Option(number=2, option_text=questions_options_fears[1][1][1], question_assigned=q4)

o5 = Option(number=1, option_text=questions_options_fears[2][1][0], question_assigned=q5)
o5_1 = Option(number=2, option_text=questions_options_fears[2][1][1], question_assigned=q5)

o6 = Option(number=1, option_text=questions_options_knowledge[0][1][0], question_assigned=q6)
o6_1 = Option(number=2, option_text=questions_options_knowledge[0][1][1], question_assigned=q6)

o7 = Option(number=1, option_text=questions_options_knowledge[1][1][0], question_assigned=q7)
o7_1 = Option(number=2, option_text=questions_options_knowledge[1][1][1], question_assigned=q7)

o8 = Option(number=1, option_text=questions_options_knowledge[2][1][0], question_assigned=q8)
o8_1 = Option(number=2, option_text=questions_options_knowledge[2][1][1], question_assigned=q8)
o8_2 = Option(number=3, option_text=questions_options_knowledge[2][1][2], question_assigned=q8)
o8_3 = Option(number=4, option_text=questions_options_knowledge[2][1][3], question_assigned=q8)

o9 = Option(number=1, option_text=questions_options_knowledge[3][1][0], question_assigned=q9)
o9_1 = Option(number=2, option_text=questions_options_knowledge[3][1][1], question_assigned=q9)

o10 = Option(number=1, option_text=questions_options_knowledge[4][1][0], question_assigned=q10)
o10_1 = Option(number=2, option_text=questions_options_knowledge[4][1][1], question_assigned=q10)
o10_2 = Option(number=3, option_text=questions_options_knowledge[4][1][2], question_assigned=q10)

#o4 = Option(number=1, option_text=questions_options[3][1][0], question_assigned=q4)
#o4_1 = Option(number=2, option_text=questions_options[3][1][1], question_assigned=q4)
#o4_2 = Option(number=3, option_text=questions_options[3][1][2], question_assigned=q4)


# ADD TO DATABASE

db.session.add(q1)
db.session.add(o1)
db.session.add(o1_1)
db.session.add(o1_2)

db.session.add(q2)
db.session.add(o2)
db.session.add(o2_1)


db.session.add(q3)
db.session.add(o3)
db.session.add(o3_1)


db.session.add(q4)
db.session.add(o4)
db.session.add(o4_1)


db.session.add(q5)
db.session.add(o5)
db.session.add(o5_1)

db.session.add(q6)
db.session.add(o6)
db.session.add(o6_1)

db.session.add(q7)
db.session.add(o7)
db.session.add(o7_1)

db.session.add(q8)
db.session.add(o8)
db.session.add(o8_1)
db.session.add(o8_2)

db.session.add(q9)
db.session.add(o9)
db.session.add(o9_1)

db.session.add(q10)
db.session.add(o10)
db.session.add(o10_1)
db.session.add(o10_2)


# DYNAMIC DATA (EXAMPLE)

r1 = Respondent(age=22, gender=1, med_education=True, place=1)
r2 = Respondent(age=20, gender=2, med_education=False, place=2)

db.session.add(r1)
db.session.add(r2)

db.session.commit()

a1 = Answer(respondent_id=r1.id, question_id=q1.id, option_number=o1_1.number)
a2 = Answer(respondent_id=r2.id, question_id=q1.id, option_number=o1_1.number)

db.session.add(a1)
db.session.add(a2)

db.session.commit()