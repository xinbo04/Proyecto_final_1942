import constantes
from proyectil import Proyectil


class Enemigo:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.e_disparos = []
        self.vivo = True
        # vuelta del avión regular
        self.vuelta = False
        self.pos = 0
        self.fin_explo = False
        # Para el sprite tenemos la tupla (banco, x , y, ancho, alto)

    def disparar(self):
        e_disparo = Proyectil(self.x, self.y)
        self.e_disparos.append(e_disparo)


class Regular(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        if self.vivo:
            self.sprite = (0, *constantes.SPRITE_REGULAR, constantes.COLKEY)

    def mover(self, dframe):
        if not self.vuelta:
            self.y += constantes.ENEMIGO_VELOCIDAD
        if 125 <= self.y <= 135:
            self.vuelta = True
        if self.vuelta:
            self.y -= constantes.ENEMIGO_VELOCIDAD
            self.sprite = (
                0, *constantes.REGULAR_VUELTA[self.pos], constantes.COLKEY)
            if dframe % 3 == 0:
                if not self.pos == len(constantes.REGULAR_VUELTA) - 1:
                    self.pos += 1

    def disparar(self):
        super().disparar()


class Rojo(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = (1, *constantes.SPRITE_ROJO, constantes.COLKEY)

    def mover(self, dframe):

        if 200 < dframe < 245:
            self.sprite = (1, *constantes.ROJO_VUELTA[0], constantes.COLKEY)
            self.x += constantes.ENEMIGO_VELOCIDAD
        if 245 < dframe < 260:
            self.sprite = (1, *constantes.ROJO_VUELTA[1], constantes.COLKEY)
            self.x += constantes.ENEMIGO_VELOCIDAD
            self.y += constantes.ENEMIGO_VELOCIDAD
        if 260 < dframe < 275:
            self.sprite = (1, *constantes.ROJO_VUELTA[2], constantes.COLKEY)
            self.y += constantes.ENEMIGO_VELOCIDAD
        if 275 < dframe < 290:
            self.sprite = (1, *constantes.ROJO_VUELTA[3], constantes.COLKEY)
            self.x -= constantes.ENEMIGO_VELOCIDAD
            self.y += constantes.ENEMIGO_VELOCIDAD
        if 290 < dframe < 305:
            self.sprite = (1, *constantes.ROJO_VUELTA[4], constantes.COLKEY)
            self.x -= constantes.ENEMIGO_VELOCIDAD
        if 305 < dframe < 320:
            self.sprite = (1, *constantes.ROJO_VUELTA[5], constantes.COLKEY)
            self.x -= constantes.ENEMIGO_VELOCIDAD
            self.y -= constantes.ENEMIGO_VELOCIDAD
        if 320 < dframe < 335:
            self.sprite = (1, *constantes.ROJO_VUELTA[6], constantes.COLKEY)
            self.y -= constantes.ENEMIGO_VELOCIDAD
        if 335 < dframe < 350:
            self.sprite = (1, *constantes.ROJO_VUELTA[7], constantes.COLKEY)
            self.x += constantes.ENEMIGO_VELOCIDAD
            self.y -= constantes.ENEMIGO_VELOCIDAD
        if 350 < dframe < 365:
            self.sprite = (1, *constantes.ROJO_VUELTA[4], constantes.COLKEY)
            self.x -= constantes.ENEMIGO_VELOCIDAD
        if 365 < dframe > 380:
            self.sprite = (1, *constantes.ROJO_VUELTA[0], constantes.COLKEY)
            self.x += constantes.ENEMIGO_VELOCIDAD
        if 380 < dframe < 395:
            self.sprite = (1, *constantes.ROJO_VUELTA[4], constantes.COLKEY)
            self.x -= constantes.ENEMIGO_VELOCIDAD
        if dframe > 400:
            dframe -= 45


class Bombardero(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = (1, *constantes.SPRITE_BOMBARDERO, constantes.COLKEY)
        self.vidas = 4

    def mover(self, dframe):
        # primera aparicion
        if 500 < dframe < 560:
            self.sprite = (
            1, *constantes.BOMBARDERO_VUELTA[0], constantes.COLKEY)
            self.y += constantes.ENEMIGO_VELOCIDAD
        if 560 < dframe < 575:
            self.sprite = (
            1, *constantes.BOMBARDERO_VUELTA[1], constantes.COLKEY)
            self.x += constantes.ENEMIGO_VELOCIDAD
            self.y += constantes.ENEMIGO_VELOCIDAD
        if 575 < dframe < 590:
            self.sprite = (
            1, *constantes.BOMBARDERO_VUELTA[2], constantes.COLKEY)
            self.x += constantes.ENEMIGO_VELOCIDAD
        if 590 < dframe < 605:
            self.sprite = (
            1, *constantes.BOMBARDERO_VUELTA[3], constantes.COLKEY)
            self.x += constantes.ENEMIGO_VELOCIDAD
            self.y -= constantes.ENEMIGO_VELOCIDAD
        if 605 < dframe < 620:
            self.sprite = (
            1, *constantes.BOMBARDERO_VUELTA[4], constantes.COLKEY)
            self.y -= constantes.ENEMIGO_VELOCIDAD
        if 620 < dframe < 635:
            self.sprite = (
            1, *constantes.BOMBARDERO_VUELTA[5], constantes.COLKEY)
            self.y -= constantes.ENEMIGO_VELOCIDAD
            self.x -= constantes.ENEMIGO_VELOCIDAD
        if 635 < dframe < 650:
            self.sprite = (
            1, *constantes.BOMBARDERO_VUELTA[6], constantes.COLKEY)
            self.x -= constantes.ENEMIGO_VELOCIDAD
        if 650 < dframe < 665:
            self.sprite = (
            1, *constantes.BOMBARDERO_VUELTA[7], constantes.COLKEY)
            self.y += constantes.ENEMIGO_VELOCIDAD
            self.x -= constantes.ENEMIGO_VELOCIDAD
        if 665 < dframe < 1000:
            self.sprite = (
            1, *constantes.BOMBARDERO_VUELTA[0], constantes.COLKEY)
            self.y += constantes.ENEMIGO_VELOCIDAD

        # segunda aparicion
        if 1000 < dframe < 1060:
            self.sprite = (
            1, *constantes.BOMBARDERO_VUELTA[0], constantes.COLKEY)
            self.y += constantes.ENEMIGO_VELOCIDAD
        if 1060 < dframe < 1075:
            self.sprite = (
            1, *constantes.BOMBARDERO_VUELTA[1], constantes.COLKEY)
            self.x += constantes.ENEMIGO_VELOCIDAD
            self.y += constantes.ENEMIGO_VELOCIDAD
        if 1075 < dframe < 1090:
            self.sprite = (
            1, *constantes.BOMBARDERO_VUELTA[2], constantes.COLKEY)
            self.x += constantes.ENEMIGO_VELOCIDAD
        if 1090 < dframe < 1105:
            self.sprite = (
            1, *constantes.BOMBARDERO_VUELTA[3], constantes.COLKEY)
            self.x += constantes.ENEMIGO_VELOCIDAD
            self.y -= constantes.ENEMIGO_VELOCIDAD
        if 1105 < dframe < 1120:
            self.sprite = (
            1, *constantes.BOMBARDERO_VUELTA[4], constantes.COLKEY)
            self.y -= constantes.ENEMIGO_VELOCIDAD
        if 1120 < dframe < 1135:
            self.sprite = (
            1, *constantes.BOMBARDERO_VUELTA[5], constantes.COLKEY)
            self.y -= constantes.ENEMIGO_VELOCIDAD
            self.x -= constantes.ENEMIGO_VELOCIDAD
        if 1135 < dframe < 1150:
            self.sprite = (
            1, *constantes.BOMBARDERO_VUELTA[6], constantes.COLKEY)
            self.x -= constantes.ENEMIGO_VELOCIDAD
        if 1150 < dframe < 1165:
            self.sprite = (
            1, *constantes.BOMBARDERO_VUELTA[7], constantes.COLKEY)
            self.y += constantes.ENEMIGO_VELOCIDAD
            self.x -= constantes.ENEMIGO_VELOCIDAD
        if 1165 < dframe < 1500:
            self.sprite = (
            1, *constantes.BOMBARDERO_VUELTA[0], constantes.COLKEY)
            self.y += constantes.ENEMIGO_VELOCIDAD


class Superbombardero(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = (
            1, *constantes.SPRITE_SUPERBOMBARDERO, constantes.COLKEY)
        self.vidas = 15

    def mover(self, dframe):
        if 1200 < dframe < 1260:
            self.y -= constantes.ENEMIGO_VELOCIDAD
        if 1260 < dframe < 1275:
            self.x += constantes.ENEMIGO_VELOCIDAD
            self.y += constantes.ENEMIGO_VELOCIDAD
        if 1275 < dframe < 1290:
            self.x += constantes.ENEMIGO_VELOCIDAD
        if 1290 < dframe < 1315:
            self.x += constantes.ENEMIGO_VELOCIDAD
            self.y -= constantes.ENEMIGO_VELOCIDAD
        if 1315 < dframe < 1330:
            self.y -= constantes.ENEMIGO_VELOCIDAD
        if 1330 < dframe < 1345:
            self.y -= constantes.ENEMIGO_VELOCIDAD
            self.x -= constantes.ENEMIGO_VELOCIDAD
        if 1345 < dframe < 1360:
            self.x -= constantes.ENEMIGO_VELOCIDAD
        if 1360 < dframe < 1375:
            self.y += constantes.ENEMIGO_VELOCIDAD
            self.x -= constantes.ENEMIGO_VELOCIDAD
        if 1375 < dframe < 1390:
            self.x -= constantes.ENEMIGO_VELOCIDAD
            self.y -= constantes.ENEMIGO_VELOCIDAD
        if 1390 < dframe < 1405:
            self.x += constantes.ENEMIGO_VELOCIDAD
            self.y += constantes.ENEMIGO_VELOCIDAD

    def disparar(self):
        super().disparar()
        e_2 = Proyectil(self.x, self.y)
        e_3 = Proyectil(self.x, self.y)
        self.e_disparos.append(e_2)
        self.e_disparos.append(e_3)
