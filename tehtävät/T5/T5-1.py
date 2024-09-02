import random
die=int(input("Anna noppamäärä: \n"))
summa=0
for luku in range(die):
    luku = random.randint(1,6)
    summa=summa+luku
print(f"Noppien summa: {summa}")