posTable = int(input())
change = int(input())
tableau = [0]*posTable
actualval = int()
for u in range(posTable):
    tableau[u] = int(input())
for i in range(change):
    x = int(input())
    y = int(input())
    actualval = tableau[y] 
    tableau[y] = tableau[x]
    tableau[x] = actualval
for i in range(len(tableau)):
    print(tableau[i]) 
