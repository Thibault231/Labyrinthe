# coding: utf-8

# importation de modules
import os
from pickle import *
from tkinter import messagebox as tk
from fonctions.fonctions_labyrinthe import *
from fonctions.module_deplacements import *
from fonctions.module_cmd_sans_deplacement import *
from classes.classe_carte import *
from classes.classe_joueur import *
from cartes.plan_cartes_jeu import *


                                                    #variables
joueur= type(Joueur)
P=[]
plan_labyrinthe=plan_facile() 
carte_vierge=creation_carte_vierge()
carte_jeu= type(Carte)


        

                                                       #script
regle_du_jeu()
carte_jeu, joueur=choix_carte_demarrage(carte_vierge)
P=joueur.position_joueur()
carte_jeu.marque_joueur(P,"J")
carte_jeu.affichage_plan()
i=0

while (P!= plan_labyrinthe[-1]) and (i!=1):
        
    instruction=input("\nTapez H pour aide. \n   Que souhaitez vous faire?=")
    P_test=list(P)
    P_test=mouvement_test(P_test,instruction)

    if instruction.lower() in ["q","h","ss","solution"]:
        i=module_commandes_annexes(instruction, i, carte_jeu, joueur)

    elif (P_test in plan_labyrinthe)==True:
        print("lecture blok mouvement")
        P=list(P_test)
        carte_jeu, P, joueur=deplacement_autorise(carte_jeu, P, joueur, instruction)
            
    else:
        print("Vous bloquez contre un mur")
        carte_jeu.marque_joueur(P_test, 'X')
        carte_jeu.affichage_plan()                     

if P== plan_labyrinthe[-1]:
    print("\nFélicitation vous êtes sorti du labyrinthe!!!")

print("\n\nAurevoir. \n     Merci et à bientôt.")
    
os.system("pause")


