input("ES 30")

count = 1
listprod = []
due = 2
ncifre = int(input("Da quante cifre è composto il numero binario?"))
print("inserisci la cifra corrispondente (0 oppure 1) partendo da destra")
cifra = int(input("inserisci 0 oppure 1: "))
if cifra == 1:
    prod = cifra
    listprod.append(prod)
while True:
    if count == ncifre:
        break
    else:
        print("inserisci la cifra corrispondente (0 oppure 1) partendo da destra")
        cifra = int(input("inserisci 0 oppure 1: "))
        count = count + 1
        if cifra == 1:
            prod = cifra*due
            listprod.append(prod)
        due = due*2
print("il numero decimale è", sum(listprod))