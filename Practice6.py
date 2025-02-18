#have the user input two letters
#the letters HAVE to be letters, lowercase, and the first letter has to come before the second alphabetically

#variables
valid_input = False
letter1 = 'x'
letter2 = 'x'
must_be_upper = False
alphabet = []

while not valid_input:
    #Get first letter
    letter1 = input('Enter the starting character: ')
    if len(letter1) == 1:
        if letter1.isupper():
            must_be_upper = True
            if letter1.isalpha():
                valid_input = True
        else:
            must_be_upper = False
            if letter1.isalpha():
                valid_input = True

    #Move on to second letter if first letter is valid
    if valid_input:

        #assume their input won't be valid until shown otherwise
        valid_input = False

        #Get second letter
        letter2 = input('Enter the ending character: ')
        if len(letter2) == 1:
            if must_be_upper:
                if letter2.isupper():
                    if letter2.isalpha():
                        if ord(letter2) > ord(letter1):
                            valid_input = True
            else:
                if letter2.islower():
                    if letter2.isalpha():
                        if ord(letter2) > ord(letter1):
                            valid_input = True

#If both inputs are valid, print
for let in range(ord(letter1), ord(letter2) + 1):
    alphabet.append(chr(let))

print(alphabet)