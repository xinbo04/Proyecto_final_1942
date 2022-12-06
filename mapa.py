class Mapa:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.mapa1 = (0, )

    def mover(self):
        self.y += 1