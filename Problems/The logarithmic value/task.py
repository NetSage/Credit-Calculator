import math


number1 = int(input())
number2 = int(input())

if number2 <= 1:
    print(round(math.log(number1), 2))
else:
    print(round(math.log(number1, number2), 2))
