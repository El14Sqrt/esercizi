#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. 
#Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

name: str = "Mario"

message: str = f"Ciao {name}, ti va di imparare un po di python oggi?"

print(message)

#2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, 
#uppercase, and title case.

name: str = "Luigi"

print(f"{name}, {name.upper()}, {name.lower()}") 

#oppure creo due nuove variabili a cui assegnare i due nuovi valori, questo semplifica la lettura e il dubugging

#2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
#Your output should look something like the following, including the quotation marks: 
#Albert Einstein once said, “A person who never made a mistake never tried anything new.”

author: str = "Oscar Wilde"

quote: str = "L'uomo è poco se stesso quando parla in prima persona. Dategli una maschera e vi dirà la verità."

print(f"{author} una volta ha detto: {quote}") 

#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. 
#Then compose your message and represent it with a new variable called message. Print your message. 

famous_person: str = "Oscar Wilde"

message: str = f"{famous_person} una volta ha detto: L'uomo è poco se stesso quando parla in prima persona. Dategli una maschera e vi dirà la verità."

print(message)

