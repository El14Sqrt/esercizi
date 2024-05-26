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
    seq_a: list = []
    for i in range(1, 8):
        seq_a.append(i)
    for i in seq_a:
        print(i)

    print("\nSequenza b):")
    seq_b: list = []
    for i in range(3, 24, 5):
        seq_b.append(i)
    for i in seq_b:
        print(i)

    print("\nSequenza c):")
    seq_c: list = []
    for i in range(-10, 21, 6):
        seq_c.append(i)
    seq_c.reverse()
    for i in seq_c:
        print(i)

    print("\nSequenza d):")
    seq_d: list = []
    for i in range(19, 52, 8):
        seq_d.append(i)
    for i in seq_d:
        print(i)



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
#Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, 
#mantenendo l'ordine originale degli elementi.


def remove_duplicates(starting_list: list) -> list:
    new_list: list = []
    for i in starting_list:
        n = starting_list.count(i)
        if n == 1:
            new_list.append(i)
        elif n >= 2 and i not in new_list:
            new_list.append(i)

    return new_list


print(remove_duplicates([1, 2, 3, 1, 2, 4])) #--> [1, 2, 3, 4]
print(remove_duplicates([4, 5, 'a', 4, 6])) #--> [4, 5, 'a', 6]


#ESERCIZIO 8
#Scrivere la funzione chiamata seconds_since_noon che riceva il tempo espresso come tre argomenti interi (ore, minuti e secondi)
# e restituisca il numero dei secondi da quando l'orologio "ha battuto le 12" l'ultima volta 
#(le ore 12, dunque, vengono considerate come orario di partenza, dunque, come uno zero).

#Ad esempio, alle ore 3:15:50 sono passate 3 ore, 15 minuti e 50 secondi, ovvero sono passati 11750 secondi 
#da quando l'orologio ha "battuto le 12" per l'ultima volta.

#Definire, poi, la funzione chiamata time_difference che prende come argomento due orari, 
#entrambi espressi mediante ore, minuti e secondi. 
#La funzione time_difference deve usare la funzione seconds_since_noon per calcolare la quantità di tempo in secondi tra due orari, 
#entrambi contenuti entro un ciclo dell'orologio di 12 ore.

#Ad esempio, tra le ore 1:00 e 3:15:30 sono passati 8130 secondi.

def seconds_since_noon(ore: int, minuti: int, secondi: int) -> int:
    # Calcola i secondi totali a partire dalle 12:00:00
    return (ore * 3600) + (minuti * 60) + secondi

def time_difference(orari: tuple) -> int:
    # Estrai i due orari dalla tupla
    orario1, orario2 = orari
    
    # Calcola i secondi trascorsi dalle 12:00 per ciascun orario
    secondi_orario1 = seconds_since_noon(*orario1)
    secondi_orario2 = seconds_since_noon(*orario2)
    
    # Calcola la differenza assoluta tra i due orari in secondi
    return abs(secondi_orario2 - secondi_orario1)

# Esempio di utilizzo
orario1 = (1, 0, 0)  # 1:00:00
orario2 = (3, 15, 30)  # 3:15:30
print(time_difference((orario1, orario2)))  # Output: 8130


print(time_difference(1, 0, 0, 3, 15, 30)) # --> 8130
print(time_difference(0, 0, 0, 12, 0, 0)) # --> 43200

#ESERCIZIO 9
#Si scriva una funzione in Python che simuli una palla che rimbalza calcolando la sua altezza da terra in centimetri 
#per ogni secondo, a mano a mano che il tempo passa su un orologio simulato.

#Al tempo zero la palla comincia ad altezza zero e ha una velocità iniziale di 100 cm/s.

#Dopo ogni secondo, il valore dell'altezza cambia, aggiungendo al valore corrente dell'altezza il valore della velocità corrente; 
#poi, il valore della velocità viene modificato, sottraendo 96 al valore della velocità corrente.
#Dunque, dopo ogni secondo, si ha che
#altezza = altezza + velocità
#velocità = velocità - 96.

#Se il nuovo valore che si ottiene per l'altezza è inferiore a 0, si deve moltiplicare altezza e velocità per -0.5 
#per simulare il rimbalzo. Dunque, per il rimbalzo, si avrà che
#altezza= altezza*-0,5 
#velocità=velocità*-0,5.

#Ci si fermi al quinto rimbalzo.
 
#Per ogni secondo, la funzione deve stampare il tempo trascorso e l'altezza a cui si trova la palla in quel determinato secondo.
#Ad esempio, se al tempo 0, la palla si trova ad altezza 0 cm, allora la funzione stamperà:
 
#"Tempo: 0 Altezza: 0"

#Se avviene il rimbalzo, la funzione deve stampare il tempo trascorso e la parola "Rimbalzo!".
#Ad esempio, se il rimbalzo avviene al tempo 4, allora la funzione stamperà:
 
#"Tempo: 4 Rimbalzo!"

def rimbalzo() -> None:
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0

    while rimbalzi < 5:
        print(f"Tempo: {tempo} Altezza: {altezza}")
        altezza += velocita
        velocita -= 96
        tempo += 1

        if altezza < 0:
            altezza *= -0.5
            velocita *= -0.5
            rimbalzi += 1
            print(f"Tempo: {tempo} Rimbalzo!")
        

rimbalzo()

#ESERCIZIO 10

#Si immagini una funzione che comprime i file all'80% e li salva su un supporto di memorizzazione. 
#Prima che il file compresso venga memorizzato, deve essere diviso in blocchi da 512 byte ciascuno.
 
#Si sviluppi in Python un algoritmo per questa funzione che prende in input una lista di valori interi, 
#dove ogni valore intero della lista rappresenta la dimensione non compressa di un singolo file espressa in byte.
 
#Tale funzione deve utilizzare un ciclo per iterare la lista e, per ogni dimensione non compressa, 
#deve calcolare la dimensione compressa di tale file espressa come float (ovvero deve calcolare l' 80% della dimensione non compressa), 
#calcolare il numero di blocchi (arrotondato al numero intero più vicino) da 512 byte necessari per la memorizzazione, 
#al fine di determinare se il file compresso può essere salvato nello spazio rimanente nel supporto di memorizzazione o meno.
 
#In caso affermativo, il programma memorizza il file. In tal caso, la funzione deve stampare la dimensione originale del file, la dimensione compressa, 
#i blocchi utilizzati per memorizzare il file in questione e i blocchi disponibili rimasti sul supporto di memorizzazione. 
#Ad esempio, se è possibile salvare sul supporto di memorizzazione un file avente dimensione pari a 1100 byte, la funzione stamperà:
 
#"File di 1100 byte compresso in 880.0 byte e memorizzato. Blocchi usati: 2. Blocchi rimanenti: 998."
 
#Il ciclo continua finché non viene riscontrato un file della lista la cui dimensione compressa occupa un numero di blocchi più grande di quelli rimasti disponibili 
#sul supporto di memorizzazione. In tal caso, la funzione deve avvisare l'utente che lo spazio disponibile sul supporto di memorizzazione non è sufficiente per salvare il file. 

#Ad esempio, se non è possibile salvare sul supporto di memorizzazione un file avente dimensione pari a 1048576 byte, la funzione stamperà:
 
#"Non è possibile memorizzare il file di 1048576 byte. Spazio insufficiente."

#Inizialmente, il numero totale di blocchi disponibili sul supporto di memorizzazione per il salvataggio dei file è un numero intero pari a 1000 blocchi. 

def memorizza_file(files: list[int]) -> None:
    spazio_totale_blocchi = 1000  # Spazio totale disponibile in blocchi
    
    for dimensione_non_compressa in files:
        # Calcolare la dimensione compressa (80% della dimensione non compressa)
        dimensione_compressa = dimensione_non_compressa * 0.80
        
        # Calcolare il numero di blocchi necessari (arrotondato al numero intero più vicino)
        blocchi_necessari = round(dimensione_compressa / 512)
        
        # Verificare se ci sono abbastanza blocchi disponibili
        if blocchi_necessari <= spazio_totale_blocchi:
            # Aggiornare lo spazio disponibile
            spazio_totale_blocchi -= blocchi_necessari
            
            # Stampare i dettagli del file memorizzato
            print(f"File di {dimensione_non_compressa} byte compresso in {dimensione_compressa:.1f} byte e memorizzato. "
                  f"Blocchi usati: {blocchi_necessari}. Blocchi rimanenti: {spazio_totale_blocchi}.")
        else:
            # Stampare un avviso di spazio insufficiente
            print(f"Non è possibile memorizzare il file di {dimensione_non_compressa} byte. Spazio insufficiente.")
            break

# Esempio di utilizzo della funzione
files = [1100, 1048576, 512, 25600, 128000]
memorizza_file(files)


memorizza_file([1100, 20000, 1048576, 512, 5000])