import pyxel, random

pyxel.init(128, 128, title="DM casse brique Elisa N")

balle_x = int(60)
balle_y = int(60)
balle_en_mouvement = False
balle_direction = int(0)

plateau_x = 48
plateau_y = 110

bloc = []
balle_liste = ([])

def plateau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_D):
        if (x < 105) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_Q):
        if (x > 0) :
            x = x - 1
    return x, y

def balle_creation(plateau_x, plateau_y):
    """création de la balle sur le plateau, par la touche shift de gauche """
    global balle_x
    global balle_y
    balle_x = plateau_x + 12
    balle_y = plateau_y - 12
    # btnr pour eviter les tirs multiples
    if pyxel.btnp(pyxel.KEY_LSHIFT, 2,30):
        pyxel.circ(balle_x,balle_y,2, 3)

def balle_deplacement():
    """déplacement de la balle vers le haut """
    global balle_y
    global balle_x
    global balle_en_mouvement
    if balle_en_mouvement == True:
        balle_y = balle_y - 1
    afficher_balle()
    if balle_y <= 0:
        balle_en_mouvement = False
        balle_x = plateau_x + 12
        balle_y = plateau_y - 12
       
def casserLaBrique():
    """casser la brique"""
    global bloc,balle_x,balle_y
#Un bloc de 4 lignes
    for m in range (0,4):
        ligne = bloc[m] #Une ligne de 14 briques
        
        for n in range (0,13):
            brique = ligne[n]  #une brique définie par x1,x2,y,présence(1)/abscence(0)
            if balle_x >= brique[1] and balle_x <= brique[2]:
                if balle_y <= brique[3]:
                    """brique touchee"""
                    brique[3] = 0
                    reDisplayBriques()
                    
def reDisplayBriques():           
    global bloc
    print('redisplayyyyyyyyyyyyyyyyyyy')
    for m in range(0,4):
        ligne = bloc[m]
        for n in range(0,13):
            brique = ligne[n]
            if brique[4] == 0:
                pyxel.rect(bloc[m][n][0],bloc[m][n][2],8,4,0)
            else:
                pyxel.rect(bloc[m][n][0],bloc[m][n][2],8,4,8)
            
            


def balle_lancement():
    """la balle est lancee en appuiant sur shift (de gauche)"""
    global balle_x
    global balle_y
    global balle_en_mouvement
    print('balle x avant if= ',balle_x)

    if pyxel.btn(pyxel.KEY_LSHIFT):
        print('xxx plateau x = ',plateau_x)
        print('xx1 balle x = ',balle_x)
        balle_x=plateau_x+12
        print('xx2 balle x = ',balle_x)
        balle_y=plateau_y
        print('balle y = ',balle_y)
        afficher_balle()
        balle_en_mouvement=True
        print('balle lanceeeeeee')
        
def afficher_balle():
    global balle_x
    global balle_y
    print('In afficher ++ balle_x =', balle_x)
    if balle_y > 0 and balle_x > 0:
        pyxel.circ(balle_x,balle_y, 2, 3)
        print('affichzr la balle')
    
def creer_brique():
    ligne1 = []
    for n in range (0,13):
        brique =[10+8*n,10+8*n+8,1]
        ligne1.append(brique)

def update():
    """mise à jour des variables (30 fois par seconde)"""

    global plateau_x, plateau_y
    print('Update')

    # mise à jour de la position du plateau
    plateau_x, plateau_y = plateau_deplacement(plateau_x, plateau_y)
    print('Inside Update Plqtequ x=',plateau_x)
    print('Inside Update Plqtequ y=',plateau_y)
     # mise a jour de la position de la balle
     
    
    # mise a jour lancement balle
    print('lancement')
    balle_lancement()
    print('deplacement')
    balle_deplacement()
    casserLaBrique()
    # mise a jour de la position de la balle 
#    balle_liste = balle_deplacement(balle_liste)


    
def draw():
    print('draw')
    
    """création des objets (30 fois par seconde)
    creer_brique()"""
    # vide la fenetre
    pyxel.cls(0)

    # plateau (carre 8x8)
    pyxel.rect(plateau_x, plateau_y, 24, 8, 1)
    pyxel.rect(plateau_x + 8, plateau_y - 8,8,8,1)
    pyxel.tri(plateau_x, plateau_y, plateau_x+8, plateau_y, plateau_x+8, plateau_y-8, 1)
    pyxel.tri(plateau_x+15, plateau_y, plateau_x+23, plateau_y, plateau_x+15, plateau_y-8,1)
    
    #balle (rayon 2)
    #pyxel.circ(plateau_x + 12, plateau_y - 12, 2, 3)    
#    for balle in balle_liste:
#         pyxel.circ(balle_x , balle_y , 2, 3)

#    for n in range(0,13):
#            #brique de base (brique_1)
#            pyxel.rect(10+8*n,15,8,4,8)
#            pyxel.rect(10+8*n,15,1,4,0)

    global bloc,ligne

    #Un bloc de 4 lignes
    for m in range (0,4):
        ligne = [] #Une ligne de 14 briques
        
        for n in range (0,13):
            brique = [10*n,10*n+8,15+m*5,1]  #une brique définie par x1,x2,y,présence(1)/abscence(0)
            ligne.append(brique)
        bloc.append(ligne)
    
    for m in range(0,4):
        for n in range(0,13):
            pyxel.rect(bloc[m][n][0],bloc[m][n][2],8,4,8)
           
pyxel.run(draw, update)        
