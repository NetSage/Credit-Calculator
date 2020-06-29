# put your python code here
a = int(input())
b = int(input())
numbers = []

for i in range(a, b + 1):
    if i % 3 == 0:
        numbers.append(i)

print(sum(numbers) / len(numbers))
