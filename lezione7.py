#ESERCIZI LEZIONE 7

#ESERCIZIO 1
#Scrivi una funzione che determina se un numero è 'magico'. Un numero è considerato magico se è divisibile per 4 ma non per 6.

def numero_magico(num: int) -> bool:
    if num % 4 == 0 and num % 6 != 0:
        return True
    else:
        return False

print(numero_magico(8), numero_magico(32), numero_magico(36))


#ESERCIZIO 2
#Scrivi una funzione che riceve una lista di numeri, 
#filtra i numeri pari, e restituisce una nuova lista con i numeri pari moltiplicati per un fattore dato.

def filtra_moltiplica(lista_numeri: list[int], fattore: int) -> list[int]:
    pari: list = []
    pari_moltiplicati: list = []
    for n in lista_numeri:
        if n % 2 == 0:
            pari.append(n)
        else:
            continue
    for n in pari:
        pari_moltiplicati.append(n*fattore)
    return pari_moltiplicati
    

print(filtra_moltiplica([1, 2, 3, 4, 5, 6], 3)) 


#ESERCIZIO 3
#Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
#Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.


#chiave= el da rimuovere
#valore= n volte che va rimosso

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    nuova_lista: list = lista.copy()
    for el, volte in da_rimuovere.items():
        for _ in range(min(volte, nuova_lista.count(el))):
            if el in lista:
                nuova_lista.remove(el)
    return nuova_lista

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))


#ESERCIZIO 4
#Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti 
#e aggrega i voti per studente in un nuovo dizionario.
'''
def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    registro_voti: dict = {}
    for nomi in voti

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
'''

#ESERCIZIO 5
#Scrivi una funzione che accetti un dizionario di prodotti con i prezzi 
#e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    offerte = {}
    for prodotto, prezzo in prodotti.items():
        if prezzo >= 20.0:
            prezzo_scontato: float = prezzo - (prezzo * 10/100)
            offerte[prodotto] = prezzo_scontato
    return offerte

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
