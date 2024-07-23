import csv

with open('grades.txt', mode='w') as grades:
    grade_counter = 0 
    total=0
    grades_entered = int(input('Enter grade, -1 to end : '))
    while grades_entered != -1:
        grade_counter += 1
        total += int(grades_entered)
        grades.write(f'{grades_entered}\n')
        grades_entered = (int(input('Enter grade, -1 to end : ')))

if grade_counter != 0:
    average= average=total/grade_counter
else:
    average='No grades were entered'

with open ('grades.txt', mode='r') as grades:
    #initializing variables
    total=0 
    grade_counter=0
    print()#formatting preference
    print(f'{'Grades:'} ')
    for record in grades:
        grade_counter += 1
        total += int(record)
        print(f'{record}', end='')
print()#formatting preference
print(f'{'Count:'} \n{(grade_counter)}') # uses grade counter to display the number of entries in grade.txt
print()#formatting preference
print(f'{'Average:'}\n{average}') # uses total and grade counter to determine average
print()#formatting preference

# Takes in each student's information from user and stores each as a record in a csv file format.
with open ('grades.csv', mode='w', newline ='') as grades:
        score=0
        while score != '-1':
            #Double qoutes used because of the need for an internal " ' " for posessive
            first_name = input("Enter student's first name : ")
            last_name = input("Enter student's last name : ")
            exam1grade = (input("Enter student's score on first exam: "))
            exam2grade = (input("Enter student's score on second exam: "))
            exam3grade = (input("Enter student's score on third exam: "))
            writer = csv.writer(grades)
            record = writer.writerow([first_name,last_name,exam1grade,exam2grade,exam3grade])
            score = (input("If you'd like to quit entering in records students, input -1. If you'd like to continue inputting records for your class, enter something else.")) # assess whether user would like to continue entering in record information



#below is a loop I used from the book to test if the last code adds and extracts the way intended
'''with open ('grades.csv', mode='r', newline ='') as grades:
    print()
    print(f'{"First":<10}{"Last":<10}{"Exam 1":<10}{"Exam 2":<10}{"Exam 3":<10}')
    reader = csv.reader(grades)
    for record in reader: 
        print(record)
        first_name,last_name,exam1grade,exam2grade,exam3grade = record 
        print (f'{first_name:<10}{last_name:<10}{exam1grade:<10}{exam2grade:<10}{exam3grade:<10}')'''