class klass1:
    def __init__(self, gteh):
        self.gteh = gteh

class klass2:
    def __init__(self, as=klass1(6)):
        self.asdfgd = as

objekt = klass2()
print(object.asdfgd.gteh)