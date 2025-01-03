from time import sleep


class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_ans  = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_ans(user_ans, current_question.ans)


    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_ans(self,user_ans,correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("You got it right!")

        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_ans}")
        print(f"Your current score is: {self.score}/{self.question_number}")