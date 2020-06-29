import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str, help="Type of calculation you want to do.")
parser.add_argument("--payment", type=int, help="What the monthly payment would be.")
parser.add_argument("--principal", type=int, help="Starting Balance.")
parser.add_argument("--periods", type=int, help="How many months or years you' need for repayment.")
parser.add_argument("--interest", type=float, help="Interest rate.")

args = parser.parse_args()


def get_nominal(base):
    return float((base / 100) / 12)


if args.type == "diff":
    if args.principal is None or args.periods is None or args.interest is None or \
                args.principal < 0 or args.periods < 0 or args.interest < 0:
        print("Incorrect Parameters")
    else:
        nominal = get_nominal(args.interest)
        overpayment = 0
        for m in range(1, args.periods + 1):
            monthly = math.ceil((args.principal / args.periods) + nominal
                                * (args.principal - (args.principal * (m - 1) / args.periods)))
            print(f"Month {m}: paid out {monthly}")
            overpayment += monthly
        overpayment = overpayment - args.principal
        print(f"Overpayment = {overpayment}")
elif args.type == "annuity":
    if args.principal and args.periods:
        if args.interest is None or args.principal < 0 or args.periods < 0 or args.interest < 0:
            print("Incorrect Parameters")
        else:
            nominal = get_nominal(args.interest)
            payment = math.ceil(args.principal * ((nominal * math.pow(1 + nominal, args.periods))
                                                  / (math.pow(1 + nominal, args.periods) - 1)))
            overpayment = math.ceil((payment * args.periods) - args.principal)
            print(f"Your annuity payment = {payment}!")
            print(f"Overpayment = {overpayment}")
    elif args.payment and args.periods:
        if args.interest is None or args.payment < 0 or args.periods < 0 or args.interest < 0:
            print("Incorrect Parameters")
        else:
            nominal = get_nominal(args.interest)
            principal = int(args.payment / ((nominal * math.pow((1 + nominal), args.periods))
                                            / (math.pow((1 + nominal), args.periods) - 1)))
            overpayment = (args.payment * args.periods) - principal
            print(f"Your credit principal = {principal}")
            print(f"Overpayment = {overpayment}")
    elif args.principal and args.payment:
        if args.interest is None or args.payment < 0 or args.principal < 0 or args.interest < 0:
            print("Incorrect Parameters")
        else:
            nominal = get_nominal(args.interest)
            months = math.ceil(math.log((args.payment / (args.payment - nominal * args.principal)), (1 + nominal)))
            if months > 12 and months % 12 == 0:
                years = months // 12
                print(f"You need {years} years to repay this credit!")
            elif months > 12:
                years = months // 12
                months = months % 12
                print(f"You need {years} years and {months} months to repay this credit!")
            elif months == 12:
                print("You need 1 year to repay this credit!")
            else:
                print(f"You need {months} months to repay this credit!")
            overpayment = (args.payment * months) - args.principal
            print(f"Overpayment: {overpayment}")
    else:
        print("Incorrect Parameters")
else:
    print("Incorrect Parameters")
