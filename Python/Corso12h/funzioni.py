def somma_totale(*numeri):
    return sum(numeri)

print(somma_totale(1, 2, 3, 4))  # 10

# *args raccoglie argomenti posizionali in una tupla.
# **kwargs raccoglie argomenti con nome in un dizionario:

def mostra_info(**persona):
    for chiave, valore in persona.items():
        print(chiave, "→", valore)

mostra_info(nome="Marco", età=20, città="Padova")


#SCOPE 

def esempio():
    x = 5  # locale
    print(x)

esempio()
# print(x)  # Errore: x non esiste qui

x = 10
def modifica():
    global x
    x = 20

modifica()
print(x)  # 20


quadrato = lambda x: x**2
print(quadrato(5))  # 25
numeri = [1, 2, 3, 4, 5]
doppi = list(map(lambda x: x*2, numeri))
print(doppi)  # [2, 4, 6, 8, 10]

# si possono utilizzare insieme a funzioni come map() o filter():