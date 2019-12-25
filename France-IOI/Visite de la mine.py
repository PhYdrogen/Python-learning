Mouv = int(input())
MouvTable = [0]*Mouv
for i in range(Mouv):
    MouvTable[i] = int(input())
    if MouvTable[i] == 1:
        MouvTable[i] = 2
    elif MouvTable[i] == 2:
        MouvTable[i] = 1
    elif MouvTable[i] == 3:
        MouvTable[i] = 3
    elif MouvTable[i] == 4:
        MouvTable[i] = 5
    elif MouvTable[i] == 5:
        MouvTable[i] = 4

for i in range(1,Mouv+1):
    print(MouvTable[-i])
