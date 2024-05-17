#Esercizi vari (funzioni, classi, ereditarietà, e polimorfismo)

#ESERCIZIO 1

"""
Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.

Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa, 
in genere utilizzando tutte le lettere originali esattamente una volta.
"""

def anagram(s: str, t: str) -> bool:
    s_stripped=s.strip()
    t_stripped=t.strip()
    if len(s_stripped)==len(t_stripped):
        s_low=s_stripped.lower()
        t_low=t_stripped.lower()
        s_sorted=sorted(s_low)
        t_sorted=sorted(t_low)
        if s_sorted == t_sorted:
            return True
        else:
            return False
    else:
        return False

print(anagram("Ana gram","na Garam"))
print(anagram("rat", "car"))
print(anagram("silent","listen"))
print(anagram("NeurIPS","UniReps"))

#ESERCIZIO 2

#Progettare un semplice sistema bancario con i seguenti requisiti:

#    Classe del Account:
#        Attributi:
#            account_id: str - identificatore univoco per l'account.
#            balance: float - il saldo attuale del conto.
#        Metodi:
#            deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
#            get_balance(): restituisce il saldo corrente del conto.
#    Classe Bank:
#        Attributi:
#            accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
#        Metodi:
#            create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
#            deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
#            get_balance(account_id): restituisce il saldo del conto con l'ID specificato.


class Account:
    def __init__(self, account_id: str, balance: float = 0.0) -> None:
        self.account_id = account_id
        self.balance = balance
    
    def deposit(self, amount: float):
        self.balance += amount

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self, accounts: dict[str, Account] = None) -> None:
        if accounts is None:
            accounts = {}
        self.accounts = accounts
    
    def create_account(self, account_id: str) -> Account:
        if account_id in self.accounts:
            raise ValueError ("Account with this ID already exists")
        else:
            self.accounts[account_id] = Account(account_id, 0.0)
        return self.accounts[account_id]
    
    def deposit(self, account_id: str, amount: float):
        if account_id in self.accounts:
            self.accounts[account_id].deposit(amount)

    def get_balance(self, account_id: str) -> float:
        if account_id in self.accounts:
            return self.accounts[account_id].get_balance()
        else:
            raise ValueError ("Account not found")

            

bank = Bank()
account1 = bank.create_account("123")
print(account1.get_balance())

bank = Bank()
account1 = bank.create_account("123")
bank.deposit("123",100)
print(bank.get_balance("123"))

bank = Bank()
account2 = bank.create_account("456")
bank.deposit("456",200)
print(bank.get_balance("456"))

bank = Bank()
account1 = bank.create_account("123")
try:
    bank.create_account("123")
except ValueError as e:
    print(e)

bank = Bank()
try:
    bank.get_balance("456")
except ValueError as e:
    print(e)


#ESERCIZIO 5

#Determina se una tavola Sudoku 9 x 9 è valida. Solo le celle compilate devono essere convalidate secondo le seguenti regole:

#    Ogni riga deve contenere le cifre 1-9 senza ripetizioni.
#    Ciascuna colonna deve contenere le cifre da 1 a 9 senza ripetizioni.
#    Ciascuno dei nove sottoriquadri 3 x 3 della griglia deve contenere le cifre 1-9 senza ripetizione.

#Nota:

#    Una tavola Sudoku (parzialmente riempita) potrebbe essere valida ma non è necessariamente risolvibile.
#    Solo le celle riempite devono essere convalidate secondo le regole menzionate.

def valid_sudoku(board: list[list[str]]) -> bool:
    # la tavola del sudo viene rapperentata come una matrice (lista di liste)
    # con 9 righe e 9 colonne
    pass

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(valid_sudoku(board))              #-->True

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(valid_sudoku(board))              #-->False

	


#ESERCIZIO 7

#Data una stringa s e una lista di stringhe wordDict, restituisce True se s può essere segmentato in una sequenza separata 
#da spazi di una o più parole del dizionario; False altrimenti.
#Tieni presente che la stessa parola nel dizionario può essere riutilizzata più volte nella segmentazione.


def word_break(s: str, wordDict: list[str]) -> bool:
    pass

#print(word_break("applepenapple", ["apple","pen"])) -->True
#print(word_break("catsandog",["cats","dog","sand","and","cat"])) -->False