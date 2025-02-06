#Variables
entered_correct = False
bad_input = False
lines = 0
stars = 1
spaces = 0

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

#Print an increasing, middle-oriented triangle without spaces based on number of lines
for this_line in range(0, lines):
    print(' ' * (lines - this_line - 1) + '*' * stars + ' ' * (lines - this_line - 1))
    stars = stars + 2