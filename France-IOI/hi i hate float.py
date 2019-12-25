from  math import ceil,floor

taxe = float(input()) / 100
nouvelle = float(input()) / 100
prix = float(input())
P1 = prix / (1+taxe)
P2 = P1*nouvelle

print(round(P1 + P2,2))
