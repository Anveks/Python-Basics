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

name_a = input("Enter the first name: ").lower()
name_b = input("Enter the second name: ").lower()
two_names = name_a + name_b

first_num = int(two_names.count('t')) + int(two_names.count('r')) + int(two_names.count('u')) + int(two_names.count('e'))
second_num = int(two_names.count('l')) + int(two_names.count('o')) + int(two_names.count('v')) + int(two_names.count('e'))

total = int(str(first_num) + str(second_num))

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total > 40 and total < 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}, I have no idea.")
