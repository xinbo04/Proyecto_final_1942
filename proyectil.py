import constantes
import random


class Proyectil:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.stop = [0, 0, 0, 0]

        self.sprite = (0, *constantes.PROYECTIL_SPRITE, constantes.COLKEY)
        self.sprite_enemigo = (
            0, *constantes.PROYECTIL_ENEMIGO, constantes.COLKEY)

    def mover(self, altura: int):
        if self.y < altura:
            self.y -= constantes.PROYECTIL_VELOCIDAD

    def mover_enemigo(self, av_x, av_y):

        if av_x > self.x and self.stop[1] == 0:
            self.stop[0] = 1
        elif av_x < self.x and self.stop[0] == 0:
            self.stop[1] = 1
        if av_y > self.y and self.stop[3] == 0:
            self.stop[2] = 1
        elif av_y < self.y and self.stop[2] == 0:
            self.stop[3] = 1

        if self.stop[0] == 1:
            self.x += 0.8
        elif self.stop[1] == 1:
            self.x -= 0.8

        if self.stop[2] == 1:
            self.y += 2.4
        elif self.stop[3] == 1:
            self.y -= 2.4

    def s_bombardero(self):
        self.y += 4
        self.x -= 2

    def s_bombardero2(self):
        self.y += 4
        self.x += 2
