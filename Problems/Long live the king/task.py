row = int(input())
column = int(input())

if (row == 1 or row == 8) and (column == 1 or column == 8):
    print(3)
elif row == 1 or row == 8 or column == 1 or column == 8:
    print(5)
else:
    print(8)
