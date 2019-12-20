paire = int(input())
for i in range(paire):
    xmin1 = int(input())
    xmax1 = int(input())
    ymin1 = int(input())
    ymax1 = int(input())
    xmin2 = int(input())
    xmax2 = int(input())
    ymin2 = int(input())
    ymax2 = int(input())

    if xmax1 <= xmin2: 
        print('NON')
    if xmax2 <= xmin1: 
        print('NON')
    if ymax1 <= ymin2: 
        print('NON')
    if ymax2 <= ymin1: 
        print('NON')
    else:
        print('OUI')
