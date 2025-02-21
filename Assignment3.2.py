#Assignment3.2
#Author: Joshua White
#Due: 2/24/25
#Sets the upper half of a string to uppercase, and the lower half to lower case

#imports
import math #math allows me to use the ceil() function

#Initially get the string
user_string = input("Enter a word, and I'll set the upper half to uppercase! ")

#Force user to enter only letters
while not user_string.isalpha():
    print("Only letters are allowed!")
    user_string = input("Enter a word, and I'll set the upper half to uppercase! ")

#Split the string in half

#use ceil to ensure that in cases of odd-numbered strings, the floating point is rounded up
#This is because when I use string-slicing later, I have to account for non-inclusivity
half_mark = math.ceil(len(user_string) / 2)

#Use string-slicing to make two strings for upper and lower half
lower_half = user_string[:half_mark]
upper_half = user_string[half_mark:]

#lower and upper the two halves
lower_half = lower_half.lower()
upper_half = upper_half.upper()

#Combine the strings back together
user_string = lower_half + upper_half

#Print the final string
print(f"Result: {user_string}")