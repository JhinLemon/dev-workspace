class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni.")

p1 = Persona("Marco", 20)
p1.saluta()


class Studente(Persona):
    def __init__(self, nome, eta, corso):
        super().__init__(nome, eta)
        self.corso = corso

    def info(self):
        print(f"{self.nome} frequenta {self.corso}")

s2 = Studente("Giorgio", 22, "Informatica")
s2.info()



    # metodo con self
    # si riferisce all'istanza dell'oggetto
def info_self(self):
        print(f"Nome: {self.nome}, Eta': {self.eta}, Corso: {self.corso}")

    # metodo con cls
    # si riferisce alla classe in cui è definito
@classmethod
def info_cls(cls):
        print(f"Corso: {cls.corso}")

    # metodo con statico
    # si riferisce alla classe in cui è definito
@staticmethod
def info_statico():
        print("Questo è un metodo statico")






class Dipendente:
    aumento = 1.05

    def __init__(self, nome, stipendio):
        self.nome = nome
        self.stipendio = stipendio

    def applica_aumento(self):
        self.stipendio *= self.aumento

    @classmethod
    def imposta_aumento(cls, nuovo_aumento):
        cls.aumento = nuovo_aumento

    @staticmethod
    def is_weekday(giorno):
        return giorno.weekday() < 5

    @staticmethod
    def calcola_salario(giorni, ore):
        return giorni * (25 * ore)

Dipendente.imposta_aumento(1.10)
import datetime
print(Dipendente.is_weekday(datetime.date.today()))
print(Dipendente.calcola_salario(5, 8))
