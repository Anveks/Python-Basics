
# print nums from 1 to 100
# in a num is divisible by 3 print fizz instead of a num
# in a num is divisible by 4 print buzz instead of a num
# if both print fizzbuzz

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0: # should be top condition because it overlaps with the latter ones and blocks them
        num = 'fizzbuzz'
        print(num)

    elif num % 3 == 0:
        num = 'fizz'
        print(num)

    elif num % 5 == 0:
        num = 'buzz'
        print(num)

    else:
        print(num)
