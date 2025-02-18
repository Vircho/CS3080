#Check a string that only has a-z, A-Z and 0-9

#imports
#provides regexes
import re
user_string = input("Enter a string, and I'll check to see if it's alphanumeric. ")

alphanum_regex = re.compile(r'^[A-Za-z0-9]+$')

match = re.match(alphanum_regex, user_string)
if match:
    print("Your string is alphanumeric.")
else:
    print("Your string is not alphanumeric.")