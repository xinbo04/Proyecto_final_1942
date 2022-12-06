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
        pyxel.init(self.ancho, self.alto, title="1942", fps=30)

        # Cargamos los ficheros pyxres que vamos a usar
        pyxel.image(0).load(0, 0, "assets/sprites1.png")
        pyxel.image(1).load(0, 0, "assets/sprites2.png")
        pyxel.image(2).load(0, 0, "assets/sprites3.png")

        """tilemap(tm)
Operate the tilemap tm (0-7). (See the Tilemap class)
bltm(x, y, tm, u, v, w, h, [colkey])
Copy the region of size (w, h) from (u, v) of the tilemap tm (0-7) to (x, y). If negative value is set for w and/or h, it will reverse horizontally and/or vertically. If colkey is specified, treated as transparent color. The size of a tile is 8x8 pixels and is stored in a tilemap as a tuple of (tile_x, tile_y)."""
        pyxel.tilemap(0).load(0, 0, "assets/mapa1.png")
        pyxel.tilemap(1).load(0, 0, "assets/mapa2.png")
        pyxel.tilemap(2).load(0, 0, "assets/mapa3.png")
        pyxel.tilemap(3).load(0, 0, "assets/mapa4.png")
        pyxel.tilemap(4).load(0, 0, "assets/mapa5.png")
        pyxel.tilemap(5).load(0, 0, "assets/mapa_agua.png")



        # Creamos un avión en la mitad de la pantalla en x. En y estará en la
        # posición 200
        # Notad que la imagen indicada en el init de la clase avión (en el
        # sprite), en este ejemplo es un gato
        self.avion = Avion(self.ancho // 2, 200)
        self.enemigo = Enemigo(self.ancho // 2, 20)
        self.proyectil = Proyectil(self.ancho // 2, 200)
        self.enemigos = []
        self.proyectiles = []

        for elemento in constantes.ENEMIGOS_INICIAL:
            self.enemigos.append(Enemigo(*elemento))

        # Ejecutamos el juego
        pyxel.run(self.update, self.draw)



    def cleanup_list(list):
        a = 0
        while i < len(list):
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
        for enemigo in self.enemigos:
            enemigo.mover()
        for j in self.enemigo.e_disparos:
            j.mover
            
    def eliminar(self):
        if self.enemigo==Regular:
            tipo = 0
        if self.enemigo==Rojo:
            tipo = 1
        if self.enemigo==Bombardero:
            tipo = 2
        if self.enemigo==Superbombardero:
            tipo = 3

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
            pyxel.blt(self.avion.x + 4, self.avion.y + 1, *self.avion.helice)
            pyxel.blt(self.avion.x + 14, self.avion.y + 1, *self.avion.helice)

    def __pintar_disparo(self):
        for i in self.avion.disparos:
            pyxel.blt(i.x, i.y, *i.sprite)

    def __pintar_enemigo(self):
        for elemento in self.enemigos:
            pyxel.blt(elemento.x, elemento.y, *elemento.sprite)

    def __pintar_mapa(self):
        pyxel.blt
        
        

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
        self.__pintar_enemigo()

