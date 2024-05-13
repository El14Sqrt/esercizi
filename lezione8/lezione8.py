class Animal:
    def __init__(self, specie:str, name:str, age:int) -> None:
        self.specie=specie
        self.age=age
        self.name=name
    
     #def __str__(self) -> str:
        #return f"{self.__class__.__name__}(name={self.name}, age={self.age})

class Cat(Animal):
    def __init__(self, specie: str, name: str, age: int) -> None:
        super().__init__(specie, name, age)

class Rabbit(Animal):
    def __init__(self, specie: str, name: str, age: int) -> None:
        super().__init__(specie, name, age)

class Person(Animal):
    def __init__(self, specie: str, age: int, name: str, surname:str, cf: str) -> None:
        super().__init__(specie, age)
        self.cf=cf
        self.name=name
        self.surname=surname
    

class Student(Person):
    def __init__(self, specie: str, age: int, name: str, surname: str, cf: str, matricola:int) -> None:
        super().__init__(specie, age, name, surname, cf)
        self.matricola=matricola


#a=Animal()
p=Person(name="Lorenzo", surname="Maggi", cf="undefined", specie="human", age=22)
#c=Cat()
#print(a)
print(p)