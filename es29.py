input("ES 29")

input("Parte 1")

listcity = []
listmin = []
listmax = []
listprefiss = []
count1 = 0
ncity = int(input("Quante città prendiamo in considerazione? "))
vprefiss = int(input("qual è il valore prefissato per l'escursione termica? "))
while True:
    if count1 == ncity:
        break
    else:
        city = input("inserisci nome della città considerata: ")
        min = int(input("indica la sua temperatura minima: "))
        max = int(input("indica la sua temperatura massima: "))
        count1 = count1 + 1
        listcity.append(city)
        listmin.append(min)
        listmax.append(max)
        if max-min >= vprefiss:
            listprefiss.append(city)
print("in totale le città che hanno avuto un'escursione maggiore di", vprefiss, "gradi sono", len(listprefiss))

input("Parte 2")

listprefiss2 = []
count2 = 0
n2city = int(input("Quante città prendiamo in considerazione? "))
vprefiss2 = int(input("qual è il valore prefissato per l'escursione termica? "))
while True:
    if count2 == n2city:
        break
    else:
        city2 = input("inserisci nome della città considerata: ")
        min2 = int(input("indica la sua temperatura minima: "))
        max2 = int(input("indica la sua temperatura massima: "))
        count2 = count2 + 1
        print("L'escursione termica è di", max2-min2, "gradi a", city2)
        if max2-min2 >= vprefiss2:
            listprefiss2.append(city2)
            print("Attualmente", len(listprefiss2), "città hanno un'escursione termica maggiore di", vprefiss2)
print("Alla fine", len(listprefiss2), "città hanno un'escursione termica maggiore di", vprefiss2)