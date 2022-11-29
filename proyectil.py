"""
Created by XINBO CHEN CHEN in nov 2022
Universidad Carlos III de Madrid
"""


class Proyectil:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = (0, 103, 84, 11, 10, 14)

    def mover(self, disparar: bool):
        if disparar:
            x_momento_disparo = self.x
            y_momento_disparo = self.y
            self.x = x_momento_disparo
            self.y = y_momento_disparo
            self.y += 1
