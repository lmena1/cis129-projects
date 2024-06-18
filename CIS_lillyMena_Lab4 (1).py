# Module 4 Lab-4
# Lilly/Liliana Mena
# 6/17/2023
# Program takes input for a stores monthly sales and percent 
# sales increase. Then it uses those variables to calculate the # store and employee bonus.  

# declare local variables
monthlySales = 0  # monthly sales amount
storeAmount = 0  # store bonus amount
empAmount = 0  # employee bonus amountsalesIncrease = float(input(“By what percentage did the employees sales increase”))
salesIncrease = 0  # percent of sales increase
prompt = "How much were monthly sales?"

# This code gets the monthly sales

monthlySales = float(input(prompt))

# This code determines the store bonus

if monthlySales >= 110000:
	storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
	storeAmount = 4000
elif monthlySales >= 80000:
	storeAmount = 3000
else:
	storeAmount = 0



# This code gets the percent of increase in sales
salesIncrease = float(input('By what percentage did the employees sales increase? '))
salesIncrease = salesIncrease / 100


# This code determines the employee bonus
if salesIncrease >= .05:
	empAmount = 75
elif salesIncrease >= .04:
	empAmount = 50
elif salesIncrease >= .03:
	empAmount = 40
else:
	empAmount = 0
	
# This code prints the bonus information
# include code to print out all the results:
print("The store bonus amount is $", storeAmount)

print("The employee bonus amount is $",empAmount)

if (storeAmount == 6000 ) and (empAmount == 75):
	print('Congrats! You have reached the highest bonus amounts possible!')