#6-1. 
#Person: Use a dictionary to store information about a person you know. 
#Store their first name, last name, age, and the city in which they live. 
#You should have keys such as first_name, last_name, age, and city. 

person1 = {
    "first_name" : "Mario",
    "last_name" : "Rossi",
    "age" : 30,
    "city" : "Roma"
}

#Print each piece of information stored in your dictionary.

print(person1["first_name"])
print(person1["last_name"])
print(person1["age"])
print(person1["city"])



#6-2. 
#Favorite Numbers: Use a dictionary to store people’s favorite numbers. 
#Think of five names, and use them as keys in your dictionary. 
#Think of a favorite number for each person, and store each as a value in your dictionary. 
#For even more fun, poll a few friends and get some actual data for your program.

favourite_numbers = {
    "Francesco" : 15,
    "Tobia" : 32,
    "Vittorio" : 42,
    "Federico" : 28,
    "Leonardo" : 23
}

#Print each person’s name and their favorite number. 

print(favourite_numbers["Federico"])
print(favourite_numbers["Leonardo"])
print(favourite_numbers["Federico"])
print(favourite_numbers["Tobia"])
print(favourite_numbers["Vittorio"])



#6-3. 
#Glossary: A Python dictionary can be used to model an actual dictionary. 
#However, to avoid confusion, let’s call it a glossary.

#• Think of five programming words you’ve learned about in the previous chapters. 
#Use these words as the keys in your glossary, and store their meanings as values.

glossary = {
    "print" : "esegue la stampa di ciò che viene indicato fra parentesi",
    "global" : "fa si che quella determinata variabile sia valida i ogni caso, dentro e fuori dalle funzioni",
    "float" : "indica un numero decimale",
    "set" : "indica un insieme, ovvero una collezione non indicizzata che non ammette duplicati, non è ordinata e non modificabile",
    "elif" : "abbreviazione di else if, aggiunge una condizione da verificare"
}

#• Print each word and its meaning as neatly formatted output. 
#You might print the word followed by a colon and then its meaning, 
#or print the word on one line and then print its meaning indented on a second line. 
#Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

print("print:\n", glossary["print"])
print("global:\n", glossary["global"])
print("float:\n", glossary["float"])
print("set:\n", glossary["set"])
print("elif:\n", glossary["elif"])



#6-7. 
#People: Start with the program you wrote for Exercise 6-1. 
#Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 

person2 = {
    "first_name" : "Gabriele",
    "last_name" : "Ricci",
    "age" : 20,
    "city" : "Firenze"
}


person3 = {
    "first_name" : "Mattia",
    "last_name" : "Colombo",
    "age" : 40,
    "city" : "Bologna"
}

people = [person1, person2, person3]

#Loop through your list of people. As you loop through the list, print everything you know about each person.

for person in people:
    print("First Name:", person["first_name"])
    print("Last Name:", person["last_name"])
    print("Age:", person["age"])
    print("City:", person["city"])
    