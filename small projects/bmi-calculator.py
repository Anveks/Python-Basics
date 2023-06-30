# BMI Calculator:

weight = input("What is your weigth? ")
height = input("What is your heigth? ")
BMI = (int(float(weight) / (float(height) ** 2)))

if BMI <= 18.5:
    print(f"BMI {BMI}, you are underweight.")
elif BMI < 25:
     print(f"BMI {BMI}, you have a normal weight.")
elif BMI < 30:
     print(f"BMI {BMI}, you are overweight.")
elif BMI < 35:
     print(f"BMI {BMI}, you are obese.")
else:
     print(f"BMI {BMI}, you are clinically obese.")
