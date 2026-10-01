from random import randint, choices

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

    def set_beställning(self):
        for produkt in choices(self.beställning.keys(), k=randint(self.beställningslängd["låg"], self.beställningslängd["hög"])):
            self.beställning[produkt] += 1

    #sparka_ut()

class Normal_person(Person):
    def __init__(self, namn=""):
        super().__init__(namn)
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
    def __init__(self, namn=""):
        super().__init__(namn)

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
    def __init__(self, namn=""):
        super().__init__(namn)
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
    def __init__(self, namn=""):
        super().__init__(namn)
        self.beställning = {
            "kaffe": {
                "mängd": 0,
                "objekt": cafe.produkter["kaffe"]
            }
        }
        self.beställningslängd = {"låg": 2,
                                  "hög": 8}

class Marie_antoinette(Person):
    def __init__(self, namn=""):
        super().__init__(namn)
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

cafe = Cafe(Produkt("kaffe", 10, {"kaffebönor": 5}), Produkt("tårta", 30, {}))