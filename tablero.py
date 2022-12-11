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
        self.explosionnes = []
        self.puntuacion = Puntuacion(0)
        # variable contador que nos ayuda para el loop del avión
        self.enemigo1 = Regular(*constantes.ENEM_POS_INICIAL[0])
        self.enemigo2 = Rojo(*constantes.ENEM_POS_INICIAL[1])
        self.enemigo3 = Bombardero(*constantes.ENEM_POS_INICIAL[2])
        self.enemigo4 = Superbombardero(*constantes.ENEM_POS_INICIAL[3])
        self.enemigos.append(self.enemigo1)
        self.enemigos.append(self.enemigo2)
        self.enemigos.append(self.enemigo3)
        self.enemigos.append(self.enemigo4)
        self.av_x = 0
        self.av_y = 0


        self.pos = 0

        # Ejecutamos el juego
        pyxel.run(self.update, self.draw)

    def cleanup_list(lista : list):
        a = 0
        while a < len(list):
            elem = list[a]
            if not elem.vivo:
                list.pop(a)
            else:
                a += 1

    def update_list(list):
        for elem in list:
            elem.update()

    def draw_list(list):
        for elem in list:
            elem.draw()
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

        # Disparo de los enemigos
        for i in range(len(self.enemigos)):
            self.random = random.randint(1,2)
            if pyxel.frame_count % 25 == 0 and self.random % 2 == 0: 
                self.enemigos[i].disparar()
            for bala in self.enemigos[i].e_disparos:
                self.av_x = self.avion.x
                self.av_y = self.avion.y
                bala.mover_enemigo(self.av_x, self.av_y)


    def eliminar(self):
        # colision
        for enemy in self.enemigo.enemigos:
            for balas in self.avion.disparos:
                if (enemy.x + constantes.SPRITE_ENEMIGOS[1][2] > balas.x
                        and balas.x + 11 > enemy.x
                        and enemy.y + constantes.SPRITE_ENEMIGOS[1][3] > balas.y
                        and balas.y + 10 > enemy.y
                ):
                    enemy.vivo = False
                    balas.vivo = False
                    self.explosionnes.append(Explosion(enemy.x, enemy.y))
                    self.puntuacion += 10
        for enemy in self.enemigo.enemigos:
            if (self.player.x + 25 > enemy.x
                    and enemy.x + constantes.SPRITE_ENEMIGOS[1][2] > self.player.x
                    and self.player.y + 15 > enemy.y
                    and enemy.y + constantes.SPRITE_ENEMIGOS[1][3] > self.player.y
            ):
                enemy.vivo = False
                self.explosionnes.append(Explosion(enemy.x, enemy.y))
                self.explosionnes.append(Explosion(self.avion.x, self.avion.y))
                self.avion.vidas -= 1

        for enemy in self.enemigo.enemigos:
            for balas in self.avion.disparos:
                if (enemy.x + constantes.SPRITE_ENEMIGOS[2][2] > balas.x
                        and balas.x + 11 > enemy.x
                        and enemy.y + constantes.SPRITE_ENEMIGOS[2][3] > balas.y
                        and balas.y + 10 > enemy.y
                ):
                    enemy.vivo = False
                    balas.vivo = False
                    self.explosionnes.append(Explosion(enemy.x, enemy.y))
                    self.puntuacion += 10
        for enemy in self.enemigo.enemigos:
            if (self.player.x + 25 > enemy.x
                    and enemy.x + constantes.SPRITE_ENEMIGOS[2][2] > self.player.x
                    and self.player.y + 15 > enemy.y
                    and enemy.y + constantes.SPRITE_ENEMIGOS[2][3] > self.player.y
            ):
                enemy.vivo = False
                self.explosionnes.append(Explosion(enemy.x, enemy.y))
                self.explosionnes.append(Explosion(self.avion.x, self.avion.y))
                self.avion.vidas -= 1

        for enemy in self.enemigo.enemigos:
            for balas in self.avion.disparos:
                if (enemy.x + constantes.SPRITE_ENEMIGOS[3][2] > balas.x
                        and balas.x + 11 > enemy.x
                        and enemy.y + constantes.SPRITE_ENEMIGOS[3][3] > balas.y
                        and balas.y + 10 > enemy.y
                ):
                    enemy.vivo = False
                    balas.vivo = False
                    self.explosionnes.append(Explosion(enemy.x, enemy.y))
                    self.puntuacion += 10

        for enemy in self.enemigo.enemigos:
            if (self.player.x + 25 > enemy.x
                    and enemy.x + constantes.SPRITE_ENEMIGOS[3][2] > self.player.x
                    and self.player.y + 15 > enemy.y
                    and enemy.y + constantes.SPRITE_ENEMIGOS[3][3] > self.player.y
            ):
                enemy.vivo = False
                self.explosionnes.append(Explosion(enemy.x, enemy.y))

                self.avion.vidas -= 1

        for enemy in self.enemigo.enemigos:
            for balas in self.avion.disparos:
                if (enemy.x + constantes.SPRITE_ENEMIGOS[4][2] > balas.x
                        and balas.x + 11 > enemy.x
                        and enemy.y + constantes.SPRITE_ENEMIGOS[4][3] > balas.y
                        and balas.y + 10 > enemy.y
                ):
                    enemy.vivo = False
                    balas.vivo = False
                    self.explosionnes.append(Explosion(enemy.x, enemy.y))
                    self.puntuacion += 10
        for enemy in self.enemigo.enemigos:
            if (self.player.x + 25 > enemy.x
                    and enemy.x + constantes.SPRITE_ENEMIGOS[4][2] > self.player.x
                    and self.player.y + 15 > enemy.y
                    and enemy.y + constantes.SPRITE_ENEMIGOS[4][3] > self.player.y
            ):
                enemy.vivo = False
                self.explosionnes.append(Explosion(enemy.x, enemy.y))

                self.avion.vidas -= 1

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
            loop_avion = (self.avion.x, self.avion.y, 0, *constantes.AVION_SPRITES_LOOP[self.pos], constantes.COLKEY)
            pyxel.blt(*loop_avion)
            if pyxel.frame_count % 4 == 0:
                self.pos += 1
                if self.pos == len(constantes.AVION_SPRITES_LOOP) - 1:
                    self.avion.pulsado = False
                    self.pos = 0
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