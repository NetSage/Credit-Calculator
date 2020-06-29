income = int(input())


def calculate_tax(rate):
    return round(income * rate)


if income < 15528:
    print(f"The tax for {income} is 0%. That is 0 dollars!")
elif income < 42708:
    calculated_tax = calculate_tax(0.15)
    print(f"The tax for {income} is 15%. That is {calculated_tax} dollars!")
elif income < 132407:
    calculated_tax = calculate_tax(0.25)
    print(f"The tax for {income} is 25%. That is {calculated_tax} dollars!")
else:
    calculated_tax = calculate_tax(0.28)
    print(f"The tax for {income} is 28%. That is {calculated_tax} dollars!")
