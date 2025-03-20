#Assignment 4.4
#Author: Joshua White
#Due: 3/3/25
#Creates a file with incorrect information and edits the file to fix it

#common_mistakes - Fills a dictionary with writing errors and the corrections for them
def common_mistakes(dictionary):

    dictionary['3'] = '2'
    dictionary['20'] = '11'
    dictionary['hands'] = 'feet'
    dictionary['an'] = 'a'
    dictionary['ellipse'] = 'rectangular'
    dictionary['square'] = 'rectangular'
    dictionary['50'] = '45'
    dictionary['100'] = '90'

#Variables
    #To be written to file
paragraph = '''The soccer game is a team sport played between 3 teams of 20
players each, who almost exclusively use their hands to propel
a ball around an ellipse field. The objective of the game is to
score more goals than the opposing team by moving the ball
beyond the goal line into a square framed goal defended by the
opposing team. Traditionally, the game has been played over
two 50 minute halves, for a total match time of 100 minutes.'''
    #File
article = open("article.txt", 'w')

#Write to the file
article.write(paragraph)

#Create dictionary with the mistakes (Key:Value = Mistake:Correction)
mistakes = dict()
common_mistakes(mistakes)

#Open the file for reading and writing
article.close()
article = open("article.txt", "r")

#Set up needed variables before the loop
    #String that will be used to overwrite the file
new_paragraph = ''
    #Is current word a mistake
there_is_mistake = False

#Loop through each line
for line in article.readlines():

    #Split the string
    words = line.split()

    #Loop through each word
    for word in words:

        #For each word, compare it to each key
        for key in mistakes.keys():

            #If word matches key
            if key == word:

                #There is a mistake
                there_is_mistake = True

        #If this word is a mistake
        if there_is_mistake:

            #Add the corrected word to new paragraph
            new_paragraph += mistakes[word]

        #Otherwise add the word itself, as it's fine
        else:
            new_paragraph += word

        #Append a space to the paragraph, and reset the boolean
        new_paragraph += ' '
        there_is_mistake = False

    #Append a newline after each line
    new_paragraph += '\n'

#Write over the file with the new paragraph
article.close()
article = open("article.txt", "w")
article.write(new_paragraph)