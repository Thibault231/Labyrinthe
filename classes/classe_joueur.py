class Joueur(list):
    """ Définit la classe du joueur par sa position"""

    def __init__(self):
        """ Initie la l'objet joueur n lui attribuant à l'origine les coordonnée x=8
        et y=8 sur le plan"""
        self.pos_ligne= 8 #x
        self.pos_colonne= 8 #y

    def position_joueur(self):
        """ renvoie les coordonnées du joueur sous forme de liste."""
        P=[self.pos_ligne, self.pos_colonne]
        return P

    def mouvement_j(self,x,y):
        """ Calcule les nouvelles coordonnées du joueur, suite aux instructions
        de mouvement x et y, données avec le clavier."""
        self.pos_ligne=self.pos_ligne+y
        self.pos_colonne=self.pos_colonne+x
        return self.pos_colonne, self.pos_ligne
