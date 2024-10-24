# Auto luokka
class Auto:
    def __init__(self, rekkari, maxnopeus):
        self.rekkari = rekkari
        self.maxnopus = maxnopeus
        self.nopeus = 0
        self.kuljettumatka = 0

    def kiihdyta(self, kmh):
        if kmh + self.nopeus > 0 and kmh + self.nopeus < self.maxnopus:
            self.nopeus = self.nopeus + kmh
        elif kmh + self.nopeus < 0:
            self.nopeus = 0
        elif kmh + self.nopeus > self.maxnopus:
            self.nopeus = self.maxnopus


#Luodaan uusi auto
auto1 = Auto("ABC-123", 142)

#Kiihdytys
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

#Printataan auton ominaisuudet ja muistetaan yksiköt
print(f"Rekkari: {auto1.rekkari}")
print(f"Maximi nopeus: {auto1.maxnopus} km/h")
print(f"Tämänhetkinen nopeus: {auto1.nopeus} km/h")
print(f"Kuljettu matka: {auto1.kuljettumatka} km")

#Hätäjarrutus
auto1.kiihdyta(-200)
print("\nHätäjarrutus!")
print(f"Tämänhetkinen nopeus: {auto1.nopeus} km/h")