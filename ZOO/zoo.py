#Sistema di gestione dello zoo virtuale

class Animal:
    def __init__(self, name:str, species:str, age:float, height:float, width:float, preferred_habitat:str, health: float):
        self.name=name
        self.species=species
        self.age=age
        self.height=height
        self.width=width
        self.preferred_habitat=preferred_habitat
        self.healt=health ==round(100 * (1 / self.age), 3) #non fare i round per le operazioni


class Fence:
    def __init__(self, area:float, temperature:float, habitat:str):
        self.area=area
        self.temperature=temperature
        self.habitat=habitat
        self.animals: list = []



class ZooKeeper:
    def __init__(self, name:str, surname:str, id:str):
        self.name=name
        self.surname=surname
        self.id=id
    
    def add_animal(animal: Animal, fence: Fence):
        pass

    def remove_animal(animal: Animal, fence: Fence):
        pass

    def clean(fence: Fence):
        pass

    def feed(animal: Animal):
        pass
    

class Zoo:
    def __init__(self, fences:list[Fence], zoo_keepers:list[ZooKeeper]):
        self.fences=fences
        self.zoo_keepers=zoo_keepers
    
    def describe_zoo(self):
        print("Guardians:")
        for zk in self.zoo_keepers:
            print(f"ZooKeeper(name={zk.name}, surname={zk.surname}, id={zk.id})")
        print("\nFences:")
        for f in self.fences:
            print(f"Fence(area={f.area}, temperature={f.temperature}, habitat={f.habitat})")
            print("with animals:")
            in Fence, for a in self.animals:
                print(f"Animal(name={a.name}, species={a.species}, age={a.age})")
            print("#" * 30)

