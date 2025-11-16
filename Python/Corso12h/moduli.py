# Moduli
# Moduli in Python sono dei file contenenti codice Python che è possibile utilizzare in altri file.
# Per creare un modulo personalizzato, basta creare un file con estensione .py e scrivere il codice che lo compone.

# Ad esempio, creiamo un modulo chiamato "mio_modulo.py" con il seguente contenuto:

def saluto(nome):
    """
    Funzione che restituisce un saluto personalizzato.

    Parametri:
    nome (str): il nome da salutare.

    Restituisce:
    str: un saluto personalizzato.
    """
    return f"Ciao {nome}!"

def somma(a, b):
    """
    Funzione che restituisce la somma di due numeri.

    Parametri:
    a (int): il primo numero da sommare.
    b (int): il secondo numero da sommare.

    Restituisce:
    int: la somma tra a e b.
    """
    return a + b


# Possiamo quindi utilizzare questo modulo in un altro file Python, importandolo con il comando import e utilizzando le funzioni definite nel modulo.
# Ad esempio, creiamo un file "main.py" con il seguente contenuto:

import mio_modulo

# Utilizziamo la funzione saluto definita nel modulo mio_modulo
print(mio_modulo.saluto("Marco")) # Stampa "Ciao Marco!"

# Utilizziamo la funzione somma definita nel modulo mio_modulo
print(mio_modulo.somma(5, 3))  # Stampa 8

# Possiamo anche importare una sola funzione dal modulo utilizzando il comando from:
from mio_modulo import saluto

# Utilizziamo la funzione saluto importata definita nel modulo mio_modulo
print(saluto("Marco")) # Stampa "Ciao Marco!"

# Infine, possiamo anche rinominare una funzione importata utilizzando il comando as:
from mio_modulo import somma as somma_numeri

# Utilizziamo la funzione somma_numeri importata definita nel modulo mio_modulo
print(somma_numeri(5, 3))  # Stampa 8

# Organizzazione dei file

# Esempio di struttura di file:

# Studio/Python/Corso12h/
# ├── main.py
# └── mio_modulo.py
#
# In questo esempio, il file "main.py" è il file principale che contiene il codice principale per l'applicazione.
# Il file "mio_modulo.py" è un modulo che contiene funzioni utili per l'applicazione.
# I file dei moduli possono essere posizionati in una cartella separata, come ad esempio la cartella "Corso12h" nell'esempio sopra.

# per installare librerie esterne
pip install requests #nome simbolico 
import requests

r = requests.get("https://api.github.com")
print(r.status_code)
