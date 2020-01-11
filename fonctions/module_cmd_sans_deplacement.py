# coding: utf-8

from pickle import *
import numpy as np
from fonctions.fonctions_labyrinthe import *
from fonctions.module_deplacements import *
from classes.classe_carte import *
from classes.classe_joueur import *
from cartes.plan_cartes_jeu import *




def module_commandes_annexes(var, i, carte_jeu, joueur):
    if var.lower()=="ss":
        enregistrement(carte_jeu, joueur)
        
    elif var.lower()=="q":
       i=1
       return i
        
    elif var.lower()=='h':
         print("Tapez:\n N pour aller au nord,     S pour aller au sud, \n W pour aller à l'ouest,   \
E pour aller à l'est, \n Q pour quitter,           SS pour sauvegarder, \n H pour l'aide.\
            SOLUTION pour afficher la solution du labyrinthe. \n\n""")
         
    elif var.lower()=='solution':
        plan=plan_facile()
        carte_vierge=np.full(shape=(15,15),fill_value=' ' )
        
        for i in plan:
            carte_vierge[i[0]-1, i[1]-1]=0

        print(np.array(carte_vierge))

    
