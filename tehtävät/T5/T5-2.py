luvut=[]
luku=input("Anna luku: \n")
while luku!="":
    luvut.append(luku)
    luku=input("Anna luku tai paina enter lopettaaksesi: \n")
luvut.sort(reverse=True)
for luku in range(5,0,-1):
    print(luku)
