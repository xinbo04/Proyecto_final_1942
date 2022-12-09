import pyxel

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
        pyxel.init(self.ancho, self.alto, title="1942", fps=20)

        # Cargamos los ficheros pyxres que vamos a usar
        pyxel.image(0).load(0, 0, "assets/sprites1.png")
        pyxel.image(1).load(0, 0, "assets/sprites2.png")
        """
        pyxel.image(2).load(0, 0, "assets/sprites3.png")
        """
        """tilemap(tm)
Operate the tilemap tm (0-7). (See the Tilemap class)
bltm(x, y, tm, u, v, w, h, [colkey])
Copy the region of size (w, h) from (u, v) of the tilemap tm (0-7) to (x, y). If negative value is set for w and/or h, it will reverse horizontally and/or vertically. If colkey is specified, treated as transparent color. The size of a tile is 8x8 pixels and is stored in a tilemap as a tuple of (tile_x, tile_y)."""






        # Creamos un avión en la mitad de la pantalla en x. En y estará en la
        # posición 200
        # Notad que la imagen indicada en el init de la clase avión (en el
        # sprite), en este ejemplo es un gato
        self.avion = Avion(*constantes.AVION_INICIAL)
        self.proyectil = Proyectil(*constantes.AVION_INICIAL)
        self.enemigos = []
        self.mapa = Mapa(0, 0)
        self.puntuacion = Puntuacion(0)

        # Para la posición de los enemigos iniciales
        for elemento in constantes.ENEMIGOS_INICIAL:
            enemigo = Regular(*elemento)
            self.enemigos.append(enemigo)

        # Ejecutamos el juego
        pyxel.run(self.update, self.draw)



    def cleanup_list(list):
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


    def update(self):
        """Este código se ejecuta cada frame, aquí invocamos
        los métodos que se actualizan los  diferentes objetos"""
        #importa el mapa y cada frame va subiendo la imagen (-1280 para la zona inferior)
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

        # Movimiento de los enemigos
        for enemigo in range(len(self.enemigos)):
            self.enemigos[enemigo].mover()

        # Disparo del avión
        if pyxel.btnp(pyxel.KEY_S, 0, 0):
            self.avion.disparar()
        for bala in self.avion.disparos:
            bala.mover(self.alto)
            """
        for enemigo in self.enemigos:
            enemigo.mover()
        for j in self.enemigo.e_disparos:
            j.mover
            """
        # Disparo de los enemigos
        for i in range(len(self.enemigos)):
            if pyxel.btnp(pyxel.KEY_F, 0, 0):
                self.enemigos[i].disparar()
            for bala in self.enemigos[i].e_disparos:
                bala.mover_enemigo()
            
    def eliminar(self):
        if self.enemigo==Regular:
            tipo = 0
        if self.enemigo==Rojo:
            tipo = 1
        if self.enemigo==Bombardero:
            tipo = 2
        if self.enemigo==Superbombardero:
            tipo = 3

        #colision
        for enemy in self.enemigo.enemigos:
            for balas in self.avion.disparos:
                if (enemy.x + constantes.SPRITE_ENEMIGO[tipo][2]  > balas.x
                    and balas.x + 11 > enemy.x
                    and enemy.y + constantes.SPRITE_ENEMIGO[tipo][3] > balas.y
                    and balas.y + 10 > enemy.y
                ):
                    enemy.vivo=False
                    balas.vivo=False
                    self.enemigo.e_explosiones.append(self.explosion.Explosion)
                    self.puntuacion+=10
        for enemy in self.enemigo.enemigos:
            if (self.player.x + 25 > enemy.x
                and enemy.x + constantes.SPRITE_ENEMIGO[tipo][2]> self.player.x
                and self.player.y + 15 > enemy.y
                and enemy.y + constantes.SPRITE_ENEMIGO[tipo][3] > self.player.y
            ):
                enemy.vivo=False
                
                




    def __pintar_avion(self):
        pyxel.blt(self.avion.x, self.avion.y, *self.avion.sprite)
        # cada frame cambia la hélice
        if pyxel.frame_count % 2 == 0:
            # con ajuste de píxeles
            # mitad izquierda de la hélice
            pyxel.blt(self.avion.x + 4, self.avion.y + 1, *self.avion.helice)
            # mitad derecha
            pyxel.blt(self.avion.x + 14, self.avion.y + 1, *self.avion.helice)

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
            # los valores 5 y 12 son píxeles de margen
            pyxel.circ(5 + vida * 12, *constantes.VIDAS)


    def draw(self):
        """Este código se ejecuta también cada frame, aquí se dibujan todos los objetos
        """
        pyxel.cls(1)
        
        """Dibujamos el avión tomando los valores del objeto avión
        Los parámetros son x, y en la pantalla  y una tupla que contiene: 
        el número del banco de imágenes, la x e y de la imagen en el banco 
        y el tamaño de la imagen"""
        self.__pintar_mapa()
        self.__pintar_avion()
        self.__pintar_disparo()
        self.__pintar_enemigo()
        self.__pintar_hud()
        self.__pintar_e_disparo()

