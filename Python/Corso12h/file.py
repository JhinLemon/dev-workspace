
import os   

file = open("testo.txt", "r")  # "r" = read (lettura)
contenuto = file.read()
print(contenuto)
file.close()

#si può utilizzare with per aprire e chiudere il file automaticamente
with open("testo.txt", "r") as file:
    contenuto = file.read()
    print(contenuto)

print(os.getcwd()) #molto molto utile per vedere dove va a prendere il file

file = open("output.txt", "w")
file.write("Ciao mondo!\n")
file.write("Python è fantastico.")
file.close()


# Per creare e scrivere un file csv 

import csv

with open("studenti.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Nome", "Età"])
    writer.writerow(["Marco", 20])

    with open("studenti.csv") as f:
        reader = csv.reader(f)
        for riga in reader:
            print(riga)



# Per creare e scrivere un file json

import json

dati = {"nome": "Marco", "età": 20, "linguaggi": ["Python", "JavaScript"]}

with open("dati.json", "w") as f:
    json.dump(dati, f)

with open("dati.json") as f:
    dati = json.load(f)
    print(dati)



