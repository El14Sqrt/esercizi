#2-3. 
#Personal Message: Use a variable to represent a person’s name, and print a message to that person. 
#Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

name: str = "Mario"

message: str = f"Ciao {name}, ti va di imparare un po di python oggi?"

print(message)



#2-4. 
#Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, 
#uppercase, and title case.

name: str = "Luigi"

print(f"{name}, {name.upper()}, {name.lower()}") 

    #oppure creo due nuove variabili a cui assegnare i due nuovi valori, questo semplifica la lettura e il dubugging



#2-5. 
#Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
#Your output should look something like the following, including the quotation marks: 
#Albert Einstein once said, “A person who never made a mistake never tried anything new.”

author: str = "Oscar Wilde"

quote: str = "L'uomo è poco se stesso quando parla in prima persona. Dategli una maschera e vi dirà la verità."

print(f"{author} una volta ha detto: {quote}") 



#2-6. 
#Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. 
#Then compose your message and represent it with a new variable called message. Print your message. 

famous_person: str = "Oscar Wilde"

message: str = f"{famous_person} una volta ha detto: L'uomo è poco se stesso quando parla in prima persona. Dategli una maschera e vi dirà la verità."

print(message)



#2-8. 
#File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
#Assign the value 'python_notes.txt' to a variable called filename. 
#Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

filename = "python_notes.txt"

filename_without_extension = filename.removesuffix(".txt")

print(filename_without_extension)



#3-1. 
#Names: Store the names of a few of your friends in a list called names. 
#Print each person’s name by accessing each element in the list, one at a time.

names: list = ["Nicolò", "Marla", "Simone"]

print(names[0])
print(names[1])
print(names[2])



#3-2. 
#Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. 
#The text of each message should be the same, but each message should be personalized with the person’s name.

print(f"{names[0]} dove andiamo a skaetare oggi?")
print(f"{names[1]} dove andiamo a skaetare oggi?")
print(f"{names[2]} dove andiamo a skaetare oggi?")



#3-3. 
#Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, 
#and make a list that stores several examples. Use your list to print a series of statements about these items, 
#such as “I would like to own a Honda motorcycle.”

car: list = ["KTM", "Honda", "Yamaha", "Ducati"]

print(f"I would like to own a {car[0]} motorcycle.")
print(f"I would like to own a {car[1]} motorcycle.")
print(f"I would like to own a {car[2]} motorcycle.")
print(f"I would like to own a {car[3]} motorcycle.")



#3-4. 
#Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
#Make a list that includes at least three people you’d like to invite to dinner. 
#Then use your list to print a message to each person, inviting them to dinner.

invited = ["Michael Schumacher", "Lewis Hamilton", "Charles Leclerc"]

print(f"Ciao {invited[0]}, sei invitato a cena domani sera!")
print(f"Ciao {invited[1]}, sei invitato a cena domani sera!")
print(f"Ciao {invited[2]}, sei invitato a cena domani sera!")



#3-5. 
#Changing Guest List: You just heard that one of your guests can’t make the dinner, 
#so you need to send out a new set of invitations. 
#You’ll have to think of someone else to invite.

#• Start with your program from Exercise 3-4. Add a print() call at the end of your program, 
#stating the name of the guest who can’t make it.

print(f"{invited[1]} non può venire alla cena")

#• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

invited[1] = ("Sebastian Vettel")
print(invited)

#• Print a second set of invitation messages, one for each person who is still in your list.

print(f"Ciao {invited[0]}, sei invitato a cena domani sera!")
print(f"Ciao {invited[1]}, sei invitato a cena domani sera!")
print(f"Ciao {invited[2]}, sei invitato a cena domani sera!")



#3-6. 
#More Guests: You just found a bigger dinner table, so now more space is available. `
#Think of three more guests to invite to dinner.

#• Start with your program from Exercise 3-4 or 3-5. 
#Add a print() call to the end of your program, informing people that you found a bigger table.

print(f"Ciao {invited[0]}! Ho più posto a tavola del previsto, inviterò altre persone e volevo informarti.")
print(f"Ciao {invited[1]}! Ho più posto a tavola del previsto, inviterò altre persone e volevo informarti.")
print(f"Ciao {invited[2]}! Ho più posto a tavola del previsto, inviterò altre persone e volevo informarti.")

#• Use insert() to add one new guest to the beginning of your list.

invited.insert (0, "Fernando Alonso")

#• Use insert() to add one new guest to the middle of your list.

invited.insert (2, "Niki Lauda")

#• Use append() to add one new guest to the end of your list.

invited.append ("Ayrton Senna")

print(invited)

invited_length = len(invited)   #necessary for exercise 3-9

#• Print a new set of invitation messages, one for each person in your list.

print(f"Ciao {invited[0]}, sei invitato a cena domani sera!")
print(f"Ciao {invited[1]}, sei invitato a cena domani sera!")
print(f"Ciao {invited[2]}, sei invitato a cena domani sera!")
print(f"Ciao {invited[3]}, sei invitato a cena domani sera!")
print(f"Ciao {invited[4]}, sei invitato a cena domani sera!")
print(f"Ciao {invited[5]}, sei invitato a cena domani sera!")



#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, 
#and now you have space for only two guests.

#• Start with your program from Exercise 3-6. 
#Add a new line that prints a message saying that you can invite only two people for dinner.

message = "Imprevisto: posso invitare solo due persone!!"
print(message)

#• Use pop() to remove guests from your list one at a time until only two names remain in your list. 
#Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

print(f"sono molto dispiaciuto {invited[0]} ma ceneremo insieme un'altra volta.")
invited.pop(0)
print(f"sono molto dispiaciuto {invited[0]} ma ceneremo insieme un'altra volta.")
invited.pop(0)
print(f"sono molto dispiaciuto {invited[0]} ma ceneremo insieme un'altra volta.")
invited.pop(0)
print(f"sono molto dispiaciuto {invited[0]} ma ceneremo insieme un'altra volta.")
invited.pop(0)

#• Print a message to each of the two people still on your list, letting them know they’re still invited.

print(f"Ciao {invited[0]}, ci vediamo a cena!")
print(f"Ciao {invited[1]}, ci vediamo a cena!")

#• Use del to remove the last two names from your list, so you have an empty list. 
#Print your list to make sure you actually have an empty list at the end of your program. 

del invited[1]
del invited[0]
print(invited)



#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.

#• Store the locations in a list. Make sure the list is not in alphabetical order.

locations: list = ["New York", "Madagascar", "Tokyo", "Austrailia", "California"]

#• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.

print(locations)

#• Use sorted() to print your list in alphabetical order without modifying the actual list.

alphabetical_locations = sorted(locations)
print(alphabetical_locations)

#• Show that your list is still in its original order by printing it.

print(locations)

#• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.

reverse_alphabetical_locations = sorted(locations, reverse = True)
print(reverse_alphabetical_locations)

#• Show that your list is still in its original order by printing it again.

print(locations)

#• Use reverse()  to change the order of your list. Print the list to show that its order has changed.

locations.reverse()
print(locations)

#• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

locations.reverse()
print(locations)

#• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

locations.sort()
print(locations)

#• Use sort() to change your list so it’s stored in reverse-alphabetical order.
#Print the list to show that its order has changed.

locations.sort(reverse = True)
print(locations)



#3-9. 
#Dinner Guests: Working with one of the programs from Exercises 3, 
#use len() to print a message indicating the number of people you’re inviting to dinner.

print(invited_length) #variabile creata nell'esercizio 3-6 usando len()



#3-10. 
#Every Function: Think of things you could store in a list. 
#For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
#Write a program that creates a list containing these items and then 
#uses each function introduced in this chapter at least once. 

