"""
Created by XINBO CHEN CHEN in nov 2022
Universidad Carlos III de Madrid
"""
import constantes
class Enemigo:

    def __init__(self, x: int, y: int, tipo: str):
        self.x = x
        self.y = y
        self.tipo = tipo

        # Para el sprite tenemos la tupla (banco, x , y, ancho, alto)
        #ESTO ESTÁ HECHO SIN HERENCIA, HAY QUE USAR HERENCIA
        if tipo == "REGULAR":
            self.sprite = constantes.SPRITE_REGULAR
        elif tipo == "ROJO":
            self.sprite = constantes.SPRITE_ROJO
        elif tipo == "BOMBARDERO":
            self.sprite = constantes.SPRITE_BOMBARDERO
        elif tipo == "SUPERBOMBARDERO":
            self.sprite = constantes.SPRITE_SUPERBOMBARDERO
