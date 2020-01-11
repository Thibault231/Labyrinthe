# coding: utf-8

import numpy as np
import pickle
from classes.classe_carte import *
from classes.classe_joueur import *




def regle_du_jeu():
    """ Affiche le message de bienvenue et contextualise le jeu."""
    print("Bienvenu dans LE LABYRINTHE. Vous vous réveillez au milieu d'un lieu inconnu.\n \
Votre objectif est de vous échapper. \n \
Vous êtes représenté par le symbole 'J' \n \
Tapez:\n N pour aller au nord,     S pour aller au sud, \n W pour aller à l'ouest,   \
E pour aller à l'est, \n Q pour quitter,           SS pour sauvegarder, \n H pour l'aide.\
            SOLUTION pour afficher la solution du labyrinthe. \n\n""")
    pass



def creation_carte_vierge():
    """ créé une carte de 15*15 case inconnues, symbolisées par '?'\
La carte servira de base à la construction de la classe Carte."""
    
    carte_vierge=np.full(shape=(15,15),fill_value=' ')
    return carte_vierge



def enregistrement(carte,joueur):
    """ Sauvegarde la carte et la position du joueur dans des fichier sur DESK"""
    pickle.dump(carte, open('sauvegardes/sauvegarde_labyrinthe1.txt', 'wb'))
    pickle.dump(joueur,open('sauvegardes/sauvegarde_labyrinthe2.txt', 'wb'))


def chargement(carte,joueur):
    """ Charge les données de carte et de position du joueur issues de la
    partie précédente, à partir des fichiers de sauvegarde du DESK"""
    carte= pickle.load(open('sauvegardes/sauvegarde_labyrinthe1.txt', 'rb'))
    joueur= pickle.load(open('sauvegardes/sauvegarde_labyrinthe2.txt', 'rb'))
    return carte,joueur


def choix_carte_demarrage(carte_vierge):
    """ Définit la carte et la position du joueur par défaut ou à partir d'un dossier de
    téléchargement"""
    i=0
    while i==0:
        reponse= input("Souhaitez vous reprendre votre dernière partie? \n O=oui  N=non\n \
==""")
        if reponse.lower()=="o":
            i+=1
            q1, q2= None, None
            carte, joueur=chargement(q1,q2)
        elif reponse.lower()=="n":
            i+=1
            carte=Carte(carte_vierge)
            joueur=Joueur()
                        
        else:
            print("Veuillez tapez O ou N")
            
    return carte, joueur

def mouvement_test(P_test,instruction):
    """ Simule les nouvelles coordonnées du joueur d'aprés les instruction de mouvement
    (n,s,e,w) entrées dans le clavier"""
    if instruction.lower()=="s":
        x,y=1,0
               
    elif instruction.lower()=="e":
        x,y=0,1
        
    elif instruction.lower()=="w":
        x,y=0,-1
                
    elif instruction.lower()=="n":
        x,y=-1,0
    else:
        x,y=0,0

    P_test[1]+=y
    P_test[0]+=x
    return P_test
