
class Cafe:
    def __init__(self, kaffe, tårta, muffins, kaka):
        self.pängar = 10
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

class Produkt:
    def __init__(self, namn="", pris=0, recept={}):
        self.namn = namn
        self.__mängd = 0
        self.pris = pris
        self.recept = recept

    