import math

n = int(input('Check this number: \n'))

def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False

  if not is_prime: print('The number is not prime. ❌')
  else: print('The number is prime. 🎉')


prime_checker(number=n)
