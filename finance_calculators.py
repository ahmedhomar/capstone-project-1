import math

finance_calculator = input(
    """\n Choose either 'investment' or 'bond' from the menu below to proceed:\n
1. investment - to calculate the amount of interest you'll earn on your investment.\n
2. bond - to calculate the amount you'l pay on your home loan.\n
"""
).lower()

if finance_calculator == "investment":
    deposit = float(input("How much money will you be depositing? "))
    interest_rate = float(input("Enter the percentage interest rate: "))
    num_of_years = float(input("For how many years are you planning on investing? "))
    interest = input("Choose 'simple' or 'compound' interest: ").lower()
    if interest == "simple":
        total_amount = deposit * (1 + ((interest_rate / 100) * num_of_years))
        print(
            f"Your return on investment with simple interest applied is {total_amount:.2f}"
        )
    elif interest == "compound":
        total_amount = deposit * math.pow((1 + (interest_rate / 100)), num_of_years)
        print(
            f"Your return on investment with compound interest applied is {total_amount:.2f}"
        )

elif finance_calculator == "bond":
    house_value = float(input("What is the present value of the house? "))
    interest_rate = float(input("What is the percentage interest rate? "))
    monthly_interest = (interest_rate / 100) / 12
    num_of_months = float(input("Within how many months will you repay the bond? "))
    repayment = (monthly_interest * house_value) / (
        1 - (1 + monthly_interest) ** (-num_of_months)
    )
    print(f"Your monthly repayments will be: £{repayment:.2f}")

else:
    print("Something went wrong: please check and try again.")
