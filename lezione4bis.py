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

#data una stringa s che contiene parole e spazi, restituire una stringa