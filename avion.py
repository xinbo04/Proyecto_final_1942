class Avion:
    """Esta clase almacena la información necesaria para nuestro
    avión. Es muy probable que necesitemos más atributos, aquí mostramos
    los básicos"""

    def __init__(self, x: int, y: int):
        """ Este método crea el objeto avión
        @param x -> la posición x inicial del avión
        @param y -> la posición y inicial del avión
        """
        self.x = x
        self.y = y

        # Aquí indicamos que la imagen del avión estará en el
        # banco=0, 0,0 a 25,16, colkey=14 .ff9798
        lista_sprites = []
        self.sprite = (0, 0, 0, 25, 16, 14)
        # Establecemos que tiene tres vidas al principio del juego
        self.vidas = 3

    def mover(self, direccion: str, tamaño: int):
        """Esto es un ejemplo de un método para mover avión horizontalmente.
        Recibe la dirección y el tamaño del tablero"""
        # Calculamos el ancho  del avión para poder hacer las comprobaciones
        # necesarias parar el avión antes de alcanzar el borde derecho
        tamaño_avion_x = self.sprite[3]
        tamaño_avion_y = self.sprite[4]

        if (direccion.lower() == "derecha" and
                self.x < tamaño - tamaño_avion_x):
            self.x += 1
        elif (direccion.lower() == "izquierda" and
              self.x > 0):
            self.x -= 1
        if (direccion.lower() == "abajo" and
                self.y < 228 ):
            self.y += 1
        elif (direccion.lower() == "arriba" and
              self.y > 81):
            self.y -= 1
