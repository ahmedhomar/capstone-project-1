import math

finance_calculator = input(
    f"""\nChoose either 'investment' or 'bond' from the menu below to proceed:
1. investment - to calculate the amount of interest you'll earn on your investment.
2. bond - to calculate the amount you'l pay on your home loan.
"""
).lower()

if finance_calculator == "investment":
    deposit = float(input("How much money will you be depositing? "))
    interest_rate = float("What is the percentage interest rate? ")
    num_of_years = float(
        "For how many years are you planning on investing this money? "
    )
    interest = input("Please choose 'Simple' or 'Compound' interest: ")
