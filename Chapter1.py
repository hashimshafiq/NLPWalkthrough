from nltk.book import *  

print("Try using the Python interpreter as a calculator, and typing expressions like 12 / (4 + 1).")
print(12/(4+1))


print("Given an alphabet of 26 letters, there are 26 to the power 10, or 26 ** 10, ten-letter strings we can form. That works out to 141167095653376. How many hundred-letter strings are possible?")
print(26**100)

print("The Python multiplication operation can be applied to lists. What happens when you type ['Monty', 'Python'] * 20, or 3 * sent1?")
sent1 = ['Monty','Python']
print(sent1*20)
print(3*sent1)

print("How many words are there in text2? How many distinct words are there?")
print(len(text2))
print(len(set(text2)))

print("Compare the lexical diversity scores for humor and romance fiction in 1.1. Which genre is more lexically diverse?")
#Moby Dick by Herman Melville genre adventure 1851
#Sense and Sensibility by Jane Austen genre romance 1811 text2
#Monty Python and the Holy Grail genre comedy text6
#The Man Who Was Thursday by G . K . Chesterton genre thriller 1908
print(100 * len(set(text2))/len(text2))
print(100 * len(set(text6))/len(text6))

print("Produce a dispersion plot of the four main protagonists in Sense and Sensibility: Elinor, Marianne, Edward, and Willoughby. What can you observe about the different roles played by the males and females in this novel? Can you identify the couples?")
text2.dispersion_plot(["Elinor", "Marianne", "Edward", "Willoughby"])

print("Find the collocations in text5.")
text5.collocations()


print("Consider the following Python expression: len(set(text4)). State the purpose of this expression. Describe the two steps involved in performing this computation.")
print("It gets the vocabulary for the text4 and then return its len")

print("Question 9A")
my_string = 'My String'
my_string
print(my_string)


print("Question 9B")
print(my_string + my_string)
print(my_string*3)


print("Question 10A")
my_sent = ["My", "sent"]
print(' '.join(my_sent))
print(' '.join(my_sent).split())


print("Questin 11")
phrase1 = "hello"
phrase2 = "World"
print((len(phrase1+phrase2)))
print(len(phrase1)+len(phrase2))

print("Question 12")
print("Both are relevant but 2nd one is more suitable as it index the whole word")


