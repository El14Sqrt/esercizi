#LA TARTARUGA E LA LEPRE

import random


global T
T = 1                           #posizione iniziale tartaruga
global H
H = 1                           #posizione inziale lepre

posizioni = list("_" * 70)      #lunghezza percorso



class Tartaruga:
    def __init__(self):
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
    def __init__(self): 
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
    def __init__(self, lepre: Lepre, tartaruga: Tartaruga):
        self.lepre = lepre
        self.tartaruga = tartaruga        

    
    def mosse_tartaruga(self, tartaruga: Tartaruga):
        percentuale = random.randint(1, 10)

        if 1 <= percentuale <= 5:
            tartaruga.passo_veloce()
        elif 6 <= percentuale <= 7:
            tartaruga.scivolata()
        elif 8 <= percentuale <= 10:
            tartaruga.passo_lento()


    def mosse_lepre(self, lepre: Lepre):
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
        



def inizio_gara():
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    while True:
        Mosse.mosse_lepre()
        Mosse.mosse_tartaruga()
        if H in posizioni and T in posizioni:
            posizioni.remove(H)
            posizioni.remove(T)
            posizioni.append("_")
            posizioni.append("_")
            if H == T:
                posizioni[H] = "OUCH!!!"
            else:
                posizioni[H] = H
                posizioni[T] = T
        elif "OUCH!!!" in posizioni:
            posizioni.remove("OUCH!!!")
            posizioni.append("_")
            if H == T:
                posizioni[H] = "OUCH!!!"
            else:
                posizioni[H] = H
                posizioni[T] = T
        else:
            posizioni[H] = H
            posizioni[T] = T
        
        print(posizioni)

inizio_gara()