#!/bin/python3

#Print string
print("Strings and things:")
print('Hello World!')
print("""Hello, this is a 
multi-line string!""")
print("This is"+" a string")

print('\n') #new line

#Maths
print("Math:")
print(50 + 50)
print(50 - 50)
print(50 * 50)
print(50 / 50)
print(50 ** 2) #exponents
print(50 % 50)
print(50 // 6) #number without leftovers

print('\n') # new line

#Variables and Methods
print("Fun with variables and methods")
quote = "All is fair in love and war"
print(len(quote)) #length
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title Capitalize every word

name = "Jordan"
age = 80
gpa = 2.5

print(int(age))
print(int(80.9)) #rounds down

print("My name is " + name + " and I am " + str(age) + " years old.")

print('\n')

age += 1
print(age)

birthday = 1
age += birthday
print(age)

print("\n")

#Functions
print("Now, some functions")
def who_am_i():
	name = "Jordan"
	age = 80
	print("My name is " + name + " and I am " + str(age) + " years old.")
who_am_i()

#adding in parameters
def add_one_hundred(num):
	print(num + 100)

add_one_hundred(100)

#add in multiple parameters
def add(x,y):
	print(x + y)
add(7,7)
add(305, 207)

#using return
def multiply(x,y):
	return x * y

print(multiply(7,7))

def square_root(x):
	return x ** 0.5

print(square_root(64))

print("\n")

#Boolean expressions (True or False)
print("Boolean expressions")
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1))

greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 5 <= 5

print(greater_than, less_than, greater_than_equal_to, less_than_equal_to)

test_and = (7 > 5) and (5 < 7)
test_or = (7 > 5) or (5 < 7)
test_not = not True

print(test_and)

def soda(money):
	if money >= 2:
		return "You've got yourself a soda!"
	else:
		return "No soda for you!"
print(soda(3))
print(soda(1))

def alcohol(age, money):
	if (age >= 21) and (money >= 5):
		return "We're gettin tipsy!"
	elif (age >= 21) and (money < 5):
		return "Come back with more money."
	elif (age < 21) and (money >= 5):
		return "Nice try, kid"
	else:
		return "You didn't bring money and you're too young"

print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))

print('\n')

#Lists
print("Lists have brackets")
movies = ["TENET", "Avengers Endgame", "Imitation Game", "Mr. Robot"]

print(movies[0])
print(movies[0:3]) #prints items 0 to 2
print(movies[1:]) #prints item 1 to the end
print(movies[:1]) #prints item 0
print(movies[-1]) #prints last item of list
print(len(movies)) #length of list

movies.append("JAWS")
print(movies)

movies.pop() # deletes last item
print(movies)

movies.pop(1) # deletes second item
print(movies)

movies = ["TENET", "Avengers Endgame", "Imitation Game", "Mr. Robot"]
person = ["Jordan", "Beomus", "Scarlet", "White Rose"]
combined = zip(movies, person)
print(list(combined))

#Tuples
print("Tuples have parentheses and cannot change")
grades = ("A", "B", "C", "D", "F") # uses parentheses
print(grades[1]) #prints B
# Tuples are static; cannot append() or pop()

#Looping
print("For loops - start to finish of iterate:")
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
	print(x)

print("While loops - Execute as long as True:")
i = 1
while i < 10:
	print(i)
	i += 1





