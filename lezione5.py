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