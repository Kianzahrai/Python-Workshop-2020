# Estimated Yearly Interest:

print("How many years will you be saving?")
years = int(input("Enter number of years: "))

print("How much money is currebtly in your account?")
principal = float(input("Enter current amount in account: "))

print("How much money do you plan on investing monthly?")
monthly_invest = float(input("Enter amount: "))

print("What do you estimate will be the yearly interest of this investment?")
interest = float(input("Enter interest in decimal numbers (10% = 0.1): "))

print(" ")

monthly_invest = monthly_invest * 12
# OR above line is same as monthly_invest *= 12
final_amount = 0

for i in range(0, years):
    if final_amount == 0:
        final_amount = principal

    final_amount = (final_amount + monthly_invest) * (1 + interest)

# OR say:print("This is how much money you would have in your account after {} years: ".format(years) + str(final_amount))
print("This is how much money you would have in your account after " + str(years) + " years: " + str(final_amount))
