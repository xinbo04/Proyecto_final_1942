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
        # banco=0, 5-25 x 6-15 (tamaño avión principal: 20x9), colkey=8
        lista_sprites = []
        self.sprite = (0, 5, 6, 25, 15, 8)
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
                self.y < tamaño - tamaño_avion_y):
            self.y += 1
        elif (direccion.lower() == "arriba" and
              self.y > 0):
            self.y -= 1