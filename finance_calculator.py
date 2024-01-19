""" Allow user to calculate the interest earned on an investment or
owed on a loan."""
import math

print("------ Capstone Project ------")
print()

# Print glossary to console to explain options to user
print("investment\t- to calculate the amount of interest you'll earn on your investment")
print("bond\t\t- to calculate the amount you'll have to pay on a home loan")
print()

while True:
    try:

        # User chooses between two initial options: 'investment' and 'bond'
        user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
        user_choice_caseless = user_choice.casefold()

        # if block: if user_choice_caseless doesn't match 'investment' or 'bond':
            # print error message
        if user_choice_caseless not in ('investment', 'bond'):
            raise Exception(f"Sorry, '{user_choice}' does not match 'investment' or 'bond'.")
        break

    except Exception as e:
        print(e)

while True:

    # if block: INVESTMENT scenario
    # Prompt user to input details of their investment, then choose type of interest
    if user_choice_caseless == "investment":
        deposit_amount = float(input("Enter the amount you wish to deposit: "))
        interest_value = float(input("Enter the interest rate (without a '%'): "))
        investment_period_years = float(input("Enter the number of years you will "
                                            "leave your investment: "))
        interest_type = input("What type of interest? Enter 'simple' or 'compound': ")
        interest_rate = interest_value / 100

        # Interest type - SIMPLE
        if interest_type == "simple":
            total_simple = deposit_amount * (1 + interest_rate * investment_period_years)
            print(f"After {int(investment_period_years)} years, your £{int(deposit_amount)} "
                f"investment will be worth £{total_simple:,.2f}.")
            print()
            break

        # Interest type - COMPOUND
        if interest_type == "compound":
            total_compound = deposit_amount * math.pow((1 + interest_rate),investment_period_years)
            print(f"After {int(investment_period_years)} years, your £{int(deposit_amount)} "
                f"investment will be worth £{total_compound:,.2f}.")
            print()
            break

    #  if block: BOND scenario
    # Prompt user to enter details of bond
    elif user_choice_caseless == "bond":
        bond_value = float(input("Enter the current value of the bond: "))
        interest_value = float(input("Enter the interest rate (without a '%'): "))
        months_repayment = float(input("Enter the number of months you intend to take "
                                        "to repay the bond: "))
        monthly_interest_rate = (interest_value / 100) / 12

        monthly_repayment_value = (monthly_interest_rate*bond_value)  \
                                / (1 - (1 + monthly_interest_rate) ** (-months_repayment))

        print()
        print(f"Your monthly repayments will be £{monthly_repayment_value:,.2f} for "
            f"{int(months_repayment)} months.")
        print()
        break
