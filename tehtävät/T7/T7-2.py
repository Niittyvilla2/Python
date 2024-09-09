nimet = set()

nimi= (input("Anna nimi: \n"))
print("Uusi nimi.\n")
nimet.add(nimi)

while nimi!= "":
    nimi= (input("Anna nimi: \n"))
    if nimi== nimi in nimet and nimi!="": 
        print("Aiemmin syötetty nimi.\n")
    elif nimi== "":
        break
    else:
        print("Uusi nimi \n")
    nimet.add(nimi)

for nimi in nimet:
    print(nimi)