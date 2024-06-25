#CIS129_YourName_Lab5.py


#Lilly Mena
#6/24/2024
# Lab 5 The Bottle Return Program

#program takes input for bottles collected each day, 
# then it displays the sum of bottle collected over a week 
# and from there calculated the total payout for bottles that week

def main():
    # Step 1: Declare variables below 
    #initializing Variables
    total_bottles= 0
    counter= 0
    today_bottles = 0
    total_payout = 0 
    keep_going = 'y'

# Step 2: Loop to run program again
#loops the following set of code
    while keep_going == 'y':
        print('>>>')
        days_of_the_week=7
        # makes sure each time the while loop runs this section inside it only runs 7 times
        while counter < days_of_the_week:
             #gets input from user
             today_bottles = input(f"Enter number of bottles for day# {counter+1}:  ")
             #updates total bottle count for each "today bottle entry"
             total_bottles += int(today_bottles)
             #ensures loop iterates the correct # of times
             counter +=1
             total_payout = total_bottles *0.1
        #prints info and upholds formatting
        print()
        print(f'The total number of bottles collected is {total_bottles}')
        print(f'The total paid out is $ {total_payout:.1f}')
        print()
        #reasking affirming the variable that keeps the loop or breaks it
        keep_going = input('Do you want to enter another week’s worth of data? \n (Enter y or n): ')
        print('>>>')
        #resets vars so total_bottle & payout calculations are only for 1 loop/7days
        counter = 0
        total_payout= 0
        total_bottles=0
      

main()


             




