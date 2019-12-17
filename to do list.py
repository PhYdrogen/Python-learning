from tkinter import *
liste = []
la_liste = list(enumerate(liste,0))
def afficher():
    return liste

def add():
    ajouter = input('que veux tu avoir ?\n')
    liste.append(ajouter)
    return ajouter + ' à été ajouter'

def modif():

    choix1 = input('que veux tu changer\n' '{}\n'.format(la_liste))
    if choix1 == 'rien':
        return
    choix2 = input('en quoi?\n')
    for i in range(len(liste)):
        if i == int(choix1):
            liste[i] = str(choix2)
            return 'update'
    return 'pas trouver'

def check(nom):
    liste.remove(nom)
    return


