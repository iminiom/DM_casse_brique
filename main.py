import pyxel

class Jeu:
    def __init__(self):
        pyxel.init(128, 128)
        self.plateau_x = 60
        self.plateau_y = 60
        pyxel.run(self.update, self.draw)

    def vaisseau_deplacement(self):
        if pyxel.btn(pyxel.D) and self.plateau_x<120:
            self.plateau_x += 1
        if pyxel.btn(pyxel.Q) and self.plateau_x>0:
            self.plateau_x += -1
        if pyxel.btn(pyxel.S) and self.plateau_y<120:
            self.vaisseau_y += 1
        if pyxel.btn(pyxel.Z) and self.plateau_y>0:
            self.plateau_y += -1

    def update(self):
        self.plateau_deplacement()

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.vaisseau_x, self.vaisseau_y, 8, 8, 1)
        
Jeu()
