from random import randint, choices, random, choice
from os import system

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
    def __init__(self, namn="", tålamod=0):
        self.namn = namn
        self.__tålamod = tålamod

    def få_beställning(self):
        for produkt in self.beställning:
            if produkt["mängd"] > produkt["objekt"].get_mängd():
                return False
        nuvarande_personer.remove(self)
        return True

    def sänk_tålamod(self):
        self.__tålamod -= 1
        nuvarande_personer.remove(self)
        
    def get_tålamod(self):
        return self.__tålamod

    def set_beställning(self):
        for produkt in choices(self.beställning.keys(), k=randint(self.beställningslängd["låg"], self.beställningslängd["hög"])):
            self.beställning[produkt] += 1

    def bli_utsparkad(self):
        nuvarande_personer.remove(self)

class Normal_person(Person):
    def __init__(self, namn="", tålamod=0):
        super().__init__(namn, tålamod)
        self.beställning = {
            "kaffe": {
                "mängd": 0,
                "objekt": cafe.produkter["kaffe"]
            },
            "tårta": {
                "mängd": 0,
                "objekt": cafe.produkter["tårta"]
            },
            "kaka": {
                "mängd": 0,
                "objekt": cafe.produkter["kaka"]
            },
            "muffins": {
                "mängd": 0,
                "objekt": cafe.produkter["muffins"]
            },
        }
        self.beställningslängd = {"låg": 1,
                                  "hög": 3}

class Hungrig_person(Person):
    def __init__(self, namn="", tålamod=0):
        super().__init__(namn, tålamod)

        self.beställning = {
            "kaffe": {
                "mängd": 0,
                "objekt": cafe.produkter["kaffe"]
            },
            "tårta": {
                "mängd": 0,
                "objekt": cafe.produkter["tårta"]
            },
            "kaka": {
                "mängd": 0,
                "objekt": cafe.produkter["kaka"]
            },
            "muffins": {
                "mängd": 0,
                "objekt": cafe.produkter["muffins"]
            },
        }
        self.beställningslängd = {"låg": 3,
                                  "hög": 6}

class Korkad_person(Person):
    def __init__(self, namn="", tålamod=0):
        super().__init__(namn, tålamod)
        self.beställning = {
            "mcmeal": {
                "mängd": 0,
                "objekt": fejk_produkter["mcmeal"]
            },
            "uh": {
                "mängd": 0,
                "objekt": fejk_produkter["uh"]
            },
            "kycklingvingar": {
                "mängd": 0,
                "objekt": fejk_produkter["kycklingvingar"]
            },
            "blinkarvätska": {
                "mängd": 0,
                "objekt": fejk_produkter["blinkarvätska"]
            },
        }
        self.beställningslängd = {"låg": 1,
                                  "hög": 5}

class Kaffeberoende_person(Person):
    def __init__(self, namn="", tålamod=0):
        super().__init__(namn, tålamod)
        self.beställning = {
            "kaffe": {
                "mängd": 0,
                "objekt": cafe.produkter["kaffe"]
            }
        }
        self.beställningslängd = {"låg": 2,
                                  "hög": 8}

class Marie_antoinette(Person):
    def __init__(self, namn="", tålamod=0):
        super().__init__(namn, tålamod)
        self.beställning = {
            "tårta": {
                "mängd": 0,
                "objekt": cafe.produkter["tårta"]
            }
        }
        self.beställningslängd = {"låg": 3,
                                  "hög": 6}

fejk_produkter = {
    "mcmeal": Produkt("McHappy McMeal"),
    "uh": Produkt("Uuuuuuuuhhh"),
    "kycklingvingar": Produkt("Kycklingvingar, medium rare"),
    "blinkarvätska": Produkt("Blinkarvätska")
}

cafe = Cafe(Produkt("kaffe", 10, {"kaffebönor": 5}), Produkt("tårta", 20, {"ägg": 4, "socker": 2, "mjöl": 1, "bakpulver": 1, "grädde": 2}), Produkt("muffins", 10, {"ägg": 2, "socker": 2, "mjöl": 3, "bakpulver": 2}), Produkt("kaka", 5, {"socker": 1, "ägg": 1, "mjöl": 2}))

persontyper = [
    Normal_person,
    Hungrig_person,
    Korkad_person,
    Kaffeberoende_person,
    Marie_antoinette
]

personvikter = [6, 5, 2, 3, 1]

nuvarande_personer = []

namn = [
    "Karl",
    "Erik",
    "Lars",
    "Anders",
    "Per",
    "Mikael",
    "Johan",
    "Olof",
    "Nils",
    "Jan",
    "Maria",
    "Elisabeth",
    "Anna",
    "Kristina",
    "Margareta",
    "Eva",
    "Linnea",
    "Karin",
    "Brigitta",
    "Marie"
]

while cafe.get_pengar() < 100000000000000000000:
    system("cls")
    if len(nuvarande_personer) < 3 and 1 / (len(nuvarande_personer) + 1) >= random():
        nuvarande_personer.append(choices(persontyper, weights=personvikter, k=1)(choice(namn), randint(3, 6)))
        nuvarande_personer[len(nuvarande_personer) - 1].set_beställning()

    for person in nuvarande_personer:
        print(person.namn, person.get_tålamod)
        for produkt in person.beställning.keys():
            print(produkt, person.beställning[produkt]["mängd"])
    print(cafe.get_pengar())
    for produkt in cafe.produkter:
        print(produkt.namn, produkt.get_mängd())
    for ingrediens in cafe.ingredienser.keys():
        print(ingrediens, cafe.ingredienser[ingrediens]["mängd"])
    input("")