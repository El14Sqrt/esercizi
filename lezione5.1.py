#ESERCIZI LEZIONE 5

#9-1. 
#Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: 
#a restaurant_name and a cuisine_type. 
#Make a method called describe_restaurant() that prints these two pieces of information, 
#and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
#Make an instance called restaurant from your class. 
#Print the two attributes individually, and then call both methods.

class Restaurant:
    def __init__(self, restaurant_name:str, cuisine_type:str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant(name: {self.restaurant_name}, cuisine: {self.cuisine_type})")
    
    def open_restaurant(self):
        print(f"Il ristorante {self.restaurant_name} è aperto.")

r1 = Restaurant(restaurant_name="La vecchia Roma", cuisine_type="romana")

r1.describe_restaurant()
r1.open_restaurant()

#9-2. 
#Three Restaurants: Start with your class from Exercise 9-1. 
#Create three different instances from the class, and call describe_restaurant() for each instance.

r2 = Restaurant(restaurant_name="", cuisine_type="")
r3 = Restaurant(restaurant_name="", cuisine_type="")
r4 = Restaurant(restaurant_name="", cuisine_type="")

#9-4. 
#Number Served: Start with your program from Exercise 9-1. 
#Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. 
#Print the number of customers the restaurant has served, and then change this value and print it again. 
#Add a method called set_number_served() that lets you set the number of customers that have been served. 
#Call this method with a new number and print the value again. 
#Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
#Call this method with any number you like that could represent how many customers were served in, say, a day of business. 



#9-3. 
#Users: Make a class called User. Create two attributes called first_name and last_name, 
#and then create several other attributes that are typically stored in a user profile. 
#Make a method called describe_user() that prints a summary of the user’s information. 
#Make another method called greet_user() that prints a personalized greeting to the user. 
#Create several instances representing different users, and call both methods for each user.

class User:
    def __init__(self,
                 first_name:str,
                 last_name:str,
                 age:int,
                 email:str,
                 cf:str):
        self.first_name=first_name
        self.last_name=last_name
        self.cf=cf
        self.age=age
        self.email=email
    
    def __str__(self) -> str:
        return f"L'utente corrente si chiama {self.first_name} {self.last_name}, ha {self.age} anni, il su CF è {self.cf} e la sua mail è {self.email}"
    
user1 = User(first_name="Elia", 
             age=19,
             last_name="Squarti",
             email="myemail@gmail.com",
             cf="not_defined")

user2 = User(first_name="Diego",
             last_name="Pica",
             age=6,
             email="diegoemail@gmail.com",
             cf="unkown")

#9-5. 
#Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. 
#Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
#Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
#Make an instance of the User class and call increment_login_attempts() several times. 
#Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
#Print login_attempts again to make sure it was reset to 0.

