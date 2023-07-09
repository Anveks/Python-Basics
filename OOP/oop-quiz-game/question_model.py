
class QuestionModel:
  def __init__(self, text: str, answer: bool):
    self.text = text
    self.answer = answer
    
  def __str__(self) -> str:
    return f'Question: {self.text}, Answer: {self.answer}' 
   