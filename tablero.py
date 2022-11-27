from avion import Avion
from enemigo import Enemigo
import constantes
import pyxel


class Tablero:
    """Esta clase contiene la información neceraria para
    representar el tablero"""

    def __init__(self, ancho: int, alto: int):
        """ Estos parámetros son el ancho y el alto del tablero"""
        # Initializamos el objeto
        self.ancho = ancho
        self.alto = alto

        # Este bloque inicializa pyxel
        # Lo primero que tenemos que hacer es crear la pantalla, ver la API
        # para más parámetros
        pyxel.init(self.ancho, self.alto, title="1942", fps=120)

        # Cargamos los ficheros pyxres que vamos a usar
        pyxel.load("assets/avion_principal.pyxres")

        # Creamos un avión en la mitad de la pantalla en x. En y estará en la
        # posición 200
        # Notad que la imagen indicada en el init de la clase avión (en el
        # sprite), en este ejemplo es un gato
        self.avion = Avion(self.ancho // 2, 200)
        self.enemigos = []
        for elemento in constantes.ENEMIGOS_INICIAL:
            self.enemigos.append(Enemigo(*elemento))

        # Ejecutamos el juego
        pyxel.run(self.update, self.draw)

    def update(self):
        """Este código se ejecuta cada frame, aquí invocamos
        los métodos que se actualizan los  diferentes objetos"""
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        # Solo hacemos el movimiento horizontal del avión
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.avion.mover('derecha', self.ancho)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.avion.mover('izquierda', self.ancho)
        elif pyxel.btn(pyxel.KEY_UP):
            self.avion.mover('arriba', self.alto)
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.avion.mover('abajo', self.alto)
    '''
    def __pintar_avion(self):
        pyxel.blt(self.avion.x, self.avion.y, *self.avion.sprite)

    def __pintar_enemigo(self):
        for elemento in self.enemigos:
            pyxel.blt(elemento.x, elemento.y, *elemento.sprite)
    '''
    def draw(self):
        """Este código se ejecuta también cada frame, aquí deberías dibujar los
        objetos
        """
        pyxel.cls(1)

        """Dibujamos el avión tomando los valores del objeto avión
        Los parámetros son x, y en la pantalla  y una tupla que contiene: 
        el número del banco de imágenes, la x e y de la imagen en el banco 
        y el tamaño de la imagen"""
        '''
        self.__pintar_avion()
        self.__pintar_enemigo()
        '''
        pyxel.blt(self.avion.x, self.avion.y, *self.avion.sprite)

