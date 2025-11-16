import os

# Controlliamo se il file "testo.txt" esiste
if not os.path.isfile("testo.txt"):
    print("Il file 'testo.txt' non esiste.")
    exit()

# Apriamo il file "testo.txt" in modalità di lettura (r)
with open("testo.txt", "r") as file:
    # Leggiamo il contenuto del file e lo memorizziamo nella variabile "contenuto"
    contenuto = file.read()
    # Stampiamo il contenuto letto dal file
    print(contenuto)

# Controlliamo se la directory di destinazione esiste
if not os.path.isdir("output"):
    print("La directory 'output' non esiste.")
    exit()

# Apriamo il file "output/output.txt" in modalità di scrittura (w)
with open("output/output.txt", "w") as file:
    # Scriviamo il testo "Ciao dal file!" nel file
    file.write("Ciao dal file!\n")

# Controlliamo se il file "immagine.jpg" esiste
if not os.path.isfile("immagine.jpg"):
    print("Il file 'immagine.jpg' non esiste.")
    exit()

# Apriamo il file "immagine.jpg" in modalità binaria di lettura (rb)
with open("immagine.jpg", "rb") as file:
    # Leggiamo il contenuto del file e lo memorizziamo nella variabile "dati"
    dati = file.read()
