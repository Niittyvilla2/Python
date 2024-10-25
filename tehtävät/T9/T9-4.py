import random
# Auto luokka
class Auto:
    def __init__(self, rekkari, maxnopeus):
        self.rekkari = rekkari
        self.maxnopus = maxnopeus
        self.nopeus = 0
        self.kuljettumatka = 0
        self.voittaja = False

    def kiihdyta(self, kmh):
        if kmh + self.nopeus > 0 and kmh + self.nopeus < self.maxnopus:
            self.nopeus = self.nopeus + kmh
        elif kmh + self.nopeus < 0:
            self.nopeus = 0
        elif kmh + self.nopeus > self.maxnopus:
            self.nopeus = self.maxnopus
    
    def kulje(self, aika):
        if aika > 0:
            matka = aika * self.nopeus
            self.kuljettumatka = self.kuljettumatka + matka
    
    def maalitarkastus(self):
        if self.kuljettumatka >= 10000:
            maalissa = 0
            self.voittaja = True
        return maalissa


#Autotttt


autot = []

for i in range(10):
    auto = Auto(f"ABC-")
#Kilpailu
maalissa = 0
while maalissa == 0:
    #Kiihdytys
    

