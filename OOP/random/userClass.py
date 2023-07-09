class User: 
  def __init__(self, user_id: str, username: str) -> None:
    self.id = user_id
    self.username = username
    self.followers = 0
    self.following = 0
  
  def follow(self, user) -> None:
    user.followers += 1
    self.following += 1   
  

user_1 = User('1', 'Anna')
user_2 = User('2', 'Clark')
user_3 = User('3', 'Jack')

user_1.follow(user_2)
user_1.follow(user_3)
print(user_1.followers)  
print(user_1.following)  