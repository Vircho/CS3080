#Assignment4.
#Author: Joshua White
#Due 3/3/25
#Matches strings that are lowercase letters joined by an underscore

#Imports
import re #regex statements

#is_lower_joined_underscore - Uses regex to check if given string matches pattern of lower-case letters
#seperated by an underscore
def is_lower_joined_underscore(string_to_check):

    #Create regex object
    #This regex matches a string containing only lowercase letters seperated by an underscore (ex: ab_cd)
    this_regex = re.compile("^[a-z]+_[a-z]+$")

    #Search string
    is_match = this_regex.search(string_to_check)

    return is_match

#Initialize string
user_string = 'x'

#Loop to let the user test inputs
while user_string != '0':

    #Get string
    user_string = input("Enter a string (To exit program, type 0): ")
    if user_string != '0':
        if is_lower_joined_underscore(user_string):
            print("Your string matches the pattern!")
        else:
            print("Your string does not match the pattern...")