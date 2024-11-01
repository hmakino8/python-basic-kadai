import sys
import random

var = random.randint(1, sys.maxsize)

if var % 3 == 0 and var % 5 == 0:
    print("FizzBuzz")
elif var % 3 == 0:
    print("Fizz")
elif var % 5 == 0:
    print("Buzz")
else:
    print(var)
