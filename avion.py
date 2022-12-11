import constantes
from proyectil import Proyectil


class Avion:
    """Esta clase almacena la información necesaria para nuestro
    avión. Es muy probable que necesitemos más atributos, aquí mostramos
    los básicos"""

    def __init__(self, x: int, y: int):
        """ Este método crea el objeto avión
        @param x: indica la posición x inicial del avión
        @param y: indica la posición y inicial del avión
        """
        self.x = x
        self.y = y
        # Aquí indicamos que la imagen del avión estará en el
        # banco=0, posición inicial de tamaño mxn, colkey=14 #ff9798
        # img, u, v, w, h, [colkey]
        self.sprite = (0, *constantes.AVION_SPRITE, constantes.COLKEY)
        # para la hélice, si ponemos un número negativo se invierte la imagen
        # horizontalmente
        self.helice = (0, 9, 7, -7, 1)
        # Establecemos que tiene tres vidas al principio del juego
        self.disparos = []
        self.vidas = 3
        self.loops = 3
        self.vivo = True
        # Variable booleana para el loop del avión
        self.pulsado = False
        self.pos = 0
        # contador para los sprites de su muerte
        self.muerte = 0

    def mover(self, direccion: str, tamaño: int):
        """Esto es un ejemplo de un método para mover avión horizontalmente.
        Recibe la dirección y el tamaño del tablero"""
        # Calculamos el ancho del avión para poder hacer las comprobaciones
        # necesarias parar el avión antes de alcanzar el borde derecho
        tamaño_avion_x = self.sprite[3]

        if (direccion.lower() == "derecha" and
                self.x < 224 - tamaño_avion_x):
            self.x += constantes.AVION_VELOCIDAD
        elif (direccion.lower() == "izquierda" and
              self.x > 0):
            self.x -= constantes.AVION_VELOCIDAD
        # 228 es el límite inferior
        if (direccion.lower() == "abajo" and
                self.y < 228):
            self.y += constantes.AVION_VELOCIDAD
        # 81 es el límite superior
        elif (direccion.lower() == "arriba" and
              self.y > 81):
            self.y -= constantes.AVION_VELOCIDAD

    def disparar(self, pulsado: bool):
        if not pulsado:
            disparo = Proyectil(self.x, self.y)
            self.disparos.append(disparo)
