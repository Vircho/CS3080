int1 = input('Please enter an int')             #Set var int1 to user input
int2 = input('Please enter another int')        #Set var int2 to user input
int_sum = int(int1) + int(int2)                 #Calculate sum and typecast
print(int1 + ' + ' + int2 + ' = ' + str(int_sum))   #Print the calculated sum using print

minutes = input('Enter an amount of minutes')   #Set var minutes to user input
hours = int(minutes) // 60                      #Int divide minutes by 60 to get num of hours
remaining = int(minutes) % 60                   #Find remainder after dividing by 60 to get num of minutes
print(str(hours) + ' hours and ' + str(remaining) + ' minutes.') #Print by typecasting ints to strings