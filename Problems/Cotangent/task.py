import math


angle = int(input())
radians = angle * (math.pi / 180)

print(round(math.cos(radians) / math.sin(radians), 10))
