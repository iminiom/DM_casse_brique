import pyxel, random

pyxel.init(128, 128, title="DM casse brique Elisa N")

plateau_x = 48
plateau_y = 110

            
def plateau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_D):
        if (x < 105) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_Q):
        if (x > 0) :
            x = x - 1
    return x, y


def lancement_balle_initial(x, y):
    """au début de la partie, l'angle de lancé de la balle est alléatoire"""

def update():
    """mise à jour des variables (30 fois par seconde)"""

    global plateau_x, plateau_y

    # mise à jour de la position du plateau
    plateau_x, plateau_y = plateau_deplacement(plateau_x, plateau_y)

    
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # plateau (carre 8x8)
    pyxel.rect(plateau_x, plateau_y, 24, 8, 1)
    pyxel.rect(plateau_x + 8, plateau_y - 8,8,8,1)
    pyxel.tri(plateau_x, plateau_y, plateau_x+8, plateau_y, plateau_x+8, plateau_y-8, 1)
    pyxel.tri(plateau_x+15, plateau_y, plateau_x+23, plateau_y, plateau_x+15, plateau_y-8,1)
    
    #balle (rayon 4)
    pyxel.circ(plateau_x +12, plateau_y -12, 2, 3)

    for n in range(0,13):
            #brique de base (brique_1)
            pyxel.rect(10+8*n,15,8,4,8)
            pyxel.rect(10+8*n,15,1,4,0)
        
    for n in range(0,13):    
            #brique de base (brique_2)
            pyxel.rect(10+8*n,20,8,4,9)
            pyxel.rect(10+8*n,20,1,4,0)
            
    for n in range(0,13):
            #brique de base (brique_1)
            pyxel.rect(10+8*n,25,8,4,8)
            pyxel.rect(10+8*n,25,1,4,0)

    for n in range(0,13):    
            #brique de base (brique_2)
            pyxel.rect(10+8*n,30,8,4,9)
            pyxel.rect(10+8*n,30,1,4,0)
            
    for n in range(0,13):
            #brique de base (brique_1)
            pyxel.rect(10+8*n,35,8,4,8)
            pyxel.rect(10+8*n,35,1,4,0)
            
pyxel.run(update, draw)        
