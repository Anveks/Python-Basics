# import random 

# student_names = {'Dave', 'Tom', 'John', 'Lucas', 'Alice', 'Jake', 'Dean', 'Sam', 'Caroline', 'Jane', 'Matthew', 'Chloe'}
# student_grades = { student: random.randint(1, 100) for student in student_names }

# passed_students = { student:grade for (student, grade) in student_grades.items() if grade >= 60 }

# print(student_grades)
# print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_list = sentence.split()
result = { word:len(word) for word in word_list }

weather_c = { 'Monday': 12, 'Tuesday': 14, 'Wednesday': 15, 'Thursday': 14, 'Friday': 20, 'Saturday': 22, 'Sunday': 24 }

def convert_temp(temp):
  return (temp * 9/5) + 32

weather_f = { day:convert_temp(weather) for (day, weather) in weather_c.items() }

print(weather_f)
print(weather_c.items())