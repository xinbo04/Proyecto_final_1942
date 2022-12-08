import constantes


class Mapa:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.sprite = (2, *constantes.MAPA, 14)

    def mover(self):
        self.tipo = 0
        self.y += 1
        if self.y >= 256:
            self.y = 0
            self.tipo += 1
            if self.tipo == 5:
                self.tipo = 0