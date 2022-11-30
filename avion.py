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
        lista_sprites = []
        self.sprite = (0, 5, 6, 25, 16, 14)
        # para la hélice, si ponemos un número negativo se invierte la imagen
        # horizontalmente
        self.helice = (0, 9, 7, -7, 1)
        # Establecemos que tiene tres vidas al principio del juego
        self.vidas = 3
        self.disparos=[]
    def mover(self, direccion: str, tamaño: int):
        """Esto es un ejemplo de un método para mover avión horizontalmente.
        Recibe la dirección y el tamaño del tablero"""
        # Calculamos el ancho del avión para poder hacer las comprobaciones
        # necesarias parar el avión antes de alcanzar el borde derecho
        tamaño_avion_x = self.sprite[3]
        tamaño_avion_y = self.sprite[4]

        if (direccion.lower() == "derecha" and
                self.x < tamaño - tamaño_avion_x):
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
    def disparar(self):
        disparo= Proyectil (self.x,self.y)
        self.disparos.append(disparo)





