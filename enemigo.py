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
        self.e_explosiones= []
        self.vivo=True
        self.sprite = (0, *constantes.SPRITE_REGULAR, constantes.COLKEY)
        # Para el sprite tenemos la tupla (banco, x , y, ancho, alto)
    def mover(self, direccion, tamaño):
        self.x += 1
        self.y += 1

        
    def disparar(self):
        e_disparo = Proyectil(self.x, self.y)
        self.e_disparos.append(e_disparo)


class Regular(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = (0, *constantes.SPRITE_REGULAR, constantes.COLKEY)


    def mover(self, direccion, tamaño):
        super().mover(self, direccion, tamaño)
        if self.y<128:
            self.y+=constantes.ENEMIGO_VELOCIDAD
        else:
            self.y-=constantes.ENEMIGO_VELOCIDAD
                
        
class Rojo(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = (1, *constantes.SPRITE_ROJO, constantes.COLKEY)
    def mover(self, direccion, tamaño):
        super().mover(direccion, tamaño)
        self.x+=constantes.ENEMIGO_VELOCIDAD
        if self.x==24 or self.x==25 or self.x==26:
            for i in (1,10):
                self.x+=2
                self.y+=2
        if self.x==44 or self.x==45 or self.x==46:
            for i in (1,10):
                self.x+=2
                self.y-=2
        if self.x==64 or self.x==65 or self.x==66:
            for i in (1,6):
                self.x-=2
                self.y-=2
        if self.x==52 or self.x==53 or self.x==54:
            for i in (1,4):
                self.x+=2
                self.y+=2
        if self.x==60: 
            self.x+=3
        if self.x==61:
            self.x+=2
        if self.x==62:
            self.x+=1
        if self.x==63:
            self.x+=5

        
class Bombardero(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = (1, *constantes.SPRITE_BOMBARDERO, constantes.COLKEY)


class Superbombardero(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = (1, *constantes.SPRITE_SUPERBOMBARDERO, constantes.COLKEY)

