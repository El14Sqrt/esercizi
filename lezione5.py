#QUIZ: ESERCIZI RIEPILOGAIVI E DI RIPASSO

#Scrivi una funzione che calcola la media di una lista di numeri e ritorna il valore arrotondato all'intero più vicino.

def rounded_average(numbers: list[int]) -> int:
    somma = 0
    for n in numbers:
        somma += n
    media = somma / len(numbers)
    print(media)

rounded_average([2, 3, 5, 7, 10])

