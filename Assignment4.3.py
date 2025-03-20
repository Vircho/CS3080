#Assignment4.3
#Author: Joshua White
#Due: 3/3/25
#Uses a class to represent a virtual bank account

#imports
import random #Random number generation
import sys #Used for int limit

#Account - represents a single bank account
class Account:

    #__init__ - initializes each instance of class
    def __init__(self):
        #Generate a random 8-digit number to act as account number
        #and set initial balance to $0
        self.account_number = random.randint(10000000, 99999999)
        self.balance = float(0)

    #deposit - adds to object's balance amount
    def deposit(self, amount):
        self.balance += amount
        print(f"${deposit_amount} successfully deposited.")

    #withdraw - subtracts from object's balance amount if balance is enough
    def withdraw(self, amount):

        if amount > self.balance:
            print(f"You do not have enough balance to withdraw ${amount}.")
            print(f"You currently have ${self.balance} in your account.")
        else:
            self.balance -= amount
            print(f"${withdraw_amount} successfully withdrawn")

    #__str__ - returns account information
    def __str__(self):
        print(f'''-ACCOUNT INFORMATION-
        ACCOUNT NUMBER: {self.account_number}
        ACCOUNT BALANCE: ${self.balance}
        ===========================''')

#print_accounts - prints a list of bank accounts
def print_accounts(accounts_list):

    cur_acc = 0 #The current account being printed

    #Top of list, with -1 acting as option to create account
    print('''==Current Accounts===''')
    print("-2: Terminate program")
    print("-1: Create new account")

    #Loop through list of accounts and print them
    for account in accounts_list:
        print(f"{cur_acc}: {account.account_number}")
        cur_acc += 1

#check_list_empty - Returns a boolean representing if a list has no elements or not
def check_list_empty(this_list):

    try:
        if this_list[0] == 'x':
            pass
    except IndexError:
        return True
    return False

#get_int - gets an integer from the user. Gets passed a message string to give when getting input,
#and a minimum/maximum int (inclusive)
def get_int(message, min_int, max_int):

    #Assume input is not int until proven otherwise
    is_int = False
    user_int = 0

    #Loop until given an int
    while not is_int:

        #Take in input
        user_input = input(f"{message}")

        #Test for int
        try:
            user_int = int(user_input)
        except ValueError:
            print("You have not inputted an integer. Try again.")
        else:
            is_int = True

        #Test for within range
        if is_int:
            if user_int < min_int or user_int > max_int:
                print(f"Number is outside of range {min_int} - {max_int}. Try again.")
                is_int = False

    return user_int

#get_float - gets a float from the user. Gets passed a message string to give when getting input,
#and a minimum/maximum float (inclusive)
def get_float(message, min_float, max_float):

    #Assume input is not a float until proven otherwise
    is_float = False
    user_float = 0

    #Loop until given a valid float
    while not is_float:

        #Take in input
        user_input = input(f"{message}")

        #Test for float
        try:
            user_float = float(user_input)
        except ValueError:
            print("You have not inputted a number. Try again.")
        else:
            is_float = True

        #Test for within range
        if is_float:
            if user_float < min_float or user_float > max_float:
                print(f"Number is outside of range {min_float} - {max_float}. Try again.")
                is_float = False

    return user_float


#Variables
program_running = True #When false, program terminates
accounts = [] #Keeps all accounts made

#Runs until program terminated by user
while program_running:

    #Create account for user if it has not yet created an account (accounts list is empty)
    if check_list_empty(accounts):
        print("Welcome to the bank account simulation!")
        print("Seems you have no bank accounts, I'll go ahead and make one for you...")
        accounts.append(Account())
        print("Done! Your bank account has been made. Please continue on to the simulation.")
    else:

        #Prints list of accounts, get user input to decide an account to use or other actions relating to the program
        #Such as creating a new account or terminating the program
        print_accounts(accounts)
        user_choice_account = get_int("Enter a number to perform actions with that account: ", -2, len(accounts) - 1)

        #Create a new account if the user chooses to create one
        if user_choice_account == -1:
            accounts.append(Account())
            print("Account created!")

        #Break out of the while loop if the user terminates the program
        elif user_choice_account == -2:
            program_running = False

        else:

            #Present options for actions
            print(f'''Account: {accounts[user_choice_account].account_number}
                1: Deposit
                2. Withdraw
                3. Print information''')
            user_choice_action = get_int("Choose a number to decide what to do with this account: ", 1, 3)

            #Deposit into account
            if user_choice_action == 1:
                deposit_amount = get_float("How much would you like to deposit? ", 0, sys.maxsize)
                accounts[user_choice_account].deposit(deposit_amount)

            #Withdraw from account
            elif user_choice_action == 2:
                withdraw_amount = get_float("How much would you like to withdraw? ", 0, sys.maxsize)
                accounts[user_choice_account].withdraw(withdraw_amount)

            #Print account information
            elif user_choice_action == 3:
                accounts[user_choice_account].__str__()