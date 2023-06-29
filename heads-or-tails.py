import random

print('This is a heads or tails game.')

random_num = random.randint(0, 1)

print("Throwing a coin... 🪙")

if random_num == 0:
    print("Tails!")
else:
    print("Heads!")

# One line: print("Heads!" if random.randint(0, 1) else "Tails!")