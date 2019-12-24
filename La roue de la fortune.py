nbZones = int(input())
resultat = int()
if nbZones > 23:
    resultat = nbZones % 24
if nbZones < 0:
    resultat = nbZones % 24
if nbZones == 23:
   resultat = nbZones
print(resultat)

"""
Ce qu'il m'a aider c'est ça
In [3]: for nbZones in range(20, 30):
   ...:      print(f"{nbZones} // 24 = {nbZones // 24}")
   ...:      print(f"{nbZones}  % 24 = {nbZones % 24}")
   ...:                                                                                                                      
20 // 24 = 0
20  % 24 = 20
21 // 24 = 0
21  % 24 = 21
22 // 24 = 0
22  % 24 = 22
23 // 24 = 0
23  % 24 = 23
24 // 24 = 1
24  % 24 = 0
25 // 24 = 1
25  % 24 = 1
26 // 24 = 1
26  % 24 = 2
27 // 24 = 1
27  % 24 = 3
28 // 24 = 1
28  % 24 = 4
29 // 24 = 1
29  % 24 = 5
"""
