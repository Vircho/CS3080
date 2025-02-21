#Assignment3.3
#Author: Joshua White
#Due: 2/24/25
#Counts amount of characters in a string excluding spaces

user_string = input('''Enter a string and I'll tell you how many characters there are!
(spaces are not included): ''')

characters = 0

for char in user_string:
    if not char.isspace():
        characters += 1

print(f"There are {characters} characters.")