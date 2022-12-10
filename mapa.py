import constantes


class Mapa:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.sprite = (2, *constantes.MAPA, constantes.COLKEY)