#Create a program that returns a user's watchlist, every time the user continues, give them the next film

#Class WatchList - represents a watchlist containing movies the user wants to watch
class WatchList:

    #__init__ - creates an empty watchlist upon object creation
    def __init__(self):
        self.list = []
        self.at = 0
        self.stop = 0

    #__add__ - adds a string representing movie name to the watchlist
    def __add__(self, to_add):
        self.list.append(to_add)
        self.stop += 1

    #__iter__ - returns the iterator object
    def __iter__(self):
        return self

    #__next__ - returns the next film in user watchlist
    def __next__(self):
        if self.at < self.stop:
            next_value = self.list[self.at]
            self.at += 1
            return next_value
        else:
            raise StopIteration

#Add films
my_watchlist = WatchList()
my_watchlist.__add__("Barbie")
my_watchlist.__add__("Parasite")
my_watchlist.__add__("Interstellar")
my_watchlist.__add__("Fight Club")
my_watchlist.__add__("La La Land")

#Allow the user to get their watchlist films one by one
while True:
    input("Enter for the next film.")

    try:
        print(my_watchlist.__next__())
    except StopIteration:
        print("That's all the films on your watchlist!")
        break