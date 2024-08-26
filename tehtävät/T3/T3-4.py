vuosi = int(input("Anna vuosi: \n"))

if vuosi%400 == 0:
    print("Ei ole karkausvuosi.")
elif vuosi%4 == 0:
    print("On karkausvuosi.")
else:
    print("Ei ole karkausvuosi.")