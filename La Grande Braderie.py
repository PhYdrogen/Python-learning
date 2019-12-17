positionDepart = int(input(''))
largeurEmplacement= int(input(''))
nbVendeurs= int(input(''))
for i in range(nbVendeurs):
    print
    print(positionDepart + largeurEmplacement)
    positionDepart = positionDepart + largeurEmplacement
