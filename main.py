# print('Day 1 - String Manipulation') - example for print("")

# print(len(input('What is your name? '))) - example for print AND input 

# name = input('What is your name? ')
# length = len(name)
# print(length)

# a = input("a: ") # 10
# b = input("b: ") # 5
# c = a # 10

# # switching the data:
# a = b
# b = c

# print(a, b) # 5 10

# print('Hello there!')
# city = input('What is the city you were born in? \n')
# pet = input('What is the name of your first pet? \n')

# print('Your bands name will be: \n' + city + " " + pet)

# str = 'Hello'
# length = len(str)
# print(str[length - 1]) # 'o'

# print(int(12.5))

# num = input('Type a number: \n')
# sum = int(num[0]) + int(num[1])
# print(sum)

# Total Bill Calculator:

# height = int(input("What is your height? \n"))
# bill = 0

# if height > 120:
#     print("You can ride rollercoaster!")
#     age = int(input("What is your age? \n"))
#     if age < 12:
#         bill += 5
#     elif age > 12 and age <= 18:
#         bill += 7
#     else:
#         bill += 12

#     photoes = bool(input("Do you want photoes? Type true or false. \n"))
#     if photoes:
#         bill += 3
#         print(f"Your bill is {bill} $")
#     else:
#         print(f"Your bill is {bill} $")
# else:
#     print("See you next year!")

# Score Calculator:

# name_a = input("Enter the first name: ").lower()
# name_b = input("Enter the second name: ").lower()
# two_names = name_a + name_b

# first_num = int(two_names.count('t')) + int(two_names.count('r')) + int(two_names.count('u')) + int(two_names.count('e'))
# second_num = int(two_names.count('l')) + int(two_names.count('o')) + int(two_names.count('v')) + int(two_names.count('e'))

# total = int(str(first_num) + str(second_num))

# if total < 10 or total > 90:
#     print(f"Your score is {total}, you go together like coke and mentos.")
# elif total > 40 and total < 50:
#     print(f"Your score is {total}, you are alright together.")
# else:
#     print(f"Your score is {total}, I have no idea.")

# import random
# names_str = input('Give me a list of names \n')
# names = names_str.split(" ")
# random_integer = random.randint(0, len(names) - 1)
# winner = names[random_integer]
# print(winner)

# LOOPS

# heights = [ 182, 170, 165, 190, 175]
# sum = 0
# num_of_elems = 0

# for height in heights:
#     sum += height
#     num_of_elems += 1

# average = sum / num_of_elems
# print(average)

#  max score in a loop:

# student_scores = input("Type all the student scores here: \n")
# student_scores_list = student_scores.split()  # Split the input string into a list

# for n in range(0, len(student_scores_list)):
#     student_scores_list[n] = int(student_scores_list[n])

# print(student_scores_list)

# max_score = 0
# for score in student_scores_list:
#     if score > max_score:
#         max_score = score

# print(max_score)

# functions practice:

# def calcPaintCans(h,w):
#     cans = (h * w) / 5
#     print(f'For such a wall you will need {cans} cans of paint.')

# height = int(input('Whats the height of the wall? \n'))
# width = int(input('Whats the width of the wall? \n'))

# calcPaintCans(h=height, w=width)    

# dictionaries practice:

# student_scores = {
#     'Harry': 81,
#     'Ron': 78,
#     'Hermione': 99,
#     'Draco': 75,
#     'Neville': 68,
# }

# student_grades = {}

# def convert_scores(score):
#     if score <= 100 and score >= 91:
#         return 'Outstanding'
#     elif score <= 91 and score >= 81:
#         return 'Exceeds Expectations'
#     elif score <= 81 and score >= 71:
#         return 'Acceptable'
#     elif score <= 71:
#         return 'Fail'

# for key in student_scores:
#     student_grades[key] = convert_scores(student_scores[key])

# print(student_grades)

#  travel log ex

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]

# def add_new_country(country, visits, cities):
#    new_country = {
#         'country': country,
#         'visits': visits,
#         'cities': cities
#    }
#    travel_log.append(new_country)

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

#  highest bidder ex:

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#          return False
#     else:
#        return True
#   else:
#     return False

# def days_in_month(year, month):
#   if year < 0 or month > 12: return 'Invalid date.'
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#   if is_leap(year) and month == 2: return int(month_days[month - 1]) + 1
#   else: return month_days[month - 1]
  
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# file = open('my_file.txt')
# content = file.read()
# print(content)












    

