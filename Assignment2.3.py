#Program Assignment2.3
#Author: Joshua White
#Due: 2/17/25
#Utilizes a function get_random_from_list that takes a list and returns a random element from that list

#imports
import random

#get_random_from_list - Returns a random element from an inputted list
def get_random_from_list(this_list):

    #Check that the list is a list first
    if not check_for_list(this_list):
        print("Error: Inputted list is not a list")
        return None
    else:

        #generate a random number from 0 to the final index and return the element in that index
        random_element = random.randint(0, len(this_list) - 1)
        return this_list[random_element]

#check_for_list - Returns a boolean indicating if the variable passed to function is a list
def check_for_list(this_list):

    #Variable is a list until proven otherwise
    is_list = True

    #If it can't be enumerated, it isn't a list
    try:
        for index, element in enumerate(this_list):
            #None as I don't want to actually do anything, I am simply checking if it can be enumerated
            None
    except TypeError:
        is_list = False

    return is_list

#Good tests
print(get_random_from_list([5, -9, 70, 15]))
print(get_random_from_list([0, 1, 2, 3, 4, 7, 12]))

#Bad tests
print(get_random_from_list(1))
