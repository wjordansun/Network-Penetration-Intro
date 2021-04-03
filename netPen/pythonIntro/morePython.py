#!/bin/python3

#Importing
print("Importing is important:")

import sys #system functions and parameters

from datetime import datetime
print(datetime.now())

from datetime import datetime as dt #importing with an alias
print(dt.now())

def new_line():
	print('\n')

new_line()

#Advanced Strings
print("Advanced strings:")
my_name = "Jordan"
print(my_name[0]) #first letter
print(my_name[-1]) #last letter

sentence = "This is a sentence."

print(sentence[:4]) #first word
print(sentence[-9:-1]) #last word

print(sentence.split()) #split sentence by delimiter (space)

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join) # This is a sentence
print('\n'.join(sentence_split))

quoteception = "I said, 'give me the knowledge'"
print(quoteception)

quoteception = "I said, \"give me the knowwledge\""
print(quoteception)

print("A" in "Apple") # returns True

letter = "a"
word = "Apple"
print(letter.lower() in word.lower()) # case insensitive

word_two = "Bingo"
print(letter.lower() in word.lower() and not (letter.lower() in word_two.lower()))

too_much_space = "      hello      "
print(too_much_space.strip()) #gets rid of space by default

full_name = "ordan Sun"
print(full_name.replace("ordan", "Jordan"))
print(full_name.find("Sun"))

movie = "Tenet"
print("my favorite movie is {}.".format(movie))

def favorite_book(title, author):
	fav = "My favorite book is \"{}\", which is written by {}.".format(title, author) #place holder
	return fav

print(favorite_book("The Prince of Milk", "Exurb1a"))

#Dictionaries
print("Dictionaries are keys and values:")
drinks = {"Sprite": 7, "Cococola": 8, "Aloe": 15, "Tea": 10 }
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR":
 ["Jimmy Jr.", "Mort"]}
print(employees)

employees['Legal'] = ["Mr. Frond"] #add new key: value pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]})
print(employees)

drinks['Sprite'] = 6
print(drinks)

print(drinks.get("Sprite"))
print(drinks["Sprite"])

#Lists and dictionaries
movies = ["TENET", "Avengers Endgame", "Imitation Game", "Mr. Robot"]
person = ["Jordan", "Beomus", "Scarlet", "White Rose"]
combined = zip(movies, person)
movie_dictionary = {key: value for key, value in combined}
print(movie_dictionary)







