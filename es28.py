input("ES 28")
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
