"""
Created by XINBO CHEN CHEN in nov 2022
Universidad Carlos III de Madrid
"""
import pyxel

import constantes
from proyectil import Proyectil

class Enemigo:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.e_disparos = []
        self.vivo = True
        #vuelta del avión regular
        self.vuelta = False
        self.pos = 0
        # Para el sprite tenemos la tupla (banco, x , y, ancho, alto)

    #borrar
    def mover(self):
        self.x += 0
        self.y += 0

    def disparar(self):
        e_disparo = Proyectil(self.x, self.y)
        self.e_disparos.append(e_disparo)



class Regular(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        if self.vivo:
            self.sprite = (0, *constantes.SPRITE_REGULAR, constantes.COLKEY)

    def mover(self):
        if not self.vuelta:
          self.y += constantes.ENEMIGO_VELOCIDAD
        if 125 <= self.y <= 135:
            self.vuelta = True
        if self.vuelta:
            self.y-= constantes.ENEMIGO_VELOCIDAD
            self.sprite = (0, *constantes.REGULAR_VUELTA[self.pos], constantes.COLKEY)
            if pyxel.frame_count % 3 == 0:
                if not self.pos == len(constantes.REGULAR_VUELTA) - 1:
                    self.pos += 1
            
    def disparar(self):
        super().disparar()


 
class Rojo(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = (1, *constantes.SPRITE_ROJO, constantes.COLKEY)
 
 
    def mover(self):
        #PRIMERA VUELTA
 
        if 0<pyxel.frame_count<15:
            self.x+=constantes.ENEMIGO_VELOCIDAD
            self.y+=constantes.ENEMIGO_VELOCIDAD
        if 15<pyxel.frame_count<30:
            self.y+=constantes.ENEMIGO_VELOCIDAD
        if 30<pyxel.frame_count<45:
            self.x-=constantes.ENEMIGO_VELOCIDAD
            self.y+=constantes.ENEMIGO_VELOCIDAD
        if 45<pyxel.frame_count<60:
            self.x-=constantes.ENEMIGO_VELOCIDAD
        if 60<pyxel.frame_count<75:
            self.x-=constantes.ENEMIGO_VELOCIDAD
            self.y+=constantes.ENEMIGO_VELOCIDAD
        if 75<pyxel.frame_count<90:
            self.y-=constantes.ENEMIGO_VELOCIDAD
        if 90<pyxel.frame_count<105:
            self.x+=constantes.ENEMIGO_VELOCIDAD
            self.y-=constantes.ENEMIGO_VELOCIDAD
        if 105<pyxel.frame_count<220:
            self.x+=constantes.ENEMIGO_VELOCIDAD
    #SEGUNDA VUELTA
        if 220<pyxel.frame_count<235:
            self.x+=constantes.ENEMIGO_VELOCIDAD
            self.y+=constantes.ENEMIGO_VELOCIDAD
        if 235<pyxel.frame_count<250:
            self.y+=constantes.ENEMIGO_VELOCIDAD
        if 250<pyxel.frame_count<265:
            self.x-=constantes.ENEMIGO_VELOCIDAD
            self.y+=constantes.ENEMIGO_VELOCIDAD
        if 265<pyxel.frame_count<280:
            self.x-=constantes.ENEMIGO_VELOCIDAD
        if 280<pyxel.frame_count<295:
            self.x-=constantes.ENEMIGO_VELOCIDAD
            self.y+=constantes.ENEMIGO_VELOCIDAD
        if 295<pyxel.frame_count<310:
            self.y-=constantes.ENEMIGO_VELOCIDAD
        if 310<pyxel.frame_count<325:
            self.x+=constantes.ENEMIGO_VELOCIDAD
            self.y-=constantes.ENEMIGO_VELOCIDAD
        if 325<pyxel.frame_count<400:
            self.x+=constantes.ENEMIGO_VELOCIDAD
 
class Bombardero(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = (1, *constantes.SPRITE_BOMBARDERO, constantes.COLKEY)
        self.vidas=4
    def mover(self):
        if 0<pyxel.frame_count<60:
            self.y+=constantes.ENEMIGO_VELOCIDAD
        if 60<pyxel.frame_count<75:
            self.x+=constantes.ENEMIGO_VELOCIDAD
            self.y+=constantes.ENEMIGO_VELOCIDAD
        if 75<pyxel.frame_count<90:
            self.x+=constantes.ENEMIGO_VELOCIDAD
        if 90<pyxel.frame_count<105:
            self.x+=constantes.ENEMIGO_VELOCIDAD
            self.y-=constantes.ENEMIGO_VELOCIDAD
        if 105<pyxel.frame_count<120:
            self.y-=constantes.ENEMIGO_VELOCIDAD
        if 120<pyxel.frame_count<135:
            self.y-=constantes.ENEMIGO_VELOCIDAD
            self.x-=constantes.ENEMIGO_VELOCIDAD
        if 135<pyxel.frame_count<150:
            self.x-=constantes.ENEMIGO_VELOCIDAD
        if 150<pyxel.frame_count<165:
            self.y+=constantes.ENEMIGO_VELOCIDAD
            self.x-=constantes.ENEMIGO_VELOCIDAD
        if 165<pyxel.frame_count<500:
            self.y+=constantes.ENEMIGO_VELOCIDAD
           
               
               
 
class Superbombardero(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = (1, *constantes.SPRITE_SUPERBOMBARDERO, constantes.COLKEY)
        self.vidas=20
    def mover(self):
        if 0<pyxel.frame_count<60:
            self.y-=constantes.ENEMIGO_VELOCIDAD
        if 60<pyxel.frame_count<75:
            self.x+=constantes.ENEMIGO_VELOCIDAD
            self.y+=constantes.ENEMIGO_VELOCIDAD
        if 75<pyxel.frame_count<90:
            self.x+=constantes.ENEMIGO_VELOCIDAD
        if 90<pyxel.frame_count<115:
            self.x+=constantes.ENEMIGO_VELOCIDAD
            self.y-=constantes.ENEMIGO_VELOCIDAD
        if 115<pyxel.frame_count<130:
            self.y-=constantes.ENEMIGO_VELOCIDAD
        if 130<pyxel.frame_count<145:
            self.y-=constantes.ENEMIGO_VELOCIDAD
            self.x-=constantes.ENEMIGO_VELOCIDAD
        if 145<pyxel.frame_count<160:
            self.x-=constantes.ENEMIGO_VELOCIDAD
        if 160<pyxel.frame_count<175:
            self.y+=constantes.ENEMIGO_VELOCIDAD
            self.x-=constantes.ENEMIGO_VELOCIDAD
        if 175<pyxel.frame_count<250:
            self.x-=constantes.ENEMIGO_VELOCIDAD
            self.y-=constantes.ENEMIGO_VELOCIDAD



            
    def disparar(self):
        super().disparar()
        e_2=Proyectil(self.x, self.y)
        e_3=Proyectil(self.x, self.y)
        self.e_disparos.append(e_2)
        self.e_disparos.append(e_3)
