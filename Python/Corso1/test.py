import math
# Stringa
#string = "Hello World"

# Integrale
#int = 1 

# Stringa x
x = "marchetto"

# Stampa il tipo di x
#print(type(x))

# Stampo un errore poichè non esiste variabile upper o lower
# print(upper.x)
# print(lower.x)

# Stampo il primo carattere di x
print(x[0])
print(x[8])
print(x[0:2])


# Operazioni aritmetiche
# Esegui le operazioni aritmetiche tra x e y
# Stampo il risultato di ogni operazione

# Addizione
print(x + y)  # Aggiunge due stringhe

# Sottrazione
print(x - y)  # Ritorna un errore poichè non è possibile eseguire la sottrazione tra stringhe

# Moltiplicazione
print(x * y)  # Moltiplica la stringa x per il valore di y

# Divisione
print(x / y)  # Divide la stringa x per il valore di y

# Divisione intera (lascia la parte intera)
print(x // y) # Divide la stringa x per il valore di y e restituisce la parte intera

# Resto della divisione
print(x % y)  # Calcola il resto della divisione tra la stringa x e il valore di y

# Potenza
print(x ** y) # Elevamento alla potenza: la stringa x è elevata al valore di y

# Valore assoluto
print(abs(-5))     # Ritorna il valore assoluto di un numero, ovvero il numero positivo

# Arrotondamento a numero intero più vicino
print(round(3.6))  # Arrotonda un numero a un numero intero più vicino


# Funzione per ottenere il valore assoluto di un numero
# math.abs(-5)     # Ritorna il valore assoluto di un numero, ovvero il numero positivo

# Funzione per arrotondare un numero a un numero intero più vicino
# math.round(3.6)  # Arrotonda un numero a un numero intero più vicino

# Funzione per ottenere il valore di pi greco
# math.pi         # Ritorna il valore di pi greco

# Funzione per ottenere la radice quadrata di un numero
# math.sqrt(16)   # Ritorna la radice quadrata di un numero

# Inizializzo una lista di frutta
frutti = ["mela", "pera", "banana"]  # Inizializzo una lista di stringhe

# Aggiungo una frutta ad essa
frutti.append("kiwi")  # Aggiunge una nuova stringa alla fine della lista

# Rimuovo una frutta dalla lista
frutti.remove("pera")  # Rimuove la prima occorrenza della stringa "pera" dalla lista

# Stampo il primo elemento della lista
print(frutti[0])  # Stampa il primo elemento della lista, ovvero "mela"



# Inizializzo un dizionario di persona
persona = {
    "nome": "Marco",  # Chiave: "nome", Valore: "Marco"
    "eta": 20,       # Chiave: "eta", Valore: 20
    "città": "Padova" # Chiave: "città", Valore: "Padova"
}

# Stampo il valore associato alla chiave "nome"
print(persona["nome"])  # Stampa "Marco"

# Stampo il valore associato alla chiave "eta"
print(persona.get("eta"))  # Stampa 20

# Stampo il valore associato alla chiave "città"
print(persona.get("città"))  # Stampa "Padova"

# Modifico il valore associato alla chiave "eta"
persona["eta"] = 21  # Modifica il valore associato alla chiave "eta" a 21

# Aggiungo una nuova chiave-valore al dizionario
persona["hobby"] = "palestra"  # Aggiunge la chiave "hobby" e il valore "palestra" al dizionario

# Scorro il dizionario e stampo le coppie chiave-valore
for chiave, valore in persona.items():
    print(chiave, "→", valore)  # Stampa le coppie chiave-valore

# Stampo i valori associati alle chiavi nel dizionario persona
for chiave, valore in persona.items():
    print(chiave, "→", valore)  # Stampa le coppie chiave-valore

# Stampo i numeri da 0 a 9
for l in range(10):
    print(x)  # Stampa il numero corrente nella sequenza di numeri da 0 a 9

# Verifico se x è maggiore di y
p = 10
y = 20

if p > y:
    print("x è maggiore di y")  # Stampa questa stringa se x è maggiore di y
else:
    print("y è maggiore di x")  # Stampa questa stringa se y è maggiore di x
