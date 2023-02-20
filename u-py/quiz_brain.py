# from classquiz import question_bank
from cgitb import text
import random
class QuizBrain:
    def __init__(self,q_list) -> None:
        self.question_number=0
        self.question_list=q_list
        self.user_score=0

    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number +=1
        user_answer=input(f"Q{self.question_number}: {current_question.text} (true/false): ")
        self.check_answer(user_answer,current_question.answer)
    def still_have_questions(self):
        return self.question_number < len(self.question_list)


    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.user_score +=1
        else:
            print("Ohh!its Wrong")
             
        print(f"The correct answer is {correct_answer}")
        print(f"The score is {self.user_score} / {self.question_number} ")