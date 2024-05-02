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

def remove_duplicates(lst: list) -> list:
    seen = set()                # Insieme per tenere traccia degli elementi unici già visti
    result = []                 # Lista per mantenere l'ordine originale degli elementi unici
    for item in lst:
        if item not in seen:    # Se l'elemento non è già stato visto, lo aggiungiamo alla lista di risultati
            result.append(item)
            seen.add(item)      # Aggiungiamo l'elemento all'insieme degli elementi visti
    return result

print(remove_duplicates([]))
print(remove_duplicates([1, 1, 1, 1]))
print(remove_duplicates([4, 5, 'a', 4, 6]))

	

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
#Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.
#esempio: print(frequency_dict(['mela', 'banana', 'mela'])) il risultato è: {'mela': 2, 'banana': 1}

def frequency_dict(elements: list) -> dict:
    freq_dict = {}              # Dizionario per memorizzare la frequenza di ciascun elemento
    for item in elements:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict

print(frequency_dict(['mela', 'banana', 'mela']))
print(frequency_dict([1, 2, 2, 3, 3, 3]))


#ESERCIZIO 7
#Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, 
#cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.

def check_parentheses(expression: str) -> bool:
    stack = []               # Stack per tenere traccia delle parentesi aperte
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                return False
    return len(stack) == 0

print(check_parentheses("(()))("))
print(check_parentheses("((()))"))


#ESERCIZIO 8
#Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. 
#Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.

def count_isolated(numbers: list) -> int:
    count = 0               # Contatore per tenere traccia del numero di elementi isolati
    for i in range(len(numbers)):
                            # Verifica se l'elemento corrente è isolato
        if (i == 0 or numbers[i] != numbers[i-1]) and (i == len(numbers)-1 or numbers[i] != numbers[i+1]):
            count += 1
    return count

print(count_isolated([1, 2, 2, 3, 3, 3, 4]))
print(count_isolated([1, 2, 3, 4, 5]))