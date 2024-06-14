class Persona:
    
    def __init__(self, __first_name: str, __last_name: str):
        if isinstance(__first_name, str) and isinstance(__last_name, str) is True:
            
            self.__first_name = __first_name
            self.__last_name = __last_name
            self.__age = 0

        else:
            print("Il nome inserito non è una stringa")
            self.__first_name = None
            self.__last_name = None
            self.__age = None

    
    def setName(self, name: str):
        if isinstance(name, str) is True:
            self.__first_name = name
        else:
            print("Il nome inserito deve essere una stringa!") 


    def setLastName(self, surname: str):
        if isinstance(surname, str) is True:
            self.__last_name = surname
        else:
            print("Il congnome inserito deve essere una stringa!") 


    def setAge(self, age: int):
        if isinstance(age, int) is True:
            self.__age = age
        else:
            print("L'età deve essere un numero intero!") 


    def getName(self):
        return self.__first_name

    def getLastname(self):
        return self.__last_name

    def getAge(self):
        return self.__age


    def greet(self):
        print(f"Ciao, sono {self.__first_name} {self.__last_name}! Ho {self.__age} anni!")