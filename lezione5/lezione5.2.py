#9-13. 
#Dice: Make a class Dice with one attribute called sides, which has a default value of 6. 
#Write a method called roll_dice() that prints a random number between 1 and the number of sides the dice has. 
#Make a 6-sided dice and roll it 10 times. Make a 10-sided dice and a 20-sided dice. Roll each dice 10 times.
import random

class Dice:
    def __init__(self, sides:int=6) -> None:
        self.sides=sides
        
    def roll_dice(self, times:int):
        self.times=times

        for time in range(self.times):
            print(random.randint(1, self.sides))


first_dice = Dice(sides=6)
second_dice = Dice(sides=10)
third_dice = Dice(sides=20)

first_dice.roll_dice(10)
second_dice.roll_dice(10)
third_dice.roll_dice(10)


print("\n")



#9-14. 
#Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. 
#Randomly select 4 numbers or letters from the list and print a message saying 
#that any ticket matching these 4 numbers or letters wins a prize.

alphanumeric_list: list = [5, 8, "c", 6, "o", "l", 9, 7, 44, 52, "z", "y", 41, 22, 77]

random_items: list = random.sample(alphanumeric_list, 4)        #Genera una lista costruita con n elementi casuali della struttura dati z. Senza reinserimento. n ≤ len(z)
print("any ticket matching these 4 items wins a prize: ", random_items)


#9-15. 
#Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. 
#Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. 
#Print a message reporting how many times the loop had to run to give you a winning ticket.