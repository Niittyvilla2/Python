import random
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros > self.ylin or kohde_kerros < self.alin:
            print(f"Antamaasi kerrosta ei ole olemassa.")
            return
        if self.nykyinen_kerros < kohde_kerros:
            while self.nykyinen_kerros < kohde_kerros:
                self.kerros_ylos()
            print("Olet perillä.")
        elif self.nykyinen_kerros > kohde_kerros:
            while self.nykyinen_kerros > kohde_kerros:
                self.kerros_alas()
            print("Olet perillä.")
        else:
            print("Olet jo tässä kerroksessa")
    
    def kerros_ylos(self):
        self.nykyinen_kerros +=1
        print(f"Nykyinen kerros {self.nykyinen_kerros}")

    def kerros_alas(self):
        self.nykyinen_kerros -= 1
        print(f"Nykyinen kerros {self.nykyinen_kerros}")
    


class Talo:
    def __init__(self, alin, ylin, hissi_maara):
        self.ylin = ylin
        self.alin = alin
        self.hissit = []
        self.luo_hissi(hissi_maara)
        

    def luo_hissi(self, hissi_maara):
        for nro in range(hissi_maara):
            uus_hissi = Hissi(self.alin, self.ylin)
            self.hissit.append(uus_hissi)
        return
        
    def aja_hissia(self, hissinro, kohdekerros):
        hissi = self.hissit[hissinro -1]
        hissi.siirry_kerrokseen(kohdekerros)
    
    def palohalytys(self):
        print("Palohälytys!")
        for nro in range(hissit):
            hissi = self.hissit[nro]
            hissi.nykyinen_kerros = hissi.alin
            print(f"Hissi {nro + 1} päässyt kerrokseen {hissi.nykyinen_kerros}")
        print("Kaikki hissit alimmassa kerroksessa")

#tehdään talo
ylin = 8
alin = 1
hissit = 2
talo = Talo(alin, ylin, hissit)

#Palohälytystesti

#hissien käyttö hissin käyttöä ei voi lopettaa, joten olet hissilimbossa :)
kaytto = True
palohalytys = 0
while kaytto == True:
    hnro = int(input("Anna hissin numero: \n"))
    knro = int(input("Anna kerroksen numero: \n"))
    if hnro > 0 and hnro <= hissit:
        talo.aja_hissia(hnro, knro)
    else:
        print(f"Virheellinen hissin numero, hissien määrä on: {hissit}\n")
    palohalytys = random.randint(1,100)
    if palohalytys == 100:
        talo.palohalytys()