#ESERCIZIO 1:

#1. Copy the code and print the age of bob (using the dot notation)
#2. Create an if-statement that prints the name of the oldest of the two Persons
#3. Create three other Persons. Make a list called people with all 5 Persons.
#4. Make a loop that finds and prints the youngest person’s name

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

print(f"età di Bob: {bob.age}")

if alice.age >= bob.age:
    print(f"the oldest person is {alice.name}")
else:
    print(f"the oldest person is {bob.name}")

leo = Person("Leo B.", 21)
andrea = Person("Andrea L.", 33)
matteo = Person("Matteo C.", 48)

People: list = [alice, bob, leo, andrea, matteo]

#vedere serie di screenshot

#ESERCIZIO 2:

#1. Write a class called Student with the attributes name (str) and studyProgram (str)
#2. Create three instances. One for yourself, one for your left neighbour and one for our right neighbour.
#3. Add a method printInfo that prints the name and studyProgram of a Student. Test your method on the objects!
#4. Modify the code and add age and gender to the attributes. Modify your printing methods respectively too.

class Sudent:
    def __init__(self, name: str, studyProgram: str):
        self.name = name
        self.studyProgram = studyProgram
    
    #vedere foto e appunti

#ESERCIZIO 3:

#Given is the class Animal. For each task, test your changes!
#1. Create two realistic instances of Animals
#2. Print the name of each object
#3. Change the amount of legs of one object using the dot notation
#4. Add a method setLegs() to set the legs of an object and repeat task 3 but this time using the method.
#5. Add a method getLegs() to return the amount of legs
#6. Add a method named printInfo that prints all attributes of the Animal

class Animal:
    def __init__(self, name:str, species: str, legs: int = 0):
        self.name = name
        self.species = species
        self.legs = legs

    def set_legs(self, new_leg):

animal_1 = Animal("cat", 4)
animal_2 = Animal("dog", 4)

print(f"il primo animale è: {animal_1.name}", f"il secondo animale è: {animal_2.name}")

#ESERCIZIO 4:

#1. Write a new class called Food, it should have name, price and description as attributes.
#2. Instantiate at least three different foods you know and like.
#3. Create a new class called Menu, it should have a list (of Foods) as attribute.
#   __init__ should take a list of Foods as optional parameters (default=[])
#4. Create a addFood() and removeFood() for the Menu
#5. Create a few new Food instances. Add each to the Menu using the respective Method.
#6. Add a method printPrices() that list all items on the Menu with their prices.
#7. Add a Menu method getAveragePrice() that returns the average Food price of the Menu

class Food:
    def __init__(self, name:str, price:int, description:str):
        self.name = name
        self.price = price
        self.description = description

carbonara = Food("Carbonara", 10, "pasta con uova, guanciale, pepe, pecorino")
tiramisu = Food("Tiramisù", 5, "dolce con caffè, savoiardi e mascarpone")
cotoletta = Food("Cotoletta", 8, "carne impanata")

class Menu:
