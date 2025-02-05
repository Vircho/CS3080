#Variables
year = 0
entered_year = False
bad_input = False

#Ask the user to enter a calendar year, loop until they enter a year
while not entered_year:

    #As long as user has not entered a value, their input is not yet bad
    bad_input = False

    #Get a year from the user
    year = input('Enter a year! ')

    #Check that user inputted an integer
    try:
        year = int(year)
    except ValueError:
        print('You did not enter a year')
        bad_input = True

    if not bad_input:
        entered_year = True

#Check if it is a leap year
#If the year is a divisor of 400, it's a leap year
if year % 400 == 0:
    print('That year is a leap year!')

#If the year is a divisor of 4, but not by 100, it's a leap year
elif (year % 4 == 0) and (year %100 != 0):
        print('That year is a leap year!')

#Otherwise, it's not a leap year
else:
    print('That year is not a leap year!')