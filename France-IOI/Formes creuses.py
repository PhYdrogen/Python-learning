def ligne(nb):
    print("X" * nb)
    print()
def rectangle(nb1,nb2):
    for j in range(nb1):
        if j == 0 or j == nb1-1:
            print("#" * nb2)
        elif nb2 == 1:
            print("#")
        else:
            print("#" + " " * (nb2-2) + "#")
    print()
def triangle(nb):
    for i in range(nb):
        if i > 1 and i < nb-1:
            print("@" + " " * (i-1) + "@")
        elif i <= 1 or i == nb-1:
            print("@" * (i+1))
    print()
llin = int(input())
linn = int(input())
col = int(input())
tri = int(input())
ligne(llin)
rectangle(linn,col)
triangle(tri)
