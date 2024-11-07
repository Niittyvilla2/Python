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
        elif self.nykyinen_kerros > kohde_kerros:
            while self.nykyinen_kerros > kohde_kerros:
                self.kerros_alas()
        print("Olet perillä.")

    
    def kerros_ylos(self):
        self.nykyinen_kerros +=1
        print(f"Nykyinen kerros {self.nykyinen_kerros}")

    def kerros_alas(self):
        self.nykyinen_kerros -= 1
        print(f"Nykyinen kerros {self.nykyinen_kerros}")
    
hissi = Hissi(1, 9)
hissi.siirry_kerrokseen(1)
hissi.siirry_kerrokseen(7)
hissi.siirry_kerrokseen(9)
hissi.siirry_kerrokseen(9)
hissi.siirry_kerrokseen(10)
hissi.siirry_kerrokseen(1)