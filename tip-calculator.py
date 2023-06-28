
bill = int(input('How much is the bill? '))
tip = bill / 100 * int(input("How much is the tip? 10, 12 or 15? "))
people = int(input('How many people want to pay? '))

print(f"The final bill including the tip will be: {bill + tip}. Per one person that would be {(bill + tip) / people}")