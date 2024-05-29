from abc import ABC, abstractmethod

class AbcAnimal(ABC):

    @abstractmethod
    def verso(self):
        pass
    
    @abstractmethod
    def movimento(self):
        pass


class Cane(AbcAnimal):
    def __init__(self, nome:str) -> None:
        super().__init__()

        self.nome = nome
        self.velocità: float = 10.0 #m/s

    def verso(self):
        return print("Bau!")
    
    def movimento(self, t: int):
        return self.velocità * t
    
cane_1: Cane = Cane(nome="Pluto")
cane_1.verso()
cane_1.movimento(t=10)


class Gatto(AbcAnimal):
    def __init__(self, nome:str) -> None:
        super().__init__()
    
        self.nome = nome
        self.velocità: float = 12.0 #m/s

    def verso(self):
        return print("Meow!")
    
    def movimento(self, t: int):
        return self.velocità * t
 
gatto_1: Gatto = Gatto(nome="Scamorza")
gatto_1.verso()
gatto_1.movimento(t=10)

