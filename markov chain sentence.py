import random as random
dico = ["Le","dev","chien","est","dit waf","fort","con","=)",".","hehe"]
lendico = int(len(dico))
def texte():
    texte.aleatoire = random.uniform(0.1,1.0)
    texte.resultat = [""]
    if texte.aleatoire > 0.5:
        texte.aleatoire = random.uniform(0.1,1.0)
        texte.resultat.append(dico[0])
        texte.resultat.append(dico[1])
        texte.resultat.append(dico[3])
        if texte.aleatoire >= 0.5:
            texte.resultat.append(dico[6])
        else:
            texte.aleatoire = random.uniform(0.1,1.0)
            texte.resultat.append(dico[5])
            if texte.aleatoire <= 0.3:
                texte.resultat.append(dico[7])
            elif 0.3 >= texte.aleatoire <= 0.6:
                texte.resultat.append(dico[8])
            else:
                texte.resultat.append(dico[9])
    elif texte.aleatoire <= 0.5:
        texte.resultat.append(dico[0])
        texte.resultat.append(dico[2])
        if texte.aleatoire <= 0.5:
            texte.resultat.append(dico[3])
            if texte.aleatoire >= 0.5:
                texte.resultat.append(dico[6])
            else:
                texte.aleatoire = random.uniform(0.1,1.0)
                texte.resultat.append(dico[5])
                if texte.aleatoire <= 0.3:
                    texte.resultat.append(dico[7])
                elif 0.3 <= texte.aleatoire <= 0.6:
                    texte.resultat.append(dico[8])
                else:
                    texte.resultat.append(dico[9])
        else:
            texte.resultat.append(dico[4])
    final = print(' '.join(texte.resultat[1:]))
    return final

texte()