luku=int(input("Anna kokonaisluku: \n"))
if luku>1:
    for i in range (2,(luku//2)+1):
        if (luku%i)==0:
            print(f"{luku} ei ole alkuluku")
            break
    else:
        print(f"{luku} on alkuluku")
else:
    print(f"{luku} ei ole alkuluku")