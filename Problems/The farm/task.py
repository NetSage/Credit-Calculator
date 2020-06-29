money = int(input())
if money >= 6769:
    count = money // 6769
    print(f"{count} sheep")
elif money >= 3848:
    count = money // 3848
    if count > 1:
        print(f"{count} cows")
    else:
        print("1 cow")
elif money >= 1296:
    count = money // 1296
    if count > 1:
        print(f"{count} pigs")
    else:
        print("1 pig")
elif money >= 678:
    count = money // 678
    if count > 1:
        print(f"{count} goats")
    else:
        print("1 goat")
elif money >= 23:
    count = money // 23
    if count > 1:
        print(f"{count} chickens")
    else:
        print("1 chicken")
else:
    print("None")
