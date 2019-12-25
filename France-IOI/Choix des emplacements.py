nbEmplacements = int(input())
tableau = [0]*nbEmplacements

for i in range(nbEmplacements):
    x = int(input())
    tableau[x]= i
for i in range(nbEmplacements):
    print(tableau[i])
