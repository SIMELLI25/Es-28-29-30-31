input("ES 31")

listresto = []
listcfr = []
count = -1
ndec = int(input("Inserisci il numero decimale: "))
while True:
    if ndec == 0:
        break
    else:
        resto = ndec % 2
        ndec = ndec // 2
        listresto.append(resto)
listresto.reverse()
totresti = len(listresto)-1
while True:
    pot = pow(10, totresti)
    cfr = listresto[count+1]*pot
    totresti = totresti - 1
    count = count + 1
    listcfr.append(cfr)
    if totresti == -1:
        break
print("il numero decimale", ndec, "è il numero binario", sum(listcfr))