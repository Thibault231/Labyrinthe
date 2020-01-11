import numpy as np
from cartes.plan_cartes_jeu import *
    
plan=plan_facile()
carte_vierge=np.full(shape=(15,15),fill_value=' ' )
        
for i in plan:
    print(i[0]-1,i[1]-1)
    carte_vierge[i[0]-1, i[1]-1]=0
print(np.array(carte_vierge))
