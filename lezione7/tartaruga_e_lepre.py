#LA TARTARUGA E LA LEPRE

#lunghezza percorso: 70 quadrati
#1 = inizio , 70 = traguardo
# T = tartaruga , H = lepre

import random

global T
T = 1                           #posizione iniziale tartaruga
global H
H = 1                           #posizione inziale lepre


class Tartaruga:
    def __init__(self) -> None:
        self.T = T
        

    def passo_veloce(self):
        T += 3

    def scivolata(self):
        if T >= 7:
            T -= 6
        else:
            T = 1

    def passo_lento(self):
        T += 1



class Lepre:
    def __init__(self) -> None:
        self.H = H
        

    def riposo(self):
        H += 0

    def grande_balzo(self):
        H += 9

    def grande_scivolata(self):
        if H >= 13:
            H -= 12
        else:
            H = 1

    def piccolo_balzo(self):
        T += 1

    def piccola_scivolata(self):
        if H >= 3:
            H -= 2
        else:
            H = 1

class Mosse:
    def __init__(self, lepre: Lepre, tartaruga: Tartaruga) -> None:
        self.lepre = lepre
        self.tartaruga = tartaruga        

    
    def mosse_tartaruga(self, tartaruga):
        percentuale = random.randint(1, 10)

        if 1 <= percentuale <= 5:
            tartaruga.passo_veloce()
        elif 6 <= percentuale <= 7:
            tartaruga.scivolata()
        elif 8 <= percentuale <= 10:
            tartaruga.passo_lento()


    def mosse_lepre(self, lepre):
        percentuale = random.randint(1, 10)

        if 1 <= percentuale <= 2:
            lepre.riposo()
        elif 3 <= percentuale <= 4:
            lepre.grande_balzo()
        elif percentuale == 5:
            lepre.grande_scivolata()
        elif 6 <= percentuale <= 8:
            lepre.piccolo_balzo()
        elif 9 <= percentuale <= 10:
            lepre.piccola_scivolata()
        


percorso = list(range(1,71))    #lunghezza percorso
posizioni = list("_" * 70)



def inizio_gara():
    print("BANG !!!!! AND THEY'RE OFF !!!!!")

