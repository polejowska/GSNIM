from website import db
from website.models import Respondent, Question, Option, Answer


# TESTING QUERIES

# questions = Question.query.all()
# print(questions[0].text)

options = Option.query.all()
print(options)

options_objects_list = Option.query.all()
options_1_question = []

for option in options_objects_list:
    print(option.question_id)
    #if option.question_assigned == id - 1:
    #    options_1_question.append(option.option_text)


print(options_1_question)