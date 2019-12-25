abscmin = int(input())
abscmax = int(input())
ordmin = int(input())
ordmax = int(input())
compte = int()
maison = int(input())
for i in range(maison):
    maisonabs = int(input())
    maisonord = int(input())
    if abscmin <= maisonabs <= abscmax and ordmin <= maisonord <= ordmax:
        compte += 1
print(compte)
