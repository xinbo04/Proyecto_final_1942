import constantes

class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = 0
        self.sprite=(0, *constantes.EXPLOSION[self.pos], constantes.COLKEY)
        self.vivo=True

    def explotar(self):
        for i in constantes.EXPLOSION:
            self.sprite=constantes.EXPLOSION[i]
        

