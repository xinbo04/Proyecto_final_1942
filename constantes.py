

# Módulo que agrupa las constantes que se van a usar en el juego.
ANCHO = 224
ALTO = 256

#COLKEY
COLKEY = 14

# Avión
# para lista de sprites
AVION_SPRITE = (5, 6, 25, 16)
AVION_INICIAL = (ANCHO // 2, 200)
AVION_SPRITES_LOOP = ((4,26,28,14), (131,27,27,12), (35,28,29,10), (164,31,25,7), (68,27,27,13), (35,52,30,17), (66,48,32,22), (129,46,32,25), (166,48,30,21), (195,31,28,17), (195,18,27,12), (100,29,27,7), (229,2,25,8), (5,47,25,11), (5,62,25,13))
# velocidad del avión
AVION_VELOCIDAD = 5
# muerte del avion
AVION_MUERTE = ((6, 105, 25, 21), (36, 103, 30, 27), )

# Proyectil
PROYECTIL_SPRITE = (80, 83, 11, 10)
PROYECTIL_ENEMIGO = (65, 83, 4, 4)
PROYECTIL_VELOCIDAD = 7

# Enemigos
#velocidad
ENEMIGO_VELOCIDAD = 2
# u, v, w, h
#Regular
SPRITE_REGULAR = (6, 160, 15, 14)
REGULAR_VUELTA = ((23,160,15,11), (42,162,15,7), (61, 161,15,11), (81,161,15,14))

SPRITE_ROJO = (0, 0, 15, 15)
SPRITE_BOMBARDERO = (0, 196, 31, 23)
SPRITE_SUPERBOMBARDERO = (0, 61, 63, 48)
SPRITE_ENEMIGOS = (SPRITE_REGULAR, SPRITE_ROJO, SPRITE_BOMBARDERO, SPRITE_SUPERBOMBARDERO)


# Explosion
EXPLOSION =((223, 12, 12, 11),(240, 12, 14, 12),(228, 25, 16, 15),(201, 52, 17, 15),(221, 53, 15, 15),(238, 51, 16, 15))

# Números (0 al 9)
# separación con 0 de 1 pixel (num-pixel-num)
SAME = (70, 5, 10)
NUMEROS = ((117,81,4,8), (144,79,3,10), (195,*SAME), (204, *SAME), (213, 70, 6, 10), (166,79,5,10), (222, *SAME), (231, *SAME), (240, *SAME), (249, *SAME))

# Mapa
MAPA = (0, 0, 256, 1536)

NADA = (0,0,0,0,COLKEY)


