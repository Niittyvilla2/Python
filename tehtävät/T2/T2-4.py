
print("Anna kolme numeroa")
A_str = input("Anna ensimmäinen numero:\n")
B_str = input("Anna toinen numero:\n")
C_str = input("Anna kolmas numero:\n")

# muuta laskuja varen
A = float(A_str)
B = float(B_str)
C = float(C_str)

# laskut
summa = (A+B+C)
tulo = (A*B*C)
keskiarvo = ((A+B+C)/3)

# printit
print("Summa: " + str(summa))
print("Tulo: " + str(tulo))
print("Keskiarvo: " + str(keskiarvo))