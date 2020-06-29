import math


number = int(input())

area = round(2 * math.sqrt(3) * math.pow(number, 2), 2)
volume = round((1 / 3) * math.sqrt(2) * math.pow(number, 3), 2)

print(f"{area} {volume}")
