#Assignment3.1
#Author: Joshua White
#Due: 2/24/25
#Takes in a string input and uses a dictionary to find duplicate characters

#Variables
user_string = input("Enter anything, and I'll find duplicate characters! ") #The string user inputs
incrementer = 0 #incrementer value for loops
duplicates = '' #string representing all duplicate characters in user_string

#To avoid case issues, lower the string
user_string = user_string.lower()

#Create a dictionary for the string
string_dict = {}
for char in user_string:
    string_dict[incrementer] = char
    incrementer += 1
incrementer = 0

#Loop through the dictionary, for every key, see if it's value is the value of another key.
#If it is, add that value to the string + a space for formatting
#looking_key: the key whos value we're looking for
#finding_key: the key who we're looking in to find the value
for looking_key in string_dict.keys():                                  #Loop through keys
    for finding_key in string_dict.keys():                              #For each key, look through other keys
        if looking_key != finding_key:                                  #If not looking at self
            if string_dict[finding_key] == string_dict[looking_key]:    #If values are same
                if string_dict[looking_key] not in duplicates:          #And this value not already found
                    duplicates += string_dict[looking_key]              #Add to duplicates
                    duplicates += ' '                                   #Space for formatting

print(f"Duplicates found: {duplicates}")