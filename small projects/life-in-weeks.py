# this code gets your age and calculates how many weeks you've got left given that you'll live till 90 

age = input('What is your age? \n')
years_left = int(90 - int(age))

print(f"You have {int(years_left) * 365} days, {int(years_left) * 52} weeks and {int(years_left) * 12} months.")

# ☹️