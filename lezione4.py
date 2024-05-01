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

def favorite_book(title):
    print("One of my favorite books is ", title)

favorite_book("'Ventimila leghe sotto i mari'")



#8-3. 
#T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message 
#that should be printed on the shirt. 
#The function should print a sentence summarizing the size of the shirt and the message printed on it. 

def make_shirt(size, message):
    print("You've ordered a", size, "with written on it:", message)

#Call the function once using positional arguments to make a shirt. 

make_shirt("medium", "Good Weekend!")

#Call the function a second time using keyword arguments.

make_shirt(size="large", message="I like snakes")



#8-4. 
#Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message 
#that reads I love Python. 
#Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size="large", message="I love Python"):
    print("You've ordered a", size, "with written on it:", message)
make_shirt()
make_shirt(size="medium")

make_shirt(size="small", message="I'm learning Python")



#8-5. 
#Cities: Write a function called describe_city() that accepts the name of a city and its country. 
#The function should print a simple sentence, such as Reykjavik is in Iceland. 
#Give the parameter for the country a default value. 

def describe_city(city_name, country_name = "Italy"):
    print(city_name + " is in " + country_name)

#Call your function for three different cities, at least one of which is not in the default country.

describe_city("Rome")
describe_city("Naples")
describe_city("London", "UK")



#8-6. 
#City Names: Write a function called city_country() that takes in the name of a city and its country. 
#The function should return a string formatted like this: "Santiago, Chile". 

def city_country(city, country):
    return city + ", " + country

#Call your function with at least three city-country pairs, and print the values that are returned.

print(city_country("Madrid", "Spain"))
print(city_country("Tokyo", "Japan"))
print(city_country("Paris", "France"))
print(city_country("Berlin", "Germany"))



#