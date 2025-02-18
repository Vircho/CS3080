#Program Assignment2.1
#Author: Joshua White
#Due: 2/17/25
#Utilizes a function three_consecutive that takes in a list, and returns a boolean value indicating
#if there is a case where 3 elements exist consecutively in that list

#three_consecutive - returns boolean of if in the list, there are 3 numbers that exist in a row
def three_consecutive(numbers):

    #variables
    seen_times = 0  #amount of times in a row the element has been seen
    is_consecutive = False #what function returns - is there 3 consecutive numbers in the

    #Test for bad info
    try:

        #for loop catches ints, floats, and bools as they cannot be enumerated
        for index, number in enumerate(numbers):

            #This attempt to typecast to an int catches strings and strings inside a list
            try:
                numbers[index] = int(numbers[index])
            except ValueError:
                print("Error: Either not a list or non-number inside of list")
                return

    except TypeError:
        print("Error: Incorrect type. Correct type is list")
        return False

    #loop through the list
    for index, element in enumerate(numbers):

        #Set the seen_times if at the start of the list
        if index == 0:
            seen_times = 1

        #otherwise go through the logic
        else:

            #if this element is the same as the last element, increment
            if element == numbers[index - 1]:
                seen_times += 1

            #do logic if this element is different from the last element
            else:

                #set the is_consecutive if it has been seen exactly 3 times
                if seen_times == 3:
                    is_consecutive = True

                #Set the amount of times this number has been seen to 1
                seen_times = 1


    print(is_consecutive)
    return is_consecutive

#Test for good input
three_consecutive([-4, 9, 9, 9, 3, 8])
three_consecutive([5, 3, 3, 7, 7, -2])
three_consecutive([12, 12, 12, 12, 5, 5, 5, 2, 2, 2])
three_consecutive([])
three_consecutive([1, 1])

#Test for bad input
three_consecutive(1)
three_consecutive("string")
three_consecutive(True)
three_consecutive(1.1)