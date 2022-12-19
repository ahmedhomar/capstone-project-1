# The user is asked to select a calculation from a list of options.
# The user is then asked to enter the relevant data for the calculation.
# The calculation is performed and the result is printed.
#
# Args:
#   finance_calculator: The type of calculation to be done.
#   deposit: The amount of money you are investing.
#   interest_rate: The interest rate of the investment
#   num_of_years: The number of years you plan on investing the money.
#   interest: The type of interest to be applied.
#   house_value: The current value of the house.
#   num_of_months: The number of months required to repay the bond
# Returns:
#   The final value of the investment OR monthly repayments (depending on the type of investment).


import math

finance_calculator = input(
    """
Select 'investment' or 'bond' from the menu below to proceed:

1. investment - to calculate the amount of interest you'll earn on your investment.
-------------------------------------------------------------------------------------
2. bond - to calculate the amount you'l repay on your home loan each month.

"""
).lower()

# Finance calculator for: 'investment + simple interest' and investment + compound interest.
if finance_calculator == "investment":
    deposit = float(input("How much money will you be investing? "))
    interest_rate = float(input("Enter the percentage interest rate: "))
    num_of_years = float(
        input("How many years are you planning on investing this sum? ")
    )
    interest = input(
        "Select the type of interest to be applied: 'simple' or 'compound': "
    ).lower()
    if interest == "simple":
        total_amount = deposit * (1 + ((interest_rate / 100) * num_of_years))
        print(
            f"""
            Investment Type: Investment
            ----------------------------------------------------------------
            Invested Amount: £{deposit:.2f}
            ----------------------------------------------------------------
            Interest Rate: {interest_rate:.2f} %
            ----------------------------------------------------------------
            Years of investment: {num_of_years:.0f}
            ----------------------------------------------------------------
            Interest Type: Simple
            ----------------------------------------------------------------
            Return on Investment (with interest): £{total_amount:.2f}
            ----------------------------------------------------------------
            """
        )
    elif interest == "compound":
        total_amount = deposit * math.pow((1 + (interest_rate / 100)), num_of_years)
        print(
            f"""
            Investment Type: Investment
            ----------------------------------------------------------
            Invested Amount: £{deposit:.2f}
            ----------------------------------------------------------------
            Interest Rate: {interest_rate:.2f} %
            ----------------------------------------------------------------
            Years of investment: {num_of_years:.0f}
            ----------------------------------------------------------------
            Interest Type: Compound
            ----------------------------------------------------------------
            Return on Investment (with interest): £{total_amount:.2f}
            ----------------------------------------------------------------
            """
        )
    # To catch any errors:
    else:
        print("Something went wrong: please check and try again.")

# Finance Calculator for monthly repayments from a bond:
elif finance_calculator == "bond":
    house_value = float(input("What is the present value of the house? "))
    interest_rate = float(input("What is the percentage interest rate? "))
    monthly_interest = (interest_rate / 100) / 12
    num_of_months = float(input("Over how many months will the bond be repaid? "))
    repayment = (monthly_interest * house_value) / (
        1 - ((1 + monthly_interest) ** (-num_of_months))
    )
    print(
        f"""
          Investment Type: Bond
          ------------------------------------------------
          Present Value of House: £{house_value:.2f}
          ------------------------------------------------
          Annual interest Rate: {interest_rate} %
          ------------------------------------------------
          Monthly Interest Rate: {monthly_interest} %
          ------------------------------------------------
          Months of Repayment: {num_of_months:.0f}
          ------------------------------------------------
          Monthly Repayments: £{repayment:.2f}"""
    )
# To catch any errors:
else:
    print("Something went wrong: please check and try again.")
