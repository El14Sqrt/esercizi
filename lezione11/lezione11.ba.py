class Banca:
    def __init__(self, nome:str, simbolo:str) -> None:
        self.nome:str = nome 
        self.simbolo = simbolo

class Filiale:
    def __init__(self, codice, indirizzo, banca: Banca) -> None:
        self.codice = codice
        self.inidirizzo = indirizzo
        self.banca = banca 

unicredit: Banca = Banca(nome="Unicredit", simbolo="UCG")
intesa: Banca = Banca(nome="Intesa San Paolo", simbolo= "ISP")

