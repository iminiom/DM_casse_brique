import pyxel, random

pyxel.init(128, 128, title="DM casse brique Elisa N")

balle_x = int(60)
balle_y = int(60)
balle_en_mouvement = False
direction_x=0
direction_y=-1

plateau_x = 48
plateau_y = 110

balle_deplacement_vertical =  1
balle_deplacement_horizontal = random.randint(-5,5)

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
"""
def balle_creation(plateau_x, plateau_y):
    création de la balle sur le plateau, par la touche shift de gauche
    global balle_x
    global balle_y
    balle_x = plateau_x + 12
    balle_y = plateau_y - 12
"""    
def casserLaBrique():
    """casser la brique"""
    global bloc,balle_x,balle_y
    cassee=False
    #Un bloc de 4 lignes
    for m in range (0,4):
        ligne = bloc[m] #Une ligne de 13 briques
        for n in range (0,13):
            brique = ligne[n]  #une brique définie par x1,x2,y,type de brique, vies 
            if balle_x+1 >= brique[0] and balle_x-1 <= brique[1]:
                
                if balle_y <= brique[2]:
                    """brique touchee"""
                    if brique [3] == 'normale':
                        brique[3] = 'cassee'
                        brique[4] = 0 			#nombre de vies restantes (0)
                        reDisplayBriques()
                        cassee = True
                    else:
                        if brique [3] == 'a vies':
                            print('brique a vies avant',brique)
                            brique [4] = brique [4] - 1 #retirer une vie
                            if brique [4] == 1: #si plus que une vie passer en brique normale
                                brique [3] = 'normale'
                                reDisplayBriques()
                            cassee = True
                            print('brique a vies APRES',brique)
    if cassee == True:
        rebondir()
def reDisplayBriques():           
    global bloc
    for m in range(0,4):
        ligne = bloc[m]
        for n in range(0,13):
            brique = ligne[n]
            coleur = coleur_brique(brique[3], brique[4])
            pyxel.rect(bloc[m][n][0],bloc[m][n][2],8,4,coleur)
            
def balle_lancement():
    """la balle est lancee en appuiant sur shift (de gauche)"""
    global balle_x
    global balle_y
    global balle_en_mouvement
    if balle_en_mouvement == False:
        if pyxel.btn(pyxel.KEY_LSHIFT):
            balle_x=plateau_x+12
            balle_y=plateau_y
            afficher_balle()
            balle_en_mouvement=True

def afficher_balle():
    global balle_x
    global balle_y
    if balle_y > 0 and balle_x > 0:
        pyxel.circ(balle_x,balle_y, 2, 3)

def balle_deplacement():
    global balle_x, balle_y, balle_en_mouvement, direction_x, direction_y
    if balle_en_mouvement == True:
        balle_x = balle_x + direction_x
        balle_y = balle_y + direction_y
        afficher_balle()
    #rebondir sur le bords
    if balle_x <=0 or balle_x >= 120 or balle_y <=0:
        rebondir()
    #balle perdue
    if balle_y >=120:
        balle_en_mouvement = False
        direction_x = 0
        direction_y = -1
        balle_x = 60
        balle_y = 60
        
def rebondir():
    global direction_x, direction_y
    if direction_x != 0:
        direction_x = -1 * direction_x
    if direction_y != 0:
        direction_y = -1 * direction_y
    

def creer_brique():
    ligne1 = []
    for n in range (0,13):
        brique =[10+8*n,10+8*n+8,1] #
        ligne1.append(brique)

def creer_bloc():
    global bloc
    
    #Une ligne de briques normales
    ligne1 = [] #Une ligne de 13 briques normales
    for n1 in range (0,13):
        brique = [10*n1,10*n1+8,15,'normale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
        ligne1.append(brique)
    bloc.append(ligne1)
    
    ligne2 = [] #Une ligne de 13 briques a 3 vies
    for n2 in range (0,13):
        brique = [10*n2,10*n2+8,20,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
        ligne2.append(brique)
    bloc.append(ligne2)
    
    ligne3 = [] #Une ligne de 13 briques a 3 vies
    for n3 in range (0,13):
        brique = [10*n3,10*n3+8,25,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
        ligne3.append(brique)
    bloc.append(ligne3)
    
    ligne4 = [] #Une ligne de 13 briques
    for n4 in range (0,13):
        brique = [10*n4,10*n4+8,30,'normale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
        ligne4.append(brique)
    bloc.append(ligne4)
       
    print(bloc)
    for m in range(0,3):
        for n in range(0,13):
            coleur = coleur_brique(bloc[m][n][3],bloc[m][n][4])
            pyxel.rect(bloc[m][n][0],bloc[m][n][2],8,4,coleur)
            
    print (bloc)
    return bloc            

def coleur_brique(type_de_brique, nombre_de_vies):
    coleur = 8
    if type_de_brique == 'cassee':
        coleur = 0
        return coleur
    
    if type_de_brique == 'a vies':
        if nombre_de_vies == 3:
            coleur = 7
        if nombre_de_vies == 2:
            coleur = 6
        if nombre_de_vies == 1:
            """1 vie = brique normale"""
            coleur = 8 
        return coleur

    if type_de_brique == 'incassable':
        coleur = 5
        return coleur
    return coleur

def update():
    """mise à jour des variables (30 fois par seconde)"""

    global plateau_x, plateau_y, balle_x, balle_y
    global balle_deplacement_vertical, balle_deplacement_horizontal

    # mise à jour de la position du plateau
    plateau_x, plateau_y = plateau_deplacement(plateau_x, plateau_y)
    
    # mise a jour lancement balle
    balle_lancement()
    balle_deplacement()
    casserLaBrique()
    #reDisplayBriques()
    # mise a jour de la position de la balle 
      
    #balle_liste = balle_deplacement(balle_liste)
    
"""   
    balle_y = balle_y + balle_deplacement_vertical 
    balle_x = balle_x + balle_deplacement_horizontal

    balle_deplacement_vertical = balle_deplacement_vertical 
    balle_depalcement_horizontal = balle_deplacement_horizontal 
"""    

"""
    #sortie de plateau
    if balle_x >= 256 : 
        balle_deplacement_horizontal = -1
        
        
    if balle_x <= 0 : 
        balle_deplacement_horizontal = 1 
    
    if balle_y >= 256 :
        balle_y =int(60)
        balle_x =int(60)
        balle_deplacement_horizontal = random.randint(-5,5)

        
    if balle_y <= 0 :
        balle_deplacement_vertical = 1 

"""

def draw():
    """création des objets (30 fois par seconde)
    creer_brique()"""
    # vide la fenetre
    pyxel.cls(0)
        
    reDisplayBriques()

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

creer_bloc()
pyxel.run(draw, update) 

