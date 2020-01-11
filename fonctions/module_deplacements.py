from fonctions.fonctions_labyrinthe import *
from classes.classe_carte import *
from classes.classe_joueur import *
from cartes.plan_cartes_jeu import *



def deplacement_autorise(carte_jeu, P, joueur, instruction):
    """ Détermine les modification des coordonnées du joueur et de la carte_jeu \
pour les commandes (n,s,e,w) d'aprés les coordonnées du joueur non simulées."""       
            
    if instruction.lower()=="s":
        carte_jeu.mouvement_c(1,0,P,joueur)
        P=joueur.position_joueur()
        carte_jeu.affichage_plan()       
        
    elif instruction.lower()=="e":
        carte_jeu.mouvement_c(0,1,P,joueur)
        P=joueur.position_joueur()
        carte_jeu.affichage_plan()
        
    elif instruction.lower()=="w":
        carte_jeu.mouvement_c(0,-1,P,joueur)
        P=joueur.position_joueur()
        carte_jeu.affichage_plan()
        
    elif instruction.lower()=="n":
        carte_jeu.mouvement_c(-1,0,P,joueur)
        P=joueur.position_joueur()
        carte_jeu.affichage_plan()
                
    else:
        print("Cette action n'existe pas.")
    
    return carte_jeu, P, joueur


def module_sans_mouvement(instruction):
    """ définit les actions à réaliser en cas d'entrée non liées au mouvement"""
    if instruction.lower()=="ss":
        enregistrement(carte_jeu, joueur)
        
    elif instruction.lower()=="h":
        print("Tapez: \n N pour aller au nord,\n S pour aller au sud, \n W pour aller à l'ouest, \n \
E pour aller à l'est, \n Q pour quitter, \n SS pour sauvegarder, \n H pour l'aide.")
