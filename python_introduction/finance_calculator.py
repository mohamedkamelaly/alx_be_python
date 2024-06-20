#Use user input, variables, and arithmetic operations to calculate and provide feedback on a user’s monthly savings 
# and potential future savings without applying conditional statements.
income = input("Enter your monthly income: ")
expenses = input ("Enter your total monthly expenses: ")
monthly_savings = float(income) - float(expenses)
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05) 
print ("Your monthly savings are $" + str(monthly_savings))
print ("Projected savings after one year, with interest, is: $" + str(annual_savings))
