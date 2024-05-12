#ESERCIZI LEZIONE 5

#9-1. 
#Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: 
#a restaurant_name and a cuisine_type. 
#Make a method called describe_restaurant() that prints these two pieces of information, 
#and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
#Make an instance called restaurant from your class. 
#Print the two attributes individually, and then call both methods.

class Restaurant:
    def __init__(self, restaurant_name:str, cuisine_type:str, number_served:int=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self):
        print(f"Restaurant(name: {self.restaurant_name}, cuisine: {self.cuisine_type})")
    
    def open_restaurant(self):
        print(f"Il ristorante {self.restaurant_name} è aperto.")

    def set_number_served(self, new_number_served:int):
        self.number_served = new_number_served

    def increment_number_served(self):
        self.number_served += 1

    

r1 = Restaurant(restaurant_name="La vecchia Roma", cuisine_type="romana", number_served= 45)

r1.describe_restaurant()
r1.open_restaurant()


#9-2. 
#Three Restaurants: Start with your class from Exercise 9-1. 
#Create three different instances from the class, and call describe_restaurant() for each instance.

r2 = Restaurant(restaurant_name="Neko", cuisine_type="Sushi")
r3 = Restaurant(restaurant_name="c1b0", cuisine_type="hamburger")
r4 = Restaurant(restaurant_name="Il peperoncino", cuisine_type="pizzeria")

r2.describe_restaurant()
r3.describe_restaurant()
r4.describe_restaurant()


#9-4. 
#Number Served: Start with your program from Exercise 9-1. 
#Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. 
#Print the number of customers the restaurant has served, and then change this value and print it again. 
#Add a method called set_number_served() that lets you set the number of customers that have been served. 
#Call this method with a new number and print the value again. 
#Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
#Call this method with any number you like that could represent how many customers were served in, say, a day of business. 

print("Number of customers served:", r1.number_served)
r1.set_number_served(50)
print("New number of customers served:", r1.number_served)

r1.increment_number_served()
print("customers served:", r1.number_served)
r1.increment_number_served()
print("customers served:", r1.number_served)



#9-6. 
#Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
#Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4. 
#Either version of the class will work; just pick the one you like better. 
#Add an attribute called flavors that stores a list of ice cream flavors. 
#Write a method that displays these flavors. 
#Create an instance of IceCreamStand, and call this method. 

class IceCreamStand(Restaurant):
    def __init__(self, flavors: list[str], restaurant_name: str, cuisine_type: str = None, number_served: int = 0):
        super().__init__(restaurant_name, cuisine_type, number_served)
    
        self.flavors=flavors

    def show_flavors(self):
        print(f"The ice cream stand {self.restaurant_name} offers the following flavors of ice cream: {self.flavors}")

Ice_Cream_Stand_1 = IceCreamStand(["chocolate", "strawberry", "lemon", "cream"], restaurant_name="Gelato Matto")
Ice_Cream_Stand_1.show_flavors()


#9-10. 
#Imported Restaurant: Using your latest Restaurant class, store it in a module. 
#Make a separate file that imports Restaurant. 
#Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.



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
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Information:\n"
              f"First Name: {self.first_name}\n"
              f"Last Name: {self.last_name}\n"
              f"Age: {self.age}\n"
              f"Email: {self.email}\n"
              f"CF: {self.cf}")
        
    def greet_user(self):
        print(f"Welcome back {self.first_name}! How are you today?")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

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


print("\n")
user1.describe_user()
print("\n")
user2.describe_user()

user1.greet_user()
user2.greet_user()



#9-5. 
#Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. 
#Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
#Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
#Make an instance of the User class and call increment_login_attempts() several times. 
#Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
#Print login_attempts again to make sure it was reset to 0.

print("\n")
print("user1 Login attempts: ", user1.login_attempts)
user1.increment_login_attempts()
print("user1 Login attempts: ", user1.login_attempts)
user1.increment_login_attempts()
user1.increment_login_attempts()
print("user1 Login attempts: ", user1.login_attempts)
print("\n")
user1.reset_login_attempts()
print("user1 Login attempts: ", user1.login_attempts)



#9-7. 
#Admin: An administrator is a special kind of user. 
#Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5. 
#Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", 
#and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. 
#Create an instance of Admin, and call your method. 

class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, email: str, cf: str):
        super().__init__(first_name, last_name, age, email, cf)

        #self.privileges = Privileges(privileges) ----> per l'esercizio successivo
        self.privileges = ["can add post", "can delete post", "can ban user", "can control user settings"]

    def show_privileges(self):
        print(f"Admin privileges: {self.privileges}")
    
admin01 = Admin(first_name="Bob", last_name="White", age=39, email="bobemail@boh.org", cf="NJINIO51E4G94R8B")
admin01.show_privileges()

print("\n")



#9-8. 
#Privileges: Write a separate Privileges class. 
#The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
#Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. 
#Create a new instance of Admin and use your method to show its privileges.

class Privilege:
    def __init__(self, privileges:list[str]):
        self.privileges=privileges

    def show_privileges(self):
        print(f"privileges: {self.privileges}")

"""
admin02 = Admin(first_name="Alice", last_name="Vegas", age=45, email="alicemail@example.net", cf="alice_cf", privileges=["can add post", "can delete post", "can ban user", "can control user settings"])

admin02.privileges.show_privileges()
"""

print("\n")


#9-11. 
#Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges, and Admin in one module. 
#Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.

from lez_5_es_911_Imported_Admin import Admin

admin03 = Admin(first_name="Andrea",
                       last_name="Sila",
                       age=82,
                       email="andre@ndebfiu.com",
                       cf="BIUFVR45RHRG56GRH",
                       privileges=["can add post", "can delete post", "can ban user", "can control user settings"])

admin03.privileges.show_privileges()



#9-12. 
#Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. 
#In a separate file, create an Admin instance and call show_privileges() 
#to show that everything is still working correctly.



