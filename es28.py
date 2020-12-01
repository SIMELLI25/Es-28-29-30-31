input("ES 28")

input("Con i dizionari")

dizionario = {}
nrag = int(input("quanti ragazzi partecipano?"))
count = 0
while True:
    if count == nrag:
        break
    else:
        rag = input("inserisci nome studente: ")
        lan = int(input("inserisci la misura del suo lancio: "))
        count = count + 1
        dizionario.update({lan : rag})
top = max(dizionario)
print("il punteggio migliore è", top)

input("Con le liste")

lanci = []
count = 1
cand_e_lan = []
while True:
    cand = input("inserisci nome candidato: ")
    lan = input("inserisci la misura del lancio: ")
    cand_e_lan.append(cand)
    cand_e_lan.append(lan)
    lanci.append(lan)
    count = count + 1
    x = int(input("se vuoi inserire altri candidato digita 1 altrimenti se termini qui digita 0: "))
    if x == 0:
        break
lanci.sort(reverse = True, key = int)
print("il vincitore è", cand_e_lan[cand_e_lan.index(lanci[0]) - 1], "con un lancio di", lanci[0], "metri")