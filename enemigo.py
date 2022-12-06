"""
Created by XINBO CHEN CHEN in nov 2022
Universidad Carlos III de Madrid
"""
import random

import constantes
from proyectil import Proyectil
from explosion import Explosion


class Enemigo:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.e_disparos = []
        self.enemigos = []
        self.e_explosiones= []
        self.vivo=True
        self.sprite = ()
        self.tipo = -1
        # Para el sprite tenemos la tupla (banco, x , y, ancho, alto)

    def disparar(self):
        e_disparo = Proyectil(self.x, self.y)
        self.e_disparos.append(e_disparo)
    
    def mover():
        self


class Regular(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = (0, constantes.SPRITE_REGULAR, 14)
        self.tipo = 

    def mover(self, direccion, tamaño):
        super().mover(self, direccion, tamaño):
        if self.y<128:
            self.y+=constantes.ENEMIGO_VELOCIDAD
        else:
            self.y-=constantes.ENEMIGO_VELOCIDAD
                
        
class Rojo(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = (1, constantes.SPRITE_ROJO, 14)
    def mover(self, direccion, tamaño):
        super().mover(direccion, tamaño)

class Bombardero(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = (1, constantes.SPRITE_BOMBARDERO, 14)


class Superbombardero(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = (1, constantes.SPRITE_SUPERBOMBARDERO, 14)

