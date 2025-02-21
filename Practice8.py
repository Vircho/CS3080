#variables
paragraph_count = 0

#Create the file
essay = open("essay.txt", "w")

#Create the string
paragraphs = '''This essay is concerned with a comparison between the first generation vs. the fifth generation of computers.

The first generation (1946-1959) computers were slow, huge, and expensive. In these computers, vacuum tubes were used as the basic components of CPU and memory.

In the fifth generation (1980-till date) of computers, the VLSI technology was replaced with ULSI (Ultra Large Scale Integration). It made possible the production of microprocessor chips with ten million electronic components.'''

#Write the string to the file
essay.write(paragraphs)

#Begin reading the file line by line
essay.close()
essay = open(r"essay.txt", "r")

lines = essay.readlines()

for line in lines:
    if line != '\n':
        paragraph_count += 1
        print("Paragraph " + str(paragraph_count) + ":")
        print(line)
