"""
Created by XINBO CHEN CHEN in nov 2022
Universidad Carlos III de Madrid
"""

class Disparos():
    def __init__(self,x,y,color,afiliacion):
        self.x=x
        self.y=y
        self.color=8
        self.afiliacion=afiliacion

    def __str__(self):
        print('Disparos(x={}, y={}, color={}, afiliacion={self._afiliacion})')

    @property
    def afiliacion(self):
        return self.afiliacion
    @property
    def x(self):
        return self.x
    @x.setter
    def x(self,valor):
        self.x=valor

    @property
    def y(self):
        return self.y
    @y.setter
    def y(self,valor):
        self.y=valor
