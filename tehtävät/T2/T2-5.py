
# painot
luoti = float(13.3)
naula = float(32*luoti)
leiviska = float(20*naula)

luoti_kpl_str = input("Anna luotien määrä: \n")
naula_kpl_str = input("Anna naulojen määrä: \n")
leiviska_kpl_str = input("Anna leivisköjen määrä: \n")

# muutetaan määrät numeroiksi
A = float(luoti_kpl_str)
B = float(naula_kpl_str)
C = float(leiviska_kpl_str)

# lasketaan
paino = ((A*luoti)+(B*naula)+(C*leiviska))
g = (paino%1000)
kg = ((paino - g)/1000)

print ("Massa kilogrammoina ja grammoina: ")
print(f"{kg:.0f} kilogrammaa ja {g:.2f} grammaa")

