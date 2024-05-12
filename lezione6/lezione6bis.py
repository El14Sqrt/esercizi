from typing import Tuple

class Persona:
    def __init__(self, 
                nome:str,
                cognome:str,
                data_nascita:str,
                genere:str,
                codice_fiscale:str):
    
        self.nome=nome
        self.cognome=cognome
        self.data_nascita=data_nascita
        self.genere=genere
        self.codice_fiscale=codice_fiscale

    def calcola_età(self) ->int:
        current_year = 2024
        birth_year = int(self.data_nascita[-4:])
        age = current_year - birth_year
        return age
    
    def __eq__(self, value: object) -> bool:
        return value.codice_fiscale == self.codice_fiscale

persona1: Persona = Persona(nome="Mario", cognome="Rossi", data_nascita="10 maggio 1989", genere="M")   #devo sempre speciaficare cosìè quello che scrivo: nome, età...

class Dipendente(Persona):  #ereditarietà
    def __init__(self, 
                 nome: str, 
                 cognome: str, 
                 data_nascita: str, 
                 genere: str, 
                 ore_lavorate:int) ->None:
        
        super().__init__(nome, cognome, data_nascita, genere)   #fa riferimento alla superclasse, ovvero persona: non devo riscrivere le variabili

        self.ore_lavorate=ore_lavorate

    def calcola_stipendio(self) ->float:
        return 500.0
    

dipendente1: Dipendente = Dipendente(nome="Flavio", cognome="Giorgi", data_nascita="24/12/1994", genere="M", ore_lavorate=200)

print(persona1.calcola_età())
#print(persona1.calcola_stipendio())    la classe persona non ha il metodo calcola stipendio, poichè l'ho creato nella sottoclasse

print(dipendente1.nome)
print(dipendente1.nome, dipendente1.cognome, "ha", dipendente1.calcola_età(),  "anni")    #eredita anche i metodi della classe superiore
print(dipendente1.calcola_stipendio())

print(dipendente1.ore_lavorate)
#print(persona1.ore_lavorate)    la classe persona non ha l'attributo ore_lavoratedio, poichè l'ho creato nella sottoclasse

class Professore(Dipendente):  #ereditarietà
    def __init__(self, nome: str, 
                 cognome: str, 
                 data_nascita: str, 
                 genere: str, 
                 ore_lavorate: int, 
                 materia_insegnata:str, 
                 ore_lezione:int) -> None:
        
        super().__init__(nome, cognome, data_nascita, genere, ore_lavorate)

        self.materia_insegnata=materia_insegnata
        self.ore_lezione=ore_lezione


professore1: Professore = Professore(nome="Simone", cognome="Ravera", data_nascita= "29 dicembre 1996", genere= "M", ore_lavorate = 30, materia_insegnata = "giardinaggio", ore_lezione = 10)

print("\n"+professore1.nome, professore1.cognome, "ha", professore1.calcola_età(),  "anni e fa il manutentore e deve lavorare per", professore1.ore_lavorate, "ore")

professore2: Professore = Professore(nome="Francesco", cognome="Totti", data_nascita="27 settembre 1976", genere="M", ore_lavorate=2000, materia_insegnata="Calcio", ore_lezione=0)

