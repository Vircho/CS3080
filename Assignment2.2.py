#Program Assignment2.2
#Author: Joshua White
#Due: 2/17/25
#Utilizes a function merge_and_sort that takes 2 sorted lists, and merges them into 1 sorted list

#merge_and_sort - takes 2 lists, merges them, and sorts them in ascending order
def merge_and_sort(list1, list2):

    #Inputs must be lists with numbers, so check that they are first
    list1_valid = check_list_is_numeric(list1)
    list2_valid = check_list_is_numeric(list2)

    if not list1_valid or not list2_valid:
        print(f'The first lists validity is {list1_valid} and the second lists validity is {list2_valid}')
        print('Please fix the invalid list(s).')

    #Lists must be sorted, so check that they are first
    else:
        list1_valid = check_list_is_sorted(list1)
        list2_valid = check_list_is_sorted(list2)
        if not list1_valid or not list2_valid:
            print(f'The first lists validity is {list1_valid} and the second lists validity is {list2_valid}')
            print('Please fix the invalid list(s).')

    #variables
    new_list = list()

    #If the lists are valid to be merged and sorted, merge and sort them
    if list1_valid and list2_valid:

        #merge lists
        new_list = list1 + list2

        #sort list
        new_list.sort()

        #return sorted list
        return new_list
    else:
        return []

#check_list_is_numeric - checks that a list is both a list and only has ints in it.
def check_list_is_numeric(this_list):

    #valid_list becomes False if list is not valid, if it doesn't become False, list is valid
    valid_list = True

    try:

        #for loop catches ints, floats, and bools as they cannot be enumerated
        for index, number in enumerate(this_list):

            #This attempt to typecast to an int catches strings and strings inside a list
            try:
                this_list[index] = int(this_list[index])
            except ValueError:
                print("Error: Either not a list or non-number inside of list")
                valid_list = False

            #break out of the loop if it's not a valid list
            if not valid_list:
                break

    except TypeError:
        print("Error: Incorrect type. Correct type is list")
        valid_list = False

    return valid_list

#check_list_is_sorted - checks that a list with numeric values is sorted in ascending order
def check_list_is_sorted(this_list):

    #List is sorted until proven otherwise
    is_sorted = True

    #loop through the list
    for index, number in enumerate(this_list):

        #if not looking at first index
        if index != 0:

            #if the current number is less than the last number, the list is not sorted
            if this_list[index - 1] > this_list[index]:
                is_sorted = False

    return is_sorted

#Good test values
listx = merge_and_sort([1, 3, 5, 7], [2, 4, 6, 8])
print(listx)

listx = merge_and_sort([0, 7, 9, 12], [0, 1, 2, 3, 4, 7, 12])
print(listx)

#Bad test values
listx = merge_and_sort("not a list", [2, 4, 6, 8])
print(listx)

listx = merge_and_sort([1, 3, 5, 7], 123)
print(listx)

listx = merge_and_sort([1, "three", 5, 7], [2, 4, 6, 8])
print(listx)

listx = merge_and_sort([1, 3, 5, 7], [2, 4, "six", 8])
print(listx)

listx = merge_and_sort([1, 5, 3, 7], [2, 4, 6, 8])
print(listx)

listx = merge_and_sort([1, 3, 5, 7], [2, 6, 4, 8])
print(listx)

listx = merge_and_sort("hello", 42)
print(listx)

listx = merge_and_sort([1, "a", 5], [2, 4, 3.5])
print(listx)

listx = merge_and_sort([3, 1, 5, 7], [4, 2, 8, 6])
print(listx)