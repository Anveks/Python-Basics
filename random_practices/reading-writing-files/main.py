import os

# current_directory = os.getcwd()
# print('DIRECTORY: ')
# print(current_directory)

# ONE WAY:
# file = open('my_file.txt')
# content = file.read()
# print(content)
# file.close()

# ANOTHER WAY:
with open('random_practices/my_file.txt', mode='r') as file: # mode = "read only"
  content = file.read()
  print(content)
  
with open('random_practices/new_file.txt', mode='w') as file: # mode = 'write'
  file.write('My name is Darth Vader.')