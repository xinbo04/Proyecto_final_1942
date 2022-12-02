"""
Created by XINBO CHEN CHEN in nov 2022
Universidad Carlos III de Madrid
"""

# Módulo que agrupa las constantes que se van a usar en el juego.
ANCHO = 224
ALTO = 256

# Avión
# para lista de sprites
AVION_SPRITE = (5, 6, 25, 16)
AVION_INICIAL = (ANCHO // 2, 200)
# velocidad del avión
AVION_VELOCIDAD = 5

# Enemigos
SPRITE_REGULAR = ((0, 16, 0, 16, 16),)
SPRITE_ROJO = ((0, 32, 0, 16, 16),)
SPRITE_BOMBARDERO = (0, 64, 0, 16, 16)
SPRITE_SUPERBOMBARDERO = ((0, 48, 0, 16, 16),)
ENEMIGOS_INICIAL = ((20, 0, "REGULAR"), (50, 0, "ROJO"), (100, 0,
                                                          "BOMBARDERO"),
                    (200, 80, "SUPERBOMBARDERO"))
