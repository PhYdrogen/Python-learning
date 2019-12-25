participant = int(input())
half = int(participant/2)
nbTabl = [0]*participant
for i in range(participant):
    x = int(input())
    nbTabl[i] = x
nbTabl.sort()
for i in range(half):
    print("{} {}".format(nbTabl[i],nbTabl[-i-1]))
