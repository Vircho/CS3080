#Variables
entered_correct = False
bad_input = False
lines = 0

#Get a positive integer to represent amount of lines
while not entered_correct:

    #As long as user has not entered, it's not a bad input yet
    bad_input = False

    #Get input
    lines = input('How many lines should the triangle be? ')

    #Test for being an integer
    try:
        lines = int(lines)
    except ValueError:
        print('Please enter a number.')
        bad_input = True

    #Test for positive if it's a number
    if (not bad_input) and (lines <= 0):
        print('Please enter a positive integer')
        bad_input = True

    #Exit if not a bad input
    if not bad_input:
        entered_correct = True

#Print a increasing, right-oriented triangle based on number of lines
for star in range(1, lines + 1):
    print(' ' * (lines - star) + '*' * star)