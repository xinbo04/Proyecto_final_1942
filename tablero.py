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

        self.frame_count, self.dframe = 0, 0
        self.jugar, self.win = False, False

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
        self.mapa = Mapa()
        self.regulares, self.rojos, self.bombarderos, self.superbombarderos = [], [], [], []
        self.enemigos = [self.regulares, self.rojos, self.bombarderos,
                         self.superbombarderos]
        self.explosiones = []
        self.puntuacion = Puntuacion()
        # atributo contador que nos ayuda para
        self.pos = 0
        self.no_regular = 0

        # atributo que nos indica la posición del jugador en un tiempo determinado
        self.av_x = self.av_y = 0

        # variable para que parpadee el texto del inicio (es un contador)
        self.t_cont = 0
        # Ejecutamos el juego
        pyxel.run(self.update, self.draw)

    ### UPDATE ###
    def update(self):
        """Este código se ejecuta cada frame, aquí invocamos
        los métodos que actualizan los diferentes objetos"""
        # Pulsar Q para salir del juego
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        # Pulsar el espacio para iniciar el juego
        if pyxel.btn(pyxel.KEY_SPACE) and not self.jugar:
            # frames en el momento del juego
            self.frame_count = pyxel.frame_count
            self.jugar = True

        if self.jugar:
            # diferencia de frames
            self.dframe = pyxel.frame_count - self.frame_count
            # importa el mapa y cada frame va subiendo la imagen
            # (-1280 para la zona inferior)
            pyxel.image(2).load(0, -1280 + self.dframe, "assets/MAPA.png")
            # posiciones iniciales de los enemigos

            self.enem_pos_i = (
                (random.randint(40, 180), -50), (-10, 10), (random.randint(
                    40, 80), -40),
                (random.randint(100, 120), 300))

            # Movimiento del avión
            if pyxel.btn(pyxel.KEY_RIGHT):
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

            # Disparo del avión
            if pyxel.btnp(pyxel.KEY_S, 0, 0):
                self.avion.disparar(self.avion.pulsado)
            for bala in self.avion.disparos:
                bala.mover(self.alto)

            # Aparición de los enemigos
            self.regular = Regular(*self.enem_pos_i[0])
            if self.dframe % 80 == 0:
                self.regulares.append(self.regular)

            self.rojo = Rojo(*self.enem_pos_i[1])
            if 200 <= self.dframe <= 240:
                if self.dframe % 10 == 0:
                    self.rojos.append(self.rojo)

            self.bombardero = Bombardero(*self.enem_pos_i[2])
            if self.dframe == 500 or self.dframe == 1000:
                self.bombarderos.append(self.bombardero)

            self.superbombardero = Superbombardero(*self.enem_pos_i[3])
            if self.dframe == 1200:
                self.superbombarderos.append(self.superbombardero)

            # Movimiento de los enemigos
            for tipo in range(len(self.enemigos)):
                for enemigo in range(len(self.enemigos[tipo])):
                    self.enemigos[tipo][enemigo].mover(self.dframe)

            # Disparo de los enemigos
            for tipo in range(len(self.enemigos)):
                for i in range(len(self.enemigos[tipo])):
                    self.random = random.randint(1, 2)
                    if self.dframe % 25 == 0 and self.random % 2 == 0:
                        self.enemigos[tipo][i].disparar()
                    for bala in self.enemigos[tipo][i].e_disparos:
                        self.av_x = self.avion.x
                        self.av_y = self.avion.y
                        bala.mover_enemigo(self.av_x, self.av_y)

            # Colisión/muerte de Regular
            # muerte por colisión
            for regular in self.regulares:
                #hitbox reducido a un cuadrado
                if (self.avion.x + 25 > regular.x
                    and regular.x + constantes.SPRITE_ENEMIGOS[0][2] >
                    self.avion.x
                    and self.avion.y + 15 > regular.y
                    and regular.y + constantes.SPRITE_ENEMIGOS[0][3] >
                    self.avion.y) and not self.avion.pulsado:
                    regular.vivo = False
                    self.explosiones.append(
                        Explosion(regular.x, regular.y))
                    self.explosiones.append(
                        Explosion(self.avion.x, self.avion.y))
                    self.avion.vidas -= 1
                    self.avion.vivo = False
                    if not self.regular.vivo:
                        self.puntuacion.puntos += 10

            # muerte por disparo
            if len(self.regulares) > 0 and len(self.avion.disparos) > 0:
                for regular in self.regulares:
                    for balas in self.avion.disparos:
                    #hitbox reducido a un cuadrado
                        if -11 < (balas.x + 9) - (regular.x + 9) < 11 \
                                and -11 < (balas.y + 9) - (
                                regular.y + 9) < 11 \
                                and not self.avion.pulsado:
                            self.explosiones.append(
                                Explosion(regular.x, regular.y))
                            if regular in self.regulares:
                                regular.vivo = False
                                self.puntuacion.puntos += 10
            # Colisión/muerte de Rojo
            # muerte por colisión
            for rojo in self.rojos:
                #hitbox reducido a un cuadrado
                if self.avion.x + 25 > rojo.x and rojo.x + \
                        constantes.SPRITE_ENEMIGOS[1][2] > self.avion.x and \
                        self.avion.y + 15 > rojo.y and rojo.y + \
                        constantes.SPRITE_ENEMIGOS[1][3] > self.avion.y and \
                        not self.avion.pulsado:
                    self.explosiones.append(Explosion(rojo.x, rojo.y))
                    self.explosiones.append(
                        Explosion(self.avion.x, self.avion.y))
                    rojo.vivo = False
            # muerte por disparo
            for rojo in self.rojos:
                for balas in self.avion.disparos:
                    #hitbox reducido a un cuadrado
                    if -11 < (balas.x + 9) - (rojo.x + 9) < 11 and \
                            -11 < (balas.y + 9) - (rojo.y + 9) < 11 and \
                            not self.avion.pulsado:
                        if rojo in self.rojos:
                            rojo.vivo = False
                            self.puntuacion.puntos += 30
                        self.explosiones.append(
                            Explosion(self.rojo.x, self.rojo.y))

            # Colisión/muerte de Bombardero
            # muerte por colisión
            for bombardero in self.bombarderos:
                #hitbox reducido a un cuadrado
                if (-11 < (bombardero.x + 9) - (
                        self.avion.x + 9) < 11) and (
                        -11 < (bombardero.y + 9) - (
                        self.avion.y + 9) < 11) and \
                        not self.avion.pulsado:
                    self.explosiones.append(
                        Explosion(bombardero.x, bombardero.y))
                    self.explosiones.append(
                        Explosion(self.avion.x, self.avion.y))
                    bombardero.vivo = False
                    self.avion.vidas -= 1
                    self.avion.vivo = False
            # muerte por disparo
            for bombardero in self.bombarderos:
                for balas in self.avion.disparos:
                    #hitbox reducido a un cuadrado
                    if -11 < (balas.x + 9) - (bombardero.x + 9) < 11 and \
                            -11 < (balas.y + 9) - (
                            bombardero.y + 9) < 11 and \
                            not self.avion.pulsado:
                        if bombardero.vidas > 1:
                            bombardero.vidas -= 1
                        else:
                            bombardero.vivo = False

                            self.explosiones.append(
                                Explosion(bombardero.x, bombardero.y))
                            if not bombardero.vivo:
                                self.puntuacion.puntos += 50

            # Colisión/muerte de Superbombardero
            # muerte por colisión
            for superbombardero in self.superbombarderos:
                #hitbox reducido a un cuadrado
                if -11 < (superbombardero.x + 9) - (
                        self.avion.x + 9) < 11 and \
                        -11 < (superbombardero.y + 9) - (
                        self.avion.y + 9) < 11 \
                        and not self.avion.pulsado:
                    if superbombardero.vidas > 1:
                        superbombardero.vidas -= 1
                    else:
                        self.explosiones.append(
                            Explosion(superbombardero.x,
                                      superbombardero.y))
                        self.explosiones.append(
                            Explosion(self.avion.x, self.avion.y))
                        superbombardero.vivo = False
                    self.avion.vidas -= 1
                    self.avion.vivo = False
                    self.win = True

            # muerte por disparo
            for superbombardero in self.superbombarderos:
                for balas in self.avion.disparos:
                    #hitbox reducido a un cuadrado
                    if -11 < (balas.x + 9) - (
                            superbombardero.x + 9) < 11 and \
                            -11 < (balas.y + 9) - (
                            superbombardero.y + 9) < 11 \
                            and not self.avion.pulsado:
                        if superbombardero.vidas > 1:
                            superbombardero.vidas -= 1
                        else:
                            superbombardero.vivo = False
                            self.explosiones.append(
                                Explosion(superbombardero.x,
                                          superbombardero.y))
                            if not superbombardero.vivo:
                                self.puntuacion.puntos += 100
                            self.win = True

            # muerte por disparo de enemigos hacia el avión principal
            for tipo in range(len(self.enemigos)):
                for enemigo in self.enemigos[tipo]:
                    for balas in enemigo.e_disparos:
                        if -10 < (balas.x + 8) - (
                                self.avion.x + 8) < 10 and \
                                -10 < (balas.y + 8) - (
                                self.avion.y + 8) < 10 \
                                and not self.avion.pulsado:
                            self.explosiones.append(
                                Explosion(self.avion.x, self.avion.y))
                            self.avion.vidas -= 1
                            self.avion.vivo = False
                            enemigo.e_disparos.remove(balas)

    def __pintar_inicio(self):
        pyxel.blt(*constantes.NUM_1942)
        if pyxel.frame_count % 2 == 0:
            self.t_cont += 1
        if self.t_cont >= 8:
            pyxel.text(*constantes.TECLA)
            if self.t_cont == 20:
                self.t_cont = 0
        pyxel.blt(*constantes.HECHO_POR1)
        pyxel.blt(*constantes.HECHO_POR2)

    def __pintar_final(self):
        pyxel.blt(*constantes.NUM_1942)
        # Obtiene los frames pares
        if pyxel.frame_count % 2 == 0:
            # Por cada frame par aumenta un contador
            self.t_cont += 1
        # El contador sirve para pintar el texto cada varios frames y durante varios frames 
        # (evitar el parpadeo consantes de los frames pares)
        if self.t_cont >= 8:
            pyxel.text(55, 140, "GRACIAS POR JUGAR A ESTE JUEGO", 10)
            if self.t_cont == 20:
                self.t_cont = 0
        if self.win:
            pyxel.text(90, 170, "HAS GANADO", 3)
            pyxel.text(87, 180, "ENHORABUENA!", 11)
        elif self.avion.vidas < 1:
            pyxel.text(95, 170, "GAME OVER", 2)
            pyxel.text(92, 180, "HAS PERDIDO", 2)
        # Pinta el punto del jugador y una puntuación más alta (que será la misma porque no se almacena).
        pyxel.text(70, 160, f"PUNTOS DEL JUGADOR: {self.puntuacion.puntos}", 7)
        pyxel.text(70, 150, f"PUNTUACION MAS ALTA: {self.puntuacion.puntos}", 7)

        pyxel.blt(*constantes.HECHO_POR1)
        pyxel.blt(*constantes.HECHO_POR2)

    def __pintar_avion(self, pulsado: bool):
        if not pulsado and self.avion.vivo:
            pyxel.blt(self.avion.x, self.avion.y, *self.avion.sprite)
            # cada frame cambia la hélice
            if self.dframe % 2 == 0:
                # con ajuste de píxeles
                # mitad izquierda de la hélice
                pyxel.blt(self.avion.x + 4, self.avion.y + 1,
                          *self.avion.helice)
                # mitad derecha
                pyxel.blt(self.avion.x + 14, self.avion.y + 1,
                          *self.avion.helice)
        elif pulsado and self.avion.vivo:
            loop_avion = (self.avion.x, self.avion.y, 0,
                          *constantes.AVION_SPRITES_LOOP[self.avion.pos],
                          constantes.COLKEY)
            pyxel.blt(*loop_avion)
            if self.dframe % 4 == 0:
                self.avion.pos += 1
                # La posición de los sprites del avión empieza en 0 y la función len empieza en 1
                if self.avion.pos == len(
                        constantes.AVION_SPRITES_LOOP) - 1:
                    self.avion.pulsado = False
                    self.avion.pos = 0
                    self.avion.loops -= 1

        if not self.avion.vivo:
            #se ejecuta cuando el avión choca contra un enemigo o bala 
            pyxel.blt(self.avion.x, self.avion.y, 0,
                              *constantes.AVION_MUERTE[self.avion.muerte],
                              constantes.COLKEY)
            if self.dframe % 5 == 0:
                self.avion.muerte += 1
                if self.avion.muerte == len(constantes.AVION_MUERTE) - 1:
                    self.avion.x = constantes.ANCHO // 2
                    self.avion.y = 200
                    self.avion.vivo = True
                    self.avion.muerte = 0

    def __pintar_disparo(self):
        #por cada bala creada en la lista de proyectiles de avión dibuja una
        for bala in self.avion.disparos:
            # con ajuste de píxeles para que quede centrado
            pyxel.blt(bala.x + 7, bala.y - 2, *bala.sprite)

    def __pintar_e_disparo(self):
        #crea una bala por cada enemigo del que salga 
        for tipo in range(len(self.enemigos)):
            for enemigo in range(len(self.enemigos[tipo])):
                for bala in self.enemigos[tipo][enemigo].e_disparos:
                    pyxel.blt(bala.x, bala.y, *bala.sprite_enemigo)

    def __pintar_enemigo(self):
        for tipo in range(len(self.enemigos)):
            for elemento in self.enemigos[tipo]:
                pyxel.blt(elemento.x, elemento.y, *elemento.sprite)

    def __pintar_mapa(self):
        pyxel.blt(0, 0, *self.mapa.sprite)



    def __pintar_explosiones(self):
        """"este método pinta las explosiones en el lugar en el que mueren,
         cuando los enemigos dejan de estar vivos, es decir
        cuando colisionan contra un proyectil del avión o el avión en sí. 
        Eliminando al enemigo de la lista
        """
        for tipo in range(len(self.enemigos)):
            for enemigo in self.enemigos[tipo]:
                if not enemigo.vivo and not enemigo.fin_explo:
                    pyxel.blt(enemigo.x, enemigo.y, 0,
                              *constantes.EXPLOSION[self.pos],
                              constantes.COLKEY)
                    if self.dframe % 3 == 0:
                        self.pos += 1
                        if self.pos == len(constantes.EXPLOSION) - 1:
                            enemigo.fin_explo = True
                            self.enemigos[tipo].remove(enemigo)
                            self.pos = 0

    def __pintar_hud(self):
        """Este método sirve para pintar el hud (Head-Up Display o la barra de estado en español), por ejemplo la puntuación, las vidas..."""
        # P untuación actual (con sombra del texto)
        pyxel.text(10, 20, f"PUNTOS: {self.puntuacion.puntos}", 0)
        pyxel.text(9, 19, f"PUNTOS: {self.puntuacion.puntos}", 7)
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

        """Dibujamos el avión tomando los valores del objeto avión
        Los parámetros son x, y en la pantalla  y una tupla que contiene:
        el número del banco de imágenes, la x e y de la imagen en el banco
        y el tamaño de la imagen"""
        if not self.jugar:
            pyxel.cls(0)
            self.__pintar_inicio()
        else:
            pyxel.cls(1)
            self.__pintar_mapa()
            self.__pintar_avion(self.avion.pulsado)
            self.__pintar_disparo()
            self.__pintar_enemigo()
            self.__pintar_hud()
            self.__pintar_e_disparo()
            self.__pintar_explosiones()
        if self.avion.vidas < 1 or self.win:
            pyxel.cls(0)
            self.__pintar_final()
