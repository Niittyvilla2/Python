import random

def noppa():
    luku = random.randint(1,6)
    return luku
numero = 0
while numero != 6:
    numero = noppa()
    print(numero)
