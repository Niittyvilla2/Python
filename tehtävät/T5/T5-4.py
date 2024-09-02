kaupungit=[]
kaupunki=input("Anna yhteensö viisi kaupunkia, ensimmäinen kaupunki: \n")
kaupungit.append(kaupunki)
for kaupunki in range(4):
    kaupunki=input("Seuraava kaupunki: \n")
    kaupungit.append(kaupunki)
print("Tässä on kaupunkisi: \n")
for kaupunki in kaupungit:
    print(kaupunki)