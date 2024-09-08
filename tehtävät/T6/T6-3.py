def galloona(maara):
    litra = maara*3.785
    return litra

while True:
    maara = int(input("Anna galloona määrä: \n"))

    if maara<0:
        print("Anna parempi luku.")
        break

    else:
        print(galloona(maara))