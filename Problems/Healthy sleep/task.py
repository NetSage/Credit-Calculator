minimum = int(input())
maximum = int(input())
sleep = int(input())

if sleep > maximum:
    print("Excess")
elif sleep < minimum:
    print("Deficiency")
else:
    print("Normal")
