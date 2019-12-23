nbval = int(input())
tempmin = int(input())
tempmax = int(input())
alerte = False
while not alerte and nbval != 0:
    x = int(input())
    if tempmin <= x <= tempmax :
        print('Rien à signaler')
        nbval -= 1
    else:
        print('Alerte !!')
        alerte = True
