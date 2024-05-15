#Sistema di gestione dello zoo virtuale

class Animal:
    def __init__(self, name:str, species:str, age:float, height:float, width:float, preferred_habitat:str, health: float = (100 * (1 / age), 3)):
        self.name=name
        self.species=species
        self.age=age
        self.height=height
        self.width=width
        self.preferred_habitat=preferred_habitat
        self.healt=round(health) #non fare i round per le operazioni
        self.area_animal: float = self.height * self.width

class Fence:
    def __init__(self, area:float, temperature:float, habitat:str):
        self.area=area #diminuisce ogni volta che faccio add_animal
        self.temperature=temperature
        self.habitat=habitat
        self.animals: list = []
        self.total_area: float = area #perchè dopo in clean mi serve l'area iniziale
        


class ZooKeeper:
    def __init__(self, name:str, surname:str, id:str):
        self.name=name
        self.surname=surname
        self.id=id
    
    def add_animal(animal: Animal, fence: Fence):   #controllo habitat -> controllo area animale
        if animal.preferred_habitat == fence.habitat and animal.area_animal <= fence.area: 
            fence.animals.append(animal)
            fence.area -= animal.area_animal

    def remove_animal(animal: Animal, fence: Fence):
        fence.animals.remove(animal)
        fence.area += animal.area_animal

    def clean(fence: Fence):
        pass

    def feed(animal: Animal):
        pass
    

class Zoo:
    def __init__(self, fences:list[Fence], zoo_keepers:list[ZooKeeper]):
        self.fences=fences
        self.zoo_keepers=zoo_keepers
        self.animals=fence.animals
    
    def describe_zoo(self):
        print("Guardians:")
        for zk in self.zoo_keepers:
            print(f"ZooKeeper(name={zk.name}, surname={zk.surname}, id={zk.id})")
        print("\nFences:")
        for f in self.fences:
            print(f"Fence(area={f.area}, temperature={f.temperature}, habitat={f.habitat})")
            print("with animals:")
            for a in self.animals[Fence]:
                print(f"Animal(name={a.name}, species={a.species}, age={a.age})")
            print("#" * 30)

