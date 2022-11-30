"""
Created by XINBO CHEN CHEN in nov 2022
Universidad Carlos III de Madrid
"""


class Proyectil:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = (0, 103, 84, 11, 10, 14)

    def mover(self, altura:int):
        if self.y < 256:
            self.y-=7
    def mover_enemigo(self):
        self.y