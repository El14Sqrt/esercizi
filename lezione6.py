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

#vedere seriedi screenshot

