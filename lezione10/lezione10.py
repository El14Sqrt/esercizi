#ESERCIZIO 1
#Qual è il valore delle seguenti espressioni booleane se x vale 5, y vale 10 e z vale 15?
x = 5
y = 10
z = 15

print(x < 5 and y > x)
print(x < 5 or y > x)
print(x > 3 or y < 10 and z == 15)
print(not(x > 3) and x != z or x + y == z) 

#ESERCIZIO 2
#Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile a nel seguente modo:
#   - se a è pari, deve essere diviso per 2;
#   - se a è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.

def transform(a: int) -> int:
    if a % 2 == 0:
        return a / 2
    else:
        return (a * 3) - 1

print(transform(4)) # --> 2
print(transform(-10)) # --> -5

#ESERCIZIO 3
#Sviluppare una funzione in Python per calcolare lo stipendio lordo di ciascuno dei diversi impiegati. 

#L'azienda paga 10 dollari all'ora per le prime 40 ore di lavoro e paga "una volta e mezza" la paga oraria 
#per tutte le ore di lavoro oltre le 40 ore.
 
#Per ogni operaio, viene fornito il numero di ore che tale impiegato ha lavorato durante la settimana.
#La vostra funzione deve ricevere questa informazione per ogni impiegato e determinare e stampare lo stipendio lordo.

def calcola_stipendio(ore_lavorate: int) -> float:
    if ore_lavorate <= 40:
        paga_ordinaria: float = ore_lavorate * 10
        stipendio: float = float(paga_ordinaria)
    if ore_lavorate > 40:
        paga_ordinaria: float = 40 * 10
        ore_straordinari: int = ore_lavorate - 40
        paga_straordinari: float = ore_straordinari * 15
        stipendio: float = float(paga_straordinari + paga_ordinaria)
    return stipendio

print("stipendio: ", calcola_stipendio(40)) # --> 400.0
print("stipendio: ", calcola_stipendio(0)) # --> 0.0 
print("stipendio: ", calcola_stipendio(60)) # --> 700.0


#ESERCIZIO 4
#Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
#   a) 1, 2, 3, 4, 5, 6, 7
#   b) 3, 8, 13, 18, 23
#   c) 20, 14, 8, 2, -4, -10
#   d) 19, 27, 35, 43, 51


def print_seq(): 
    
    print("Sequenza a):")
    for i in range(1, 8):
        print(i)

    print("Sequenza b):")
    # SCRIVI QUI IL TUO CICLO
    print()

    print("Sequenza c):")
    # SCRIVI QUI IL TUO CICLO
    print()

    print("Sequenza d):")
    # SCRIVI QUI IL TUO CICLO
    print()
    
    return

#ESERCIZIO 5
#Scrivere una funzione chiamata integerPower che, dati in input una base e un esponente, 
#restituisca il risultato della potenza base^exponent. Supporre che base sia un numero intero e 
#che l'esponente sia un valore intero positivo e diverso da 0.
 
#La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
#Non utilizzare nessuna funzione della libreria math!

def integerPower(base: int, esponente: int):
    if esponente != 0 and esponente > 0:    
        potenza: int = base ** esponente

    return potenza

print(integerPower(3, 4)) # --> 81
print(integerPower(2, 5)) # --> 32 

#ESERCIZIO 6
#Definire una funzione chiamata hypotenuse che calcoli la lunghezza dell'ipotenusa di un triangolo rettangolo. #
# ÙLa funzione deve ricevere due argomenti di tipo float (corrispondenti ai due lati del triangolo) 
#e restituire l'ipotenusa come un float.
#Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora.

def hypotenuse(c1:float, c2:float):
    hypotenuse = ((c1 ** 2) + (c2 ** 2)) ** (1/2)
    return hypotenuse

print("lunghezza ipotenusa: ", hypotenuse(3.0, 4.0)) # --> 5.0
print("lunghezza ipotenusa: ", hypotenuse(8.0, 15.0)) # --> 17.0

#ESERCIZIO 7
#