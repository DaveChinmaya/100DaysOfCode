class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions = questions_list

    def next_question(self):
        current_question = self.questions[self.question_number]
        self.question_number += 1
        user_input = input(f"Question #{self.question_number}: {current_question.text} (T/F)")
        #self.check_answer(user_input,correct_answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions)

    #def check_answer(self, user_input,correct_answer):


#WhatItDoes
#TODO: 1. Ask question
#TODO: 2. Check answer is correct or not
#TODO: 3. Check if quiz has ended

