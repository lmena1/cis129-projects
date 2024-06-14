'''The purpose of this program is to calculate and print out the bill 
for a customer. Bill remains accurate regardless of initial inputs provided by the user.'''

'''The following block stores certain formatting as variables, uses said variables and asks the user for the quantity of items purchased
 which is also stored. '''
# I stored formatting variables because I wanted to eliminate potential printing errors, reduce time spent typing and ensure a clean appearance.
# I stored inputs as variables so that I could use them to calculate the bill in a later block of code.

title = "My Coffee and Muffin Shop"
stars = "**************************"
print(stars)
print(title)
quant_coffee = int(input("Number of coffees bought?\n"))   #\n serves to ensure the formatting depicted for this lab.
quant_muffin = int(input("Number of muffins bought?\n"))   #\n serves to ensure the formatting depicted for this lab.
print(stars)
print()

'''The following block of code serves to calculate and store different values needed before printing the final bill'''
#These are calculations based on input that I stored as variables.
#They allow me plug something into the print statement that is dynamic to input and correct.
coffee_bill = quant_coffee * 5.00
muffin_bill = quant_muffin * 4.00
tax = (coffee_bill + muffin_bill) * 0.06
total = muffin_bill + coffee_bill + tax

'''The following block prints out the receipt for the customer. the unchanging parts are hard-coded 
as strings and combined with a comma or plus symbol to concatenate with variable amounts'''
#after the calculations have been made and stored as variables,
# I can hard-code the un-changing parts of
print(stars,"\n"+title,'Receipt') #\n appearing in print statement to reduce lines of code while ensuring specified format.
print(quant_coffee,"Coffee at $5 each:","$",str(coffee_bill)+"0") # +"0" is because amounts were shown with 1 decimal as opposed to 2
print(quant_muffin,"Muffins at $4 each:","$",str(muffin_bill)+"0") #+"0" is because amounts were shown with 1 decimal as opposed to 2
print("%6 tax: $",tax)
print("---------")
print("Total: $",total,"\n"+stars)#\n appearing in print statement to reduce lines of code while ensuring specified format.
