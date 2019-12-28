entre = input().split()
prenom1 = entre[0]
prenom2 = entre[1]
foo = []
flo = []
for i in range(len(prenom1)):
    foo.append(ord(prenom1[i]) - ord("A"))
for i in range(len(prenom2)):
    flo.append(ord(prenom2[i]) - ord("A"))

calc2 = int(sum(flo))
calc = int(sum(foo))

while calc > 9:
    calc = str(calc)
    calc1 = []
    for i in range(len(calc)):
        calc1.append(int(calc[i]))
    calc = sum(calc1)

while calc2 > 9:
    calc2 = str(calc2)
    calc3 = []
    for i in range(len(calc2)):
        calc3.append(int(calc2[i]))
    calc2 = sum(calc3)

print("{} {}".format(calc,calc2))
