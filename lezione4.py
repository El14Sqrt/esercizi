#8-1. 
#Message: Write a function called display_message() 
#that prints one sentence telling everyone what you are learning about in this chapter. 
#Call the function, and make sure the message displays correctly.

def display_message():
    print("In this chapter I'm learning functions.")

display_message()



#8-2. 
#Favorite Book: Write a function called favorite_book() that accepts one parameter, title. 
#The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
#Call the function, making sure to include a book title as an argument in the function call.

def favorite_book(title)
    print("One of my favorite books is ", title)

favorite_book("Ventimila leghe sotto i mari")



#8-3. 
#T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message 
#that should be printed on the shirt. 
#The function should print a sentence summarizing the size of the shirt and the message printed on it. 
#Call the function once using positional arguments to make a shirt. 
#Call the function a second time using keyword arguments.

def make_shirt(size, message):
    print("You've ordered a", size, "with written on it:", message)

make_shirt("medium", "Good Weekend!")

make_shirt(size="large", message="I like snakes")



#