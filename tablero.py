import pyxel

import constantes
from avion import Avion
from proyectil import Proyectil
from enemigo import Enemigo


class Tablero:
    """Esta clase contiene la información necesaria para
    representar el tablero"""

    def __init__(self, ancho: int, alto: int):
        """ Estos parámetros son el ancho y el alto del tablero"""
        # Initializamos el objeto
        self.ancho = ancho
        self.alto = alto

        # Este bloque inicializa pyxel
        # Lo primero que tenemos que hacer es crear la pantalla, ver la API
        # para más parámetros
        pyxel.init(self.ancho, self.alto, title="1942", fps=30)

        # Cargamos los ficheros pyxres que vamos a usar
        pyxel.image(0).load(0, 0, "assets/sprites1.png")
        # Creamos un avión en la mitad de la pantalla en x. En y estará en la
        # posición 200
        # Notad que la imagen indicada en el init de la clase avión (en el
        # sprite), en este ejemplo es un gato
        self.avion = Avion(self.ancho // 2, 200)
        self.enemigo = Enemigo(self.ancho//2,20,'REGULAR')
        self.proyectil = Proyectil(self.ancho // 2, 200)
        self.enemigos = []
        self.proyectiles=[]

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
        if pyxel.btn(pyxel.KEY_S):
            self.avion.disparar()
        for i in self.avion.disparos:
            i.mover(256)

    def __pintar_avion(self):
        pyxel.blt(self.avion.x, self.avion.y, *self.avion.sprite)
        # cada frame cambia la hélice
        if pyxel.frame_count % 2 == 0:
            pyxel.blt(self.avion.x + 4, self.avion.y + 1, *self.avion.helice)
            pyxel.blt(self.avion.x + 14, self.avion.y + 1, *self.avion.helice)

    def __pintar_disparo(self):
        for i in self.avion.disparos:
            pyxel.blt(i.x, i.y, *i.sprite)
        for j in self.enemigo.e_disparos:
            pyxel.blt(j.x,j.y, *j.sprite)


    def __pintar_enemigo(self):
        for elemento in self.enemigos:
            pyxel.blt(elemento.x, elemento.y, *elemento.sprite)


    def draw(self):
        """Este código se ejecuta también cada frame, aquí deberías dibujar los
        objetos
        """
        pyxel.cls(1)

        """Dibujamos el avión tomando los valores del objeto avión
        Los parámetros son x, y en la pantalla  y una tupla que contiene: 
        el número del banco de imágenes, la x e y de la imagen en el banco 
        y el tamaño de la imagen"""
        self.__pintar_avion()
        self.__pintar_disparo()
        '''
        self.__pintar_enemigo()
        '''
