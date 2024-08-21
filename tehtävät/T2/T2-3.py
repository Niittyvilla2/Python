
a_str = input("Anna suorakulmion kanta:\n")
b_str = input("Anna suorakulmion korkeus:\n")

# muuta jotta voi laskea
a = float(a_str)
b = float(b_str)

# laskut
pinta_ala = a*b
piiri = a*2+b*2

# prints
print("Pinta ala: " + str(pinta_ala))
print ("Piiri: "+ str(piiri))