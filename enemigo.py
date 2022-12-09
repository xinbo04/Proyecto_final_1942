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
    def mover(self):
        self.x = 0
        self.y = 0

        
    def disparar(self):
        e_disparo = Proyectil(self.x, self.y)
        self.e_disparos.append(e_disparo)


class Regular(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = (0, *constantes.SPRITE_REGULAR, constantes.COLKEY)


    def mover(self):
        val = False
        if not val:
          self.y += constantes.ENEMIGO_VELOCIDAD
        if 125 <= self.y <= 135:
            val = True
        if val:
            self.y-= constantes.ENEMIGO_VELOCIDAD
            
    def disparar(self):
        super().disparar()
        
class Rojo(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = (1, *constantes.SPRITE_ROJO, constantes.COLKEY)
    def mover(self, direccion, tamaño):
        super().mover(direccion, tamaño)
        self.x+=constantes.ENEMIGO_VELOCIDAD
        #PRIMERA VUELTA
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
            for i in (1,2):
                self.x+=5
        #SEGUNDA VUELTA
        
        if self.x==114 or self.x==115 or self.x==116:
            for i in (1,10):
                self.x+=2
                self.y+=2
        if self.x==134 or self.x==135 or self.x==136:
            for i in (1,10):
                self.x+=2
                self.y-=2
        if self.x==154 or self.x==155 or self.x==156:
            for i in (1,6):
                self.x-=2
                self.y-=2
        if self.x==142 or self.x==143 or self.x==144:
            for i in (1,4):
                self.x+=2
                self.y+=2
        if self.x==150: 
            self.x+=3
        if self.x==151:
            self.x+=2
        if self.x==152:
            self.x+=1
        if self.x==153:
            self.x+=5
        
class Bombardero(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = (1, *constantes.SPRITE_BOMBARDERO, constantes.COLKEY)
        def mover(self,direcion,tamaño):
            super().mover(direcion, tamaño)
            self.y+=constantes.ENEMIGO_VELOCIDAD
            if self.y==180:
                for i in (1,20):
                    self.x+=constantes.ENEMIGO_VELOCIDAD
                    self.y+=1
                for i in (1,20):
                    self.x-=constantes.ENEMIGO_VELOCIDAD
                    self.y-=1
        
    def disparar(self):
        super().disparar(self)
        e_disparo = Proyectil.mover_enemigo(self.x, self.y)
        self.e_disparos.append(e_disparo)

class Superbombardero(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = (1, *constantes.SPRITE_SUPERBOMBARDERO, constantes.COLKEY)
        def mover(self,direcion,tamaño):
            super().mover(direcion, tamaño)
            self.y-=1
            if self.y ==170:
                for i in (1,30):
                    self.y-=1
                    self.x-=2
                for i in (1,20):
                    self.y+=1
                    self.x-=1
            self.y+=0

    def disparar(self):
        super().disparar(self)
        e_disparo = Proyectil(self.x, self.y)
        e_1=Proyectil(self.x, self.y)
        e_2=Proyectil(self.x, self.y)
        self.e_disparos.append(e_disparo)
        self.e_disparos.append(e_1)
        self.e_disparos.append(e_2)


    def d2(self):
        super().disparar(self)
        e_disparo = Proyectil.s_bombardero(self.x, self.y)
        self.e_disparos.append(e_disparo)
