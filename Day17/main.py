from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

q_list = QuizBrain(question_bank)
q_list.next_question()

while q_list.still_has_questions():
    q_list.next_question()
