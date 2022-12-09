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
        
        self.sprite = (0, *constantes.PROYECTIL_SPRITE, constantes.COLKEY)
        self.sprite_enemigo = (0, *constantes.PROYECTIL_ENEMIGO, constantes.COLKEY)

    def mover(self, altura: int):
        if self.y < altura:
            self.y-=7

    def mover_enemigo(self):
        self.y+=4
        self.x+=random.randint(-2,2)
        
    def s_bombardero(self):
        self.y+=4
        self.x-=2
    def s_bombardero2(self):
        self.y+=4
        self.x+=2
