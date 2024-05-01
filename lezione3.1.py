#5-1. Conditional Tests: Write a series of conditional tests. 
#Print a statement describing each test and your prediction for the results of each test. 
#Your code should look something like this:

"""
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
"""

#• Look closely at your results, and make sure you understand why each line evaluates to True or False.

#• Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.

vegetable = "pepper"
fruit = "mango"

print("\nIs vegetable == 'tomato' ? I predict False.")
print(vegetable == 'tomato')

print("\nIs vegetable == 'pepper' ? I predict True.")
print(vegetable == 'pepper')

print("\nIs fruit == 'lemon' ? I predict False.")
print(fruit == 'lemon')

print("\nIs fruit == 'mango' ? I predict True.")
print(fruit == 'mango')

print("\nIs vegetable == 'asparagus' ? I predict False.")
print(vegetable == 'asparagus')

print("\nIs vegetable == 'onion' ? I predict False.")
print(vegetable == 'onion')

print("\nIs fruit == 'kiwi' ? I predict False.")
print(fruit == 'kiwi')

print("\nIs fruit == 'papaya' ? I predict False.")
print(fruit == 'papaya')



#5-2. 
#More Conditional Tests: You don’t have to limit the number of tests you create to 10. 
#If you want to try more comparisons, write more tests and add them to conditional_tests.py. 
#Have at least one True and one False result for each of the following:

#• Tests for equality and inequality with strings

#• Tests using the lower() method

#• Numerical tests involving equality and inequality, greater than and less than, 
#greater than or equal to, and less than or equal to

#• Tests using the and keyword and the or keyword

#• Test whether an item is in a list

#• Test whether an item is not in a list


"NON HO CAPITO CHE DEVO FARE!!!"


#5-3. 
#Alien Colors #1: Imagine an alien was just shot down in a game. 
#Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

#• Write an if statement to test whether the alien’s color is green. 
#If it is, print a message that the player just earned 5 points.

#• Write one version of this program that passes the if test and another that fails. 
#(The version that fails will have no output.)

alien_color = "rosso"
points: int = 0

if alien_color == "verde":
    points += 5
    print("Il giocatore ha appena guadagnato 5 punti")

elif alien_color == "giallo":
    points += 5
    print("Il giocatore ha appena guadagnato 5 punti")

elif alien_color == "rosso":
    points += 5
    print("Il giocatore ha appena guadagnato 5 punti")


alien_color = "blu"
points: int = 0

if alien_color == "verde":
    points += 5
    print("Il giocatore ha appena guadagnato 5 punti")

elif alien_color == "giallo":
    points += 5
    print("Il giocatore ha appena guadagnato 5 punti")

elif alien_color == "rosso":
    points += 5
    print("Il giocatore ha appena guadagnato 5 punti")



#5-4. 
#Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

#• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.

#• If the alien’s color isn’t green, print a statement that the player just earned 10 points.

#• Write one version of this program that runs the if block and another that runs the else block.

alien_color = "green"
points: int = 0

if alien_color == "green":
    points += 5
    print("You just earned 5 point for shooting the alien!")
else:
    points += 10
    print("You just earned 10 points!")

alien_color = "yellow"
points: int = 0

if alien_color == "green":
    points += 5
    print("You just earned 5 point for shooting the alien!")
else:
    points += 10
    print("You just earned 10 points!")

