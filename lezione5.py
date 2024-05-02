#QUIZ: ESERCIZI RIEPILOGAIVI E DI RIPASSO

#ESERCIZIO 1
#Scrivi una funzione che calcola la media di una lista di numeri e ritorna il valore arrotondato all'intero più vicino.

def rounded_average(numbers: list[int]) -> int:
    somma = 0
    for n in numbers:
        somma += n
    media = somma / len(numbers)
    rounded_media = round(media)
    return rounded_media
print(rounded_average([100, 200, 300, 400]))
print(rounded_average([1, 1, 2, 2]))


#ESERCIZIO 2
#Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). 
#L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo. 
#La funzione ritorna "Accesso consentito" oppure "Accesso negato".

def check_access(username: str, password: ..., is_active: bool) -> str:
    if username == "admin" and password == "12345" and is_active == True:
        return "Accesso consentito"
    else:
        return "Accesso negato"

print(check_access("admin", "12345", True))
print(check_access("admin", "54321", False))


#ESERCIZIO 3
#Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. 
#L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. 
#La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.

def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA == True or conditionB == True and conditionC == True:
        return "Operazione permessa"
    else:
        return "Operazione negata"
    
print(check_combination(True, False, True))
print(check_combination(False, True, False))
print(check_combination(False, True, True))


#ESERCIZIO 4
#Scrivi una funzione che rimuove tutti i duplicati da una lista, 
#contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.

def remove_duplicates() -> list:
    

#ESERCIZIO 5
#Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. 
#La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione 
#e l'elemento iniziale viene spostato alla fine della lista. Per la rotazione utilizzare lo slicing 
#e gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.
"""
def rotate_left(elements: list, k: int) -> list:
    k = k % len(elements)  # Calcola il numero effettivo di posizioni da ruotare
    rotated_elements = elements[k:] + elements[:k]
    return rotated_elements

print(rotate_left([1, 2, 3, 4, 5], 2))
print(rotate_left([1, 2, 3, 4, 5], 8))
"""

#ESERCIZIO 6
#