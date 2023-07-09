import os

should_continue = True # statign a boolean so we can loop the calculation
result = 0 # preparing the result and sum 
sum = {
    'num1': 0,
    'num2': 0
}

def calculator():
  global should_continue

  while should_continue: # while should_continue is true - execute the loop:
      operation = input('Please select a calculation: \n * to multiply, \n / to divide, \n + to add, \n - to subtract. \n')
      
      if sum['num1'] != 0: # is num1 is not zero: use it as num1, else get it from the prompt
          a = sum['num1']
      else:
          a = float(input('Enter the first number: '))

      b = float(input('Enter the second number: '))
      sum['num2'] = b

      if operation == '*':
          result = a * sum['num2']
          print(f'The result is: {result}')
      elif operation == '/':
          result = a / sum['num2']
          print(f'The result is: {result}')
      elif operation == '+':
          result = a + sum['num2']
          print(f'The result is: {result}')
      elif operation == '-':
          result = a - sum['num2']
          print(f'The result is: {result}')
      else:
          print('Invalid command, try again.')

      action = input('Would you like to continue counting or to exit the calculator? Type "continue" or "exit". If you want to start a new calculation, type "new". \n')
      if action == 'continue':
          sum['num1'] = result
          should_continue = True
      elif action == 'new':
          should_continue = False
          os.system('cls')
          calculator() # using recursion to start the code anew
      else:
          print('Bye bye! 👋')
          should_continue = False

calculator()