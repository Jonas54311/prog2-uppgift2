class Superklass:
    def metod(self):
        print(self.value)

class Subklass(Superklass):
    def __init__(self):
        self.value = 0

o = Subklass()
o.metod()