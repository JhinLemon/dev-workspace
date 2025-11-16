# creo una lista di frutta
frutta = ["mela", "banana", "ciliegia"]

# stampo il primo elemento della lista
print(frutta[0])

# aggiungo un elemento alla lista
frutta.append("pera")

# rimuovo un elemento dalla lista
frutta.remove("banana")

# stampo la lista
print(frutta)

# ritorna la lunghezza della lista
print(len(frutta))

# ordino la lista in ordine alfabetico
frutta.sort()

# inverto l'ordine della lista
frutta.reverse()

# inserisco un elemento alla posizione indicata
frutta.insert(1, "kiwi")

# rimuovo l'ultimo elemento della lista
frutta.pop()
numeri = [0, 1, 2, 3, 4, 5]
print(numeri[1:4])  # [1, 2, 3]

coordinate = (10, 20)
print(coordinate[0])  # 10
x, y = coordinate
print(x, y)  # 10 20

#utili per costanti o dati che non devono mai cambiare visto che le tuple sono immutabili

numeri = {1, 2, 3, 3, 2}
print(numeri)  # {1, 2, 3}
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # unione → {1, 2, 3, 4, 5}
print(a & b)  # intersezione → {3}
print(a - b)  # differenza → {1, 2}


persona = {
    "nome": "Marco",
    "età": 20,
    "città": "Padova"
}

print(persona["nome"])       # Marco
persona["età"] = 21          # modifica
persona["lavoro"] = "studente"  # aggiunge
print(persona)
persona.keys()    # restituisce tutte le chiavi
persona.values()  # restituisce tutti i valori
persona.items()   # coppie chiave-valore
