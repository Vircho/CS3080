#Get the top-secret password
password = ''
while password != 'scuba':
    password = input("Enter the top-secret password: ")
    if password != 'scuba':
        print('That is not the top-secret password, try again')
    else:
        print('You can come into the party')

#Print in sequence
for i in range(1, 11, 1):
    print(i)
for i in range(-5, 6, 1):
    print(i)
for i in range(15, 36, 4):
    print(i)
for i in range(35, -16, -5):
    print(i)

#Entering negative and non-negative numbers
num = -1
while num < 0:
    num = int(input('Enter a non-negative number: '))
    if num < 0:
        print('You have not entered a non-negative number')
    else:
        print('good job')