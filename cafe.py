from random import randint

class Cafe:
    def __init__(self, kaffe, tårta, muffins, kaka):
        self.__pengar = 10
        self.ingredienser = {
            "kaffebönor": {
                "mängd": 0,
                "pris": 0
            },
            "mjöl": {
                "mängd": 0,
                "pris": 0
            },
            "socker": {
                "mängd": 0,
                "pris": 0
            },
            "ägg": {
                "mängd": 0,
                "pris": 0
            },
            "bakpulver": {
                "mängd": 0,
                "pris": 0
            },
            "grädde": {
                "mängd": 0,
                "pris": 0
            },
        }
        self.produkter = {
            "kaffe": kaffe,
            "tårta": tårta,
            "muffins": muffins,
            "kaka": kaka
        }

    def köp_ingredienser(self, ingrediens, mängd):
        if self.ingredienser[ingrediens]["pris"] * mängd <= self.__pengar:
            self.ingredienser[ingrediens]["mängd"] += mängd
            self.__pengar -= self.ingredienser[ingrediens]["pris"] * mängd
            return True
        return False

    def höj_pengar(self, mängd):
        if self.__pengar >= mängd:
            self.__pengar -= mängd
            return True
        return False

    def get_pengar(self):
        return self.__pengar

class Produkt:
    def __init__(self, namn="", pris=0, recept={}):
        self.namn = namn
        self.__mängd = 0
        self.pris = pris
        self.recept = recept

    def skapa_produkt(self, mängd):
        for ingrediens in self.recept.keys():
            if self.recept[ingrediens] * mängd > cafe.ingredienser[ingrediens]["mängd"]:
                return False
        self.__mängd += mängd
        for ingrediens in self.recept.keys():
            cafe.ingredienser[ingrediens][mängd] -= self.recept[ingrediens] * mängd

    def sänk_mängd(self, mängd):
        if self.__mängd >= mängd:
            self.__mängd -= mängd
            return True
        return False

    def get_mängd(self):
        return self.__mängd

class Person:
    def __init__(self, namn=""):
        self.namn = namn
        self.__tålamod = 0

    #få_beställning

    def sänk_tålamod(self):
        self.__tålamod -= 1
        #kåd för då tålamod blir 0

    def set_tålamod(self):
        self.__tålamod = randint(3, 5)
        
    def get_tålamod(self):
        return self.__tålamod

    #sparka_ut()

class Normal_person(Person):
    def __init__(self, namn=""):
        super().__init__(namn)

cafe = Cafe()