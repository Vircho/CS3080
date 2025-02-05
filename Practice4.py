#Create list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nonprime_found = False

#Check if all elements are prime
for element in numbers:                     #Loop through elements
    for check in range(2, (element - 1)):   #Loop through numbers from 2 -> element - 1
        if element % check == 0:            #If it can be divided cleanly by one of them
            nonprime_found = True           #It's a nonprime

print(f'{numbers} -> {not nonprime_found}')     #print the list, and then weather it has a prime or not