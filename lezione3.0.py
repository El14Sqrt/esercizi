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



