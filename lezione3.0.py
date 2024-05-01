#4-1. Pizzas: Think of at least three kinds of your favorite pizza. 
#Store these pizza names in a list, and then use a for loop to print the name of each pizza.



favourite_pizza = ["margherita", "boscaiola", "marinara"]

for pizza in favourite_pizza:
    print(pizza)

#• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. 
#For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.

for pizza in favourite_pizza:
    print("my favourite pizza is: ", pizza)

#• Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
#The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, 
#such as I really love pizza!

print("I really love pizza ", favourite_pizza[0])
print("I really love pizza ", favourite_pizza[1])
print("I really love pizza ", favourite_pizza[2])



#4-2. 
#Animals: Think of at least three different animals that have a common characteristic. 
#Store the names of these animals in a list, and then use a for loop to print out the name of each animal.

animals = ["bats", "birds", "butterflies"]

for animal in animals:
    print(animal)

    #• Modify your program to print a statement about each animal, such as A dog would make a great pet.

    print(animal, "got wings")

    #• Add a line at the end of your program, stating what these animals have in common. 
    #You could print a sentence, such as Any of these animals would make a great pet!

    print("animals have developed different types of wings, such as ", animal)



#4-3. 
#Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

for i in range(1, 21):
    print(i)



#4-4. 
#One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
#(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

numbers = list(range(1,1000001))
"""
for n in numbers:
    print(n)
"""



#4-5. 
#Summing a Million: Make a list of the numbers from one to one million, 
#and then use min() and max() to make sure your list actually starts at one and ends at one million. 
#Also, use the sum() function to see how quickly Python can add a million numbers.

print(min(numbers))
print(max(numbers))
print(sum(numbers))



#4-6. 
#Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
#Use a for loop to print each number.

odd_numbers = list(range(1, 21, 2))
for odd in odd_numbers:
    print(odd)



#4-7. 
#Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

multiples_of_3 = list(range(3, 31, 3))

for multiple in multiples_of_3:
    print(multiple)



#4-8. 
#Cubes: A number raised to the third power is called a cube. 
#For example, the cube of 2 is written as 2**3 in Python. 
#Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), 
#and use a for loop to print out the value of each cube.


bases = list(range(1, 11))
cubes = []

for base in bases:
    cubes.append(base**3)

print(cubes)



#4-9. 
#Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

cubes = [b**3 for b in range(1, 11)]
print(cubes)




#4-10. 
#Slices: Using one of the programs you wrote in this chapter, 
#add several lines to the end of the program that do the following:

#userò la lista dei multipli di 3
multiples_of_3 = list(range(3, 31, 3))

#• Print the message The first three items in the list are: . 
#Then use a slice to print the first three items from that program’s list.

print("The first three items in the list are: ", multiples_of_3[:3])

#• Print the message Three items from the middle of the list are: . 
#Then use a slice to print three items from the middle of the list.

print("Three items from the middle of the list are: ", multiples_of_3[3:6])

#• Print the message The last three items in the list are: . 
#Then use a slice to print the last three items in the list.

print("The last three items in the list are: ", multiples_of_3[-3:])




#4-11. 
#My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. 
#Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:

friend_pizzas: list = favourite_pizza.copy()

#• Add a new pizza to the original list.

favourite_pizza.append("diavola")

#• Add a different pizza to the list friend_pizzas.

friend_pizzas.append("vegetarana")

#• Prove that you have two separate lists. 
#Print the message My favorite pizzas are: , and then use a for loop to print the first list. 
print("\n")


print("My favorite pizzas are: \n")

for pizza in favourite_pizza: 
    print(pizza)

#Print the message My friend’s favorite pizzas are: , and then use a for loop to print the second list. 
#Make sure each new pizza is stored in the appropriate list.
print("\n")

print("My friend’s favorite pizzas are: \n")

for pizza in friend_pizzas:
    print(pizza)
    


#4-12. 
#More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. 
#Choose a version of foods.py, and write two for loops to print each list of foods.

