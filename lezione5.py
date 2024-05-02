#QUIZ: ESERCIZI RIEPILOGAIVI E DI RIPASSO

#Scrivi una funzione che calcola la media di una lista di numeri e ritorna il valore arrotondato all'intero più vicino.

def rounded_average(numbers: list[int]) -> float:
    somma = 0
    for n in numbers:
        somma += n
    media = somma / len(numbers)
    rounded_media = round(media)
    return rounded_media
print(rounded_average([100, 200, 300, 400]))
print(rounded_average([1, 1, 2, 2]))