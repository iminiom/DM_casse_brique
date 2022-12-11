import pyxel, random

pyxel.init(128, 128, title="DM casse brique Elisa N")

balle_x = int(60)
balle_y = int(60)
balle_en_mouvement = False
direction_x=0
direction_y=-1
vitesse = 1

plateau_x = 48
plateau_y = 110

balle_deplacement_vertical =  1
balle_deplacement_horizontal = random.randint(-5,5)

bloc = []
balle_liste = ([])

score = 0
vies = 3

def plateau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_D):
        if (x < 105) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_Q):
        if (x > 0) :
            x = x - 1
    return x, y
  
def casserLaBrique():
    """casser la brique"""
    global bloc,balle_x,balle_y,score
    cassee=False
    #Un bloc de 4 lignes
    for m in range (0,4):
        ligne = bloc[m] #Une ligne de 13 briques
        for n in range (0,13):
            brique = ligne[n]  #une brique définie par x1,x2,y,type de brique, vies
            #print('brique =',brique, ' balle_x =', balle_x, ' balle_y =', balle_y)
            if balle_x-2 <= brique[1] and balle_x+2 >= brique[0] :
                
                if balle_y+2 >= brique[2] and balle_y-2 <= brique[2] +4:
                    """brique touchee"""
                    print('casée')
                    if brique [3] == 'normale':
                        brique[3] = 'cassee'
                        brique[4] = 0 #nombre de vies restantes (0)
                        displayBriques()
                        score = score + 5
                        cassee = True
                    elif brique [3] == 'a vies':
                        print('brique a vies avant',brique)
                        brique [4] = brique [4] - 1 #retirer une vie
                        if brique [4] == 1: #si plus que une vie passer en brique normale
                            brique [3] = 'normale'
                            displayBriques()
                            score = score + 5
                        cassee = True
                        print('brique a vies APRES',brique)
                        
                    elif brique [3] == 'incassable':
                        print('brique incassable')
                        rebondir()
                        cassee = False
                        return
                  
        if cassee == True:
            rebondir()
            return
        
def displayBriques():           
    global bloc
    for m in range(0,4):
        ligne = bloc[m]
        for n in range(0,13):
            brique = ligne[n]
            couleur = couleur_brique(brique[3], brique[4])
            pyxel.rect(bloc[m][n][0],bloc[m][n][2],8,4,couleur)
            
def balle_lancement():
    """la balle est lancee en appuiant sur shift (de gauche)"""
    global balle_x,balle_y,balle_en_mouvement,direction_x
    if balle_en_mouvement == False:
        if pyxel.btn(pyxel.KEY_LSHIFT):
            balle_x=plateau_x+12
            balle_y=plateau_y
            direction_x=random.randint(-2,2)
            
            afficher_balle()
            balle_en_mouvement=True

def afficher_balle():
    global balle_x
    global balle_y
    if balle_y > 0 and balle_x > 0:
        pyxel.circ(balle_x,balle_y, 2, 14)

def balle_deplacement():
    global balle_x, balle_y, balle_en_mouvement, direction_x, direction_y, vitesse, plateau_x, plateau_y, vies
    if balle_en_mouvement == True:
        balle_x = balle_x + (vitesse * direction_x)
        balle_y = balle_y + (vitesse * direction_y)
        afficher_balle()
    #rebondir sur le mur droite
    if balle_x <=0:	#or balle_x >= 120 or balle_y <=0:
        rebondir_mur()
        return
     #rebondir sur le mur gauche
    if balle_x >= 128:
        rebondir_mur()
        return
    #rebondir sur le mur du haut
    if balle_y <= 0:
        rebondir_mur_haut()
        return
    
    #rebondir sur le plateau    
    if balle_x >= plateau_x+8 and balle_x <= plateau_x+16 and balle_y >= 112:
        repartir_vertical()
        return
    
    if balle_x >= plateau_x and balle_x <= plateau_x+8 and balle_y >= 112:
        rebondir_gauche()
        return
    
    if balle_x >= plateau_x+16 and balle_x <= plateau_x+24 and balle_y >= 112:
        rebondir_droite()
        return
    
    #balle perdue
    if balle_y >=120:
        balle_en_mouvement = False
        direction_x = 0
        direction_y = -1
        balle_x = 60
        balle_y = 60
        vies = vies -1
        
def rebondir():
    global direction_x, direction_y
    print('rebondirrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
    if direction_x != 0:
        direction_x = -1 * direction_x
    if direction_y != 0:
        direction_y = -1 * direction_y
        
def rebondir_gauche():
    global direction_x, direction_y
    direction_x = -1
    direction_y = -1
        
def rebondir_droite():
    global direction_x, direction_y
    direction_x = 1
    direction_y = -1
    
def rebondir_mur():
    global direction_x, direction_y
    direction_x = -1*direction_x
    
def rebondir_mur_haut():
    global direction_y
    direction_y = 1

def repartir_vertical():
    global direction_x,direction_y
    direction_x = 0
    direction_y = -1

def creer_brique():
    ligne1 = []
    for n in range (0,13):
        brique =[10+8*n,10+8*n+8,1] #
        ligne1.append(brique)

def creer_bloc():
    global bloc
    
   
    ligne4 = [] #Une ligne de 13 briques
    
    #brique0 a vies 
    brique = [0,8,45,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne4.append(brique)
    # brique1 incassable 
    brique = [10,18,45,'normale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne4.append(brique)
    #brique2 a vies 
    brique = [20,28,45,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne4.append(brique)
    # brique3 incassable 
    brique = [30,38,45,'incassable',999999]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne4.append(brique)
    #brique4 normale
    brique = [40,48,45,'normale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne4.append(brique)
    #brique5 a vies 
    brique = [50,58,45,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne4.append(brique)
    #brique6 normale
    brique = [60,68,45,'normale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne4.append(brique)
    #brique7 a vies 
    brique = [70,78,45,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne4.append(brique)
    #brique8 normale
    brique = [80,88,45,'normale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne4.append(brique)
    # brique9 incassable 
    brique = [90,98,45,'incassable',999999]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne4.append(brique)
    #brique10 a vies 
    brique = [100,108,45,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne4.append(brique)
    # brique11 incassable 
    brique = [110,118,45,'normale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne4.append(brique)
    #brique12 a vies 
    brique = [120,128,45,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne4.append(brique)
        
    bloc.append(ligne4)
    
    

    ligne3 = [] #Une ligne de 13 briques a 3 vies
    
    #brique0 a vies
    brique = [0,8,35,'normale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne3.append(brique)
    #brique1 a vies
    brique = [10,18,35,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne3.append(brique)
    #brique2 normale
    brique = [20,28,35,'normale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne3.append(brique)
    #brique3 normale
    brique = [30,38,35,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne3.append(brique)
    #brique4 incassable
    brique = [40,48,35,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne3.append(brique)
    #brique5 normale
    brique = [50,58,35,'incassable',999999]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne3.append(brique)
    #brique6 normale
    brique = [60,68,35,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne3.append(brique)
    #brique7 incassable
    brique = [70,78,35,'incassable',999999]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne3.append(brique)
    #brique8 normale
    brique = [80,88,35,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne3.append(brique)
    #brique9 normale
    brique = [90,98,35,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne3.append(brique)
    #brique10 incassable
    brique = [100,108,35,'normale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne3.append(brique)
    #brique11 a vies
    brique = [110,118,35,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne3.append(brique)
    #brique12 a vies
    brique = [120,128,35,'normale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne3.append(brique)
    
    bloc.append(ligne3)
        
        
        
    ligne2 = [] #Une ligne de 13 briques a 3 vies
    
    #brique0 a vies
    brique = [0,8,25,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne2.append(brique)
    #brique1 a vies
    brique = [10,18,25,'normale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne2.append(brique)
    #brique2 normale
    brique = [20,28,25,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne2.append(brique)
    #brique3 normale
    brique = [30,38,25,'normale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne2.append(brique)
    #brique4 incassable
    brique = [40,48,25,'normale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne2.append(brique)
    #brique5 normale
    brique = [50,58,25,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne2.append(brique)
    #brique6 normale
    brique = [60,68,25,'normale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne2.append(brique)
    #brique7 incassable
    brique = [70,78,25,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne2.append(brique)
    #brique8 normale
    brique = [80,88,25,'normale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne2.append(brique)
    #brique9 normale
    brique = [90,98,25,'normale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne2.append(brique)
    #brique10 incassable
    brique = [100,108,25,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne2.append(brique)
    #brique11 a vies
    brique = [110,118,25,'normale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne2.append(brique)
    #brique12 a vies
    brique = [120,128,25,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne2.append(brique)
    
    bloc.append(ligne2)
    
    #Une ligne de briques normales
    ligne1 = [] #Une ligne de 13 briques normales
     #brique0 a vies
    brique = [0,8,15,'incassable',999999]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne1.append(brique)
    #brique1 a vies
    brique = [10,18,15,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne1.append(brique)
    #brique2 normale
    brique = [20,28,15,'incassable',999999]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne1.append(brique)
    #brique3 normale
    brique = [30,38,15,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne1.append(brique)
    #brique4 incassable
    brique = [40,48,15,'normale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne1.append(brique)
    #brique5 normale
    brique = [50,58,15,'normale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne1.append(brique)
    #brique6 normale
    brique = [60,68,15,'incassable',999999]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne1.append(brique)
    #brique7 incassable
    brique = [70,78,15,'nomrale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne1.append(brique)
    #brique8 normale
    brique = [80,88,15,'normale',1]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne1.append(brique)
    #brique9 normale
    brique = [90,98,15,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne1.append(brique)
    #brique10 incassable
    brique = [100,108,15,'incassable',999999]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne1.append(brique)
    #brique11 a vies
    brique = [110,118,15,'a vies',3]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne1.append(brique)
    #brique12 a vies
    brique = [120,128,15,'incassable',999999]  #une brique définie par x1,x2,y,type de brique,vies restantes
    ligne1.append(brique)
    
    bloc.append(ligne1)
        
   
    print(bloc)
    for m in range(0,3):
        for n in range(0,13):
            couleur = couleur_brique(bloc[m][n][3],bloc[m][n][4])
            pyxel.rect(bloc[m][n][0],bloc[m][n][2],8,4,couleur)
            
    return bloc            

def couleur_brique(type_de_brique, nombre_de_vies):
    couleur = 12
    if type_de_brique == 'cassee':
        couleur = 0
        return couleur
    
    if type_de_brique == 'a vies':
        if nombre_de_vies == 3:
            couleur = 3
        if nombre_de_vies == 2:
            couleur = 11
        if nombre_de_vies == 1:
            """1 vie = brique normale"""
            couleur = 12
        return couleur

    if type_de_brique == 'incassable':
        couleur = 10
        return couleur
    return couleur

def update():
    """mise à jour des variables (30 fois par seconde)"""

    global plateau_x, plateau_y, balle_x, balle_y
    global balle_deplacement_vertical, balle_deplacement_horizontal
    global vies, score, vitesse

    # mise à jour de la position du plateau
    plateau_x, plateau_y = plateau_deplacement(plateau_x, plateau_y)
    
    # mise a jour balle
    if vies > 0:
        balle_lancement()
        balle_deplacement()
        if balle_y < 50:
            casserLaBrique()

            # mise a jour de la vitesse en fonction du score
        if score > 30:
            vitesse = 2
        if score > 70:
            vitesse = 3
        if score > 100:
            vitesse = 5
    else:
        pyxel.text(45,60,'GAME OVER ! \n \n you died',7)
        pyxel.text(25,120,'(press esc to quit)',7)

def draw():
    """création des objets (30 fois par seconde)
    creer_brique()"""
    # vide la fenetre
    pyxel.cls(0) 
    displayBriques()

    # plateau (rectangle)
    pyxel.rect(plateau_x, plateau_y, 24, 8, 1)
    
    # score en haut a gauche
    pyxel.text(0,0,'score: '+str(score),7)
    
    pyxel.text(100,0,'vies: '+str(vies),7)
    
    #balle (rayon 2)
    #pyxel.circ(plateau_x + 12, plateau_y - 12, 2, 3)    

creer_bloc()
pyxel.run(draw, update) 
