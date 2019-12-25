maxi = int(input(''))
mini = int(input(''))
x = maxi
y = int()
for i in range(maxi-(mini-1)):
    x*x
    y += x*x
    x -= 1
print(y)
