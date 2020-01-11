class Carte():
    """ défini la carte qui sera affichée à l'écran
    Initialement la carte ne comprend que des zone marquée ?"""
    
    def __init__(self, carte0):
        """ Crée la carte d'origine à partir de la liste carte 0 remplie de ?"""
        self.carte=carte0

    def marque_joueur(self, pos_joueur, lettre):
        """ Position le joueur sur la carte d'aprés ses coordonnée. La lettre désirée est 
        inscrite aux coordonnée de la carte"""
        variable= list(self.carte[pos_joueur[0]-1])
        variable[pos_joueur[1]-1]= lettre
        self.carte[pos_joueur[0]-1]= list(variable)
        return self.carte

    def affichage_plan(self):
        """ Affiche l'Objet Carte comme une liste de 15 liste"""
        i=0
        while i < len(self.carte):
            print((self.carte[i]))
            i+=1

    def mouvement_c(self,x,y,P,joueur):
        """ Modifie la carte lorsque le joueur change de position.
        Les espaces visités qui ne sont pas des murs s'inscrive en " ".
        Le joueur apparaît avec la lettre J ."""
        P=joueur.position_joueur()
        self.marque_joueur(P, lettre=" ")    
        joueur.mouvement_j(y,x)
        P=joueur.position_joueur()
        self.marque_joueur(P, lettre="J")
        return self
