#dato un intero x, restituisce True se x è palindromo, e False altrimenti.

#senza usare "return s == s[::-1]"

def is_pal(x: int) -> bool:
    s:str = str(x)
    i:int = 0
    s_length = len(s)
    while i < (s_length // 2): #for i in range(len(s))
        j = s_length - (i+1)
        if s[i] != s[j]:
            return False
        i += 1
    return True

#data una stringa s che contiene parole e spazi, restituire la lunghezza dell'ultima parola in s.
#una parola è una sottostringa che contiene caratteri contugui diversi dallo spazio.

s: str = "oggi è lunedì"

#modo 1
l: list[str] = s.split()
return len(1[-1])

#modo 2
i: int = 0
curr_len: int = 0
while i < len(s):
    if s[i] != " ":
        curr_len += 1
    else:
        break