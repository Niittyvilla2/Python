def parilliset(lista):
    kar_lista = []
    for luku in lista:
        if (luku%2) == 1:
            kar_lista.append(luku)
    for muut in kar_lista:
        lista.remove(muut)
    return lista
lista =[4, 6, 2, 57, 2, 8, 9]
print(parilliset(lista))