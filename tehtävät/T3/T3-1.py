pituus = float(input("Anna kuhan pituus senttimetreinä: \n"))
if pituus<37:
    mitta = 37-pituus
    print("Kuha on alamittainen, päästä kuha takaisin järveen, kuha on " + str(mitta) + " senttimetriä liian lyhyt.")
else:
    print("Kuha on tarpeeksi iso!")