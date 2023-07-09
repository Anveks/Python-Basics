from question_model import QuestionModel
from data import question_data
from quiz_base import Quiz

questions_list = []

for question in question_data:
  new_question = QuestionModel(text=question['text'], answer=question['answer'])
  questions_list.append(new_question)
  
quiz = Quiz(questions_list)

while quiz.questions_remain():
  quiz.next_question()
  
print('You have completed the quiz!')
print(f'Your final score was: {quiz.score}/{len(questions_list)}')