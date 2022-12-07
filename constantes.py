

# Módulo que agrupa las constantes que se van a usar en el juego.
ANCHO = 224
ALTO = 256

# Avión
# para lista de sprites
AVION_SPRITE = (5, 6, 25, 15)
AVION_INICIAL = (ANCHO // 2, 200)
# velocidad del avión
AVION_VELOCIDAD = 5
# muerte del avion
AVION_MUERTE = ((6, 105, 25, 21), (36, 103, 30, 27), )

# Proyectil
PROYECTIL_SPRITE = (80, 83, 11, 10)
PROYECTIL_ENEMIGO = (65, 83, 4, 4)

# Enemigos
#velocidad
ENEMIGO_VELOCIDAD = 3
# u, v, w, h
SPRITE_REGULAR = (5, 200, 15, 14)
SPRITE_ROJO = (0, 0, 15, 15)
SPRITE_BOMBARDERO = (0, 196, 31, 23)
SPRITE_SUPERBOMBARDERO = (0, 61, 63, 48)
SPRITE_ENEMIGO = [SPRITE_REGULAR, SPRITE_ROJO, SPRITE_BOMBARDERO, SPRITE_SUPERBOMBARDERO]
ENEMIGOS_INICIAL = ((20, 0, "REGULAR"), (50, 0, "ROJO"), (100, 0,
                                                          "BOMBARDERO"),
                    (200, 80, "SUPERBOMBARDERO"))
# Explosion
EXPLOSION1 = (223, 12, 12, 11)
EXPLOSION2 = (240, 12, 14, 12)
EXPLOSION3 = (228, 25, 16, 15)
EXPLOSION4 = (201, 52, 17, 15)
EXPLOSION5 = (221, 53, 15, 15)
EXPLOSION6 = (238, 51, 16, 15)
EXPLOSION=[EXPLOSION1,EXPLOSION2,EXPLOSION3,EXPLOSION4,EXPLOSION5,EXPLOSION6]

# Números (0 al 9)
# separación con 0 de 1 pixel (num-pixel-num)
SAME = (70, 5, 10)
NUMEROS = ((117,81,4,8), (144,79,3,10), (195,*SAME), (204, *SAME), (213, 70, 6, 10), (166,79,5,10), (222, *SAME), (231, *SAME), (240, *SAME), (249, *SAME))

# Mapa
MAPA = (0, 0, 256, 256)