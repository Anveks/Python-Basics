
class Quiz:
  def __init__(self, question_list) -> None:
    self.question_number = 0
    self.question_list = question_list
    self.score = 0
    
  def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(f'Q.{self.question_number}: {current_question.text} (True/False)\n')
    correct_answer = current_question.answer
    self.check_answer(user_answer, correct_answer)
    
  def questions_remain(self):
    return self.question_number < int(len(self.question_list))
  
  def check_answer(self, user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower(): 
      self.score += 1
      print(f'Thats right! Your current score is: {self.score}/{len(self.question_list)}.')
      print('\n')
    else: 
      print(f'Wrong! Your current score is: {self.score}/{len(self.question_list)}')
      print('\n')