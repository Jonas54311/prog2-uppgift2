from random import choices

class Klass:
    def __init__(self, nr):
        self.nr = nr

    def ta_bort(self):
        lista.remove(self)

lista = [
    Klass(1),
    Klass(2),
    Klass(3)
]
lista[1].ta_bort()
for i in lista:
    print(i.nr)