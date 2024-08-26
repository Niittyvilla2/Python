b_s = input("Biologinen sukupuoli(M/F): \n")
ha = int(input("Hemoglobiiniarvo numerona: \n"))
if b_s == "M" and ha>=134 and ha<=195:
    print("Normaali hemoglobiiniarvo")
if b_s =="M" and ha<134:
    print("Hemoglobiiniarvo on alhainen")
if b_s =="M" and ha>195:
    print("Hemoglobiiniarvo on korkea")
if b_s == "F" and ha>=117 and ha<=175:
    print("Normaali hemoglobiiniarvo")
if b_s == "F" and ha<117:
    print("Hemoglobiiniarvo on alhainen")
if b_s == "F" and ha>175:
    print("Hemoglobiiniarvo on korkea")