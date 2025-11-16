# SERVONO PER NON FAR INTERROMPERE IL PROGRAMMA

try:
    numero = int(input("Inserisci un numero: "))
    print(10 / numero)
except:
    print("Si è verificato un errore!")

#si possono gestire piu' eccezzioni assieme e alla fine si può utilizzare la sintassi finally

finally:
    print("Fine del programma")

    #finally viene usato per compiere azioni alla fine a prescindere dal risultato del programma

    eta = -5
if eta < 0:
    raise ValueError("L'età non può essere negativa!")

#raise viene usato per lanciare un'eccezione personalizzata

class EtàNonValida(Exception):
    pass

eta = -1
if eta < 0:
    raise EtàNonValida("Età non valida!")

# così si crea un'eccezione personalizzata
