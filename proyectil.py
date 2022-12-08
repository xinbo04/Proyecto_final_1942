"""
Created by XINBO CHEN CHEN in nov 2022
Universidad Carlos III de Madrid
"""
import constantes
import random
class Proyectil:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.sprite = (0, constantes.PROYECTIL_SPRITE, 14)
        self.sprite_enemigo = (0, constantes.PROYECTIL_ENEMIGO, 14)

    def mover(self, altura:int):
        if self.y < 256:
            self.y-=7
    def mover_enemigo(self):
        self.y+=random.randint(4,5)
        self.x+=random.randint(-2,2)