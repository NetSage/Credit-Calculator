# put your python code here
number1 = float(input())
number2 = float(input())
action = input()

if action == "+":
    print(number1 + number2)
elif action == "-":
    print(number1 - number2)
elif action == "/":
    if number2 == 0:
        print("Division by 0!")
    else:
        print(number1 / number2)
elif action == "*":
    print(number1 * number2)
elif action == "mod":
    if number2 == 0:
        print("Division by 0!")
    else:
        print(number1 % number2)
elif action == "pow":
    print(number1 ** number2)
else:
    if number2 == 0:
        print("Division by 0!")
    else:
        print(number1 // number2)
