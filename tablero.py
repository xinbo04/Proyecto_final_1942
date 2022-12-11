import pyxel
import random
import constantes
from avion import Avion
from proyectil import Proyectil
from enemigo import Enemigo, Regular, Rojo, Bombardero, Superbombardero
from explosion import Explosion
from puntuacion import Puntuacion
from mapa import Mapa


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
        pyxel.init(self.ancho, self.alto, title="1942", fps=25)

        # Cargamos los ficheros pyxres que vamos a usar
        pyxel.image(0).load(0, 0, "assets/sprites1.png")
        pyxel.image(1).load(0, 0, "assets/sprites2.png")
        """
        pyxel.image(2).load(0, 0, "assets/sprites3.png")
        """

        # Creamos un avión en la mitad de la pantalla en x. En y estará en la
        # posición 200
        # Notad que la imagen indicada en el init de la clase avión (en el
        # sprite), en este ejemplo es un gato
        self.avion = Avion(*constantes.AVION_INICIAL)
        self.proyectil = Proyectil(*constantes.AVION_INICIAL)
        self.enemigos = []
        self.mapa = Mapa()
        self.regulares, self.rojos, self.bombarderos, self.superbombarderos = [], [], [], []
        self.explosiones = []
        self.puntuacion = Puntuacion(0)
        # atributo contador que nos ayuda para
        self.pos = 0
        self.no_regular = 0


        # atributo que nos indica la posición del jugador en un tiempo determinado
        self.av_x = self.av_y = 0




        # Ejecutamos el juego
        pyxel.run(self.update, self.draw)


### UPDATE ###
    def update(self):
        """Este código se ejecuta cada frame, aquí invocamos
        los métodos que se actualizan los  diferentes objetos"""
        # importa el mapa y cada frame va subiendo la imagen (-1280 para la zona inferior)
        pyxel.image(2).load(0, -1280 + pyxel.frame_count, "assets/MAPA.png")
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # Movimiento del avión
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.avion.mover('derecha', self.ancho)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.avion.mover('izquierda', self.ancho)
        elif pyxel.btn(pyxel.KEY_UP):
            self.avion.mover('arriba', self.alto)
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.avion.mover('abajo', self.alto)

        # Loop del avión
        if pyxel.btnp(pyxel.KEY_Z, 0, 0) and self.avion.loops > 0:
            self.avion.pulsado = True

        # Movimiento de los enemigos
        for enemigo in range(len(self.enemigos)):
            self.enemigos[enemigo].mover()

        # Disparo del avión
        if pyxel.btnp(pyxel.KEY_S, 0, 0):
            self.avion.disparar(self.avion.pulsado)
        for bala in self.avion.disparos:
            bala.mover(self.alto)

        # Aparición de los enemigos
        self.regular = Regular(*constantes.ENEM_POS_INICIAL[0])
        if pyxel.frame_count % 50 == 0:
            self.regulares.append(self.regular)
            self.enemigos.append(self.regular)


        self.rojo = Rojo(*constantes.ENEM_POS_INICIAL[1])
        if pyxel.frame_count % 150 == 0:
            self.rojos.append(self.rojo)
            self.enemigos.append(self.rojo)


        self.bombardero = Bombardero(*constantes.ENEM_POS_INICIAL[2])
        if pyxel.frame_count % 300 == 0:
            self.bombarderos.append(self.bombardero)
            self.enemigos.append(self.bombardero)


        self.superbombardero = Superbombardero(*constantes.ENEM_POS_INICIAL[3])
        if pyxel.frame_count % 600 == 0:
            self.superbombarderos.append(self.superbombardero)
            self.enemigos.append(self.superbombardero)


        # Disparo de los enemigos
        for i in range(len(self.enemigos)):
            self.random = random.randint(1,2)
            if pyxel.frame_count % 25 == 0 and self.random % 2 == 0: 
                self.enemigos[i].disparar()
            for bala in self.enemigos[i].e_disparos:
                self.av_x = self.avion.x
                self.av_y = self.avion.y
                bala.mover_enemigo(self.av_x, self.av_y)

        #regular
        for regular in self.regulares:
            if (self.avion.x + 25 > regular.x
                and regular.x + constantes.SPRITE_ENEMIGOS[0][2] > self.avion.x
                and self.avion.y + 15 > regular.y
                and regular.y + constantes.SPRITE_ENEMIGOS[0][3] > self.avion.y):
                regular.vivo = False
                self.explosiones.append(Explosion(regular.x, regular.y))
                self.explosiones.append(Explosion(self.avion.x, self.avion.y))
                self.avion.vidas -= 1
                while self.no_regular < len(self.regulares):
                    elem = self.regulares[self.no_regular]
                    if not elem.vivo:
                        self.regulares.remove(elem)
                    else:
                        self.no_regular += 1

        if len(self.regulares) > 0 and len(self.avion.disparos) > 0:
            for regular in self.regulares:
                for balas in self.avion.disparos:
                    if -10 < (balas.x + 8) - (regular.x + 8) < 10 \
                        and -10 < (balas.y + 8) - (regular.y + 8) < 10:
                        self.explosiones.append(Explosion(regular.x, regular.y))
                        self.puntuacion.puntos += 10
                        if regular in self.regulares:
                            self.regulares.remove(regular)

    
        for rojo in self.rojos:
            if (self.avion.x + 25 > rojo.x
                and rojo.x + constantes.SPRITE_ENEMIGOS[1][2] > self.avion.x
                and self.avion.y + 15 > rojo.y
                and rojo.y + constantes.SPRITE_ENEMIGOS[1][3] > rojo.y
            ):
                self.explosiones.append(Explosion(rojo.x,rojo.y))
                self.explosiones.append(Explosion(self.avion.x, self.avion.y))

        for rojo in self.rojos:
            for balas in self.avion.disparos:
                if -10 < (balas.x + 8) - (rojo.x + 8) < 10 and \
                    -10 < (balas.y + 8) - (rojo.y + 8) < 10:
                    self.rojos.remove(rojo)
                    self.puntuacion.puntos += 10
                    self.explosiones.append(Explosion(self.rojo.x,self.rojo.y))

        for bombardero in self.bombarderos:
            print(bombardero.x, bombardero.y, self.avion.x, self.avion.y)
            if (-10 < (bombardero.x + 8) - (self.avion.x + 8) < 10) and (-10 < (bombardero.y + 8) - (self.avion.y + 8) < 10):
                self.explosiones.append(Explosion(bombardero.x, bombardero.y))
                self.explosiones.append(Explosion(self.avion.x, self.avion.y))
                self.avion.vidas -= 1

        for bombardero in self.bombarderos:
            for balas in self.avion.disparos:
                print(bombardero.x, bombardero.y, balas.x, balas.y)
                if -10 < (balas.x + 8) - (bombardero.x + 8) < 10 and \
                    -10 < (balas.y + 8) - (bombardero.y + 8) < 10:
                    if bombardero.vidas > 1:
                        bombardero.vidas-=1
                    else:
                        self.bombarderos.remove(bombardero)
                        self.explosiones.append(Explosion.explotar(bombardero.x, bombardero.y))
                        self.puntuacion.puntos += 10



        for superbombardero in self.superbombarderos:
            if -10 < (superbombardero.x + 8) - (self.avion.x + 8) < 10 and \
                    -10 < (superbombardero.y + 8) - (self.avion.y + 8) < 10:
                self.explosiones.append(Explosion(superbombardero.x, superbombardero.y))
                self.explosiones.append(Explosion(self.avion.x, self.avion.y))
                self.avion.vidas -= 1
 
        for superbombardero in self.superbombarderos:
            for balas in self.avion.disparos:
                if -10 < (balas.x + 8) - (superbombardero.x + 8) < 10 and \
                    -10 < (balas.y + 8) - (superbombardero.y + 8) < 10:
                        if superbombardero.vidas>1:
                            superbombardero.vidas-=1
                        else:

                            self.explosiones.append(Explosion(superbombardero.x, superbombardero.y))
                            self.puntuacion.puntos += 10
                            self.superbombarderos.remove(superbombardero)



    def __pintar_avion(self, pulsado: bool):
        if not pulsado:
            pyxel.blt(self.avion.x, self.avion.y, *self.avion.sprite)
            # cada frame cambia la hélice
            if pyxel.frame_count % 2 == 0:
                # con ajuste de píxeles
                # mitad izquierda de la hélice
                pyxel.blt(self.avion.x + 4, self.avion.y + 1, *self.avion.helice)
                # mitad derecha
                pyxel.blt(self.avion.x + 14, self.avion.y + 1, *self.avion.helice)
        else:
            loop_avion = (self.avion.x, self.avion.y, 0, *constantes.AVION_SPRITES_LOOP[self.avion.pos], constantes.COLKEY)
            pyxel.blt(*loop_avion)
            if pyxel.frame_count % 4 == 0:
                self.avion.pos += 1
                if self.avion.pos == len(constantes.AVION_SPRITES_LOOP) - 1:
                    self.avion.pulsado = False
                    self.avion.pos = 0
                    self.avion.loops -= 1

    def __pintar_disparo(self):
        for bala in self.avion.disparos:
            # con ajuste de píxeles para que quede centrado
            pyxel.blt(bala.x + 7, bala.y - 2, *bala.sprite)

    def __pintar_e_disparo(self):
        for enemigo in range(len(self.enemigos)):
            for bala in self.enemigos[enemigo].e_disparos:
                pyxel.blt(bala.x, bala.y, *bala.sprite_enemigo)

    def __pintar_enemigo(self):
        for elemento in self.enemigos:
            pyxel.blt(elemento.x, elemento.y, *elemento.sprite)

    def __pintar_mapa(self):
        pyxel.blt(0, 0, *self.mapa.sprite)
    
    def __pintar_explosiones(self):
        for enemigo in self.enemigos:
            for explosion in self.explosiones:
                pyxel.blt(explosion.x, explosion.y, 0, *constantes.EXPLOSION[self.pos], constantes.COLKEY)
            if pyxel.frame_count % 10 == 0:
                self.pos += 1
                if self.pos == len(constantes.EXPLOSION) - 1:
                    self.pos = 0


                

    def __pintar_hud(self):
        """Este método sirve para pintar el hud (Head-Up Display o la barra de estado en español), por ejemplo la puntuación, las vidas..."""
        # P untuación actual (con sombra del texto)
        pyxel.text(35, 20, f"{self.puntuacion.puntos}", 0)
        pyxel.text(34, 19, f"{self.puntuacion.puntos}", 5)
        # Vidas del avión
        for vida in range(self.avion.vidas):
            # circ(x, y, r, col)
            # los valores 5 y 12 son píxeles de margen
            pyxel.circ(10 + vida * 12, 246, 4, 8)
            pyxel.circ(10 + vida * 12, 246, 3, 2)
        # Loops restantes
        for loop in range(self.avion.loops):
            # rect(x, y, w, h, col)
            pyxel.rect(210 - loop * 12, 240, 8, 8, 4)
            pyxel.rect(211 - loop * 12, 241, 6, 6, 9)

    def draw(self):
        """Este código se ejecuta también cada frame, aquí se dibujan todos los objetos
        """
        pyxel.cls(1)

        """Dibujamos el avión tomando los valores del objeto avión
        Los parámetros son x, y en la pantalla  y una tupla que contiene: 
        el número del banco de imágenes, la x e y de la imagen en el banco 
        y el tamaño de la imagen"""
        self.__pintar_mapa()
        self.__pintar_avion(self.avion.pulsado)
        self.__pintar_disparo()
        self.__pintar_enemigo()
        self.__pintar_hud()
        self.__pintar_e_disparo()
        self.__pintar_explosiones()
