#Assignment4.2
#Author: Joshua White
#Due: 3/3/25
#Uses a regex to search for a string containing an uppercase followed by lowercase

#Imports
import re #regex statements

#has_upper_lower - Uses regex to check if string contains uppercase followed by lowercase
def has_upper_lower(string_to_check):

    #Create regex object
    #Matches a string that contains an uppercase letter followed by a lowercase letter
    this_regex = re.compile("[A-Z][a-z]")

    #Search string
    is_match = this_regex.search(string_to_check)

    return is_match


#Initialize string
user_string = 'x'

# Loop to let the user test inputs
while user_string != '0':

    # Get string
    user_string = input("Enter a string (To exit program, type 0): ")
    if user_string != '0':
        if has_upper_lower(user_string):
            print("Your string matches the pattern!")
        else:
            print("Your string does not match the pattern...")