nbCharrettes = int(input())
poidsTableau = [0]*nbCharrettes
diffTableau = [0]*nbCharrettes
for i in range(nbCharrettes):
    poidsCharretes = float(input())
    poidsTableau[i] += poidsCharretes
moyennePoids = sum(poidsTableau)/nbCharrettes
for i in range(nbCharrettes):
    if poidsTableau[i] != moyennePoids:
        diffTableau[i] += moyennePoids - poidsTableau[i]
for i in range(nbCharrettes):
    print(diffTableau[i])
