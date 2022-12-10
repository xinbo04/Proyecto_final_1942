import constantes

class Explosion:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.sprite=''
        self.vivo=True
        self.explosion=constantes.EXPLOSION1

    def explotar(self):
        for i in constantes.EXPLOSION:
            self.explosion=constantes.EXPLOSION[i]
        

