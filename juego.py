"""
Juego: Conejos y Tejones
Basado en la presentación "Python II".

Controles:
- W / flecha arriba: mover hacia arriba.
- A / flecha izquierda: mover hacia la izquierda.
- S / flecha abajo: mover hacia abajo.
- D / flecha derecha: mover hacia la derecha.
- Clic izquierdo: disparar una flecha.
- Cerrar la ventana: salir del juego.
"""

import os
import sys
import math
import random

import pygame as pg


# ---------------------------------------------------------------------
# 1. Inicialización del juego
# ---------------------------------------------------------------------

pg.init()

# Dimensiones de la ventana.
width, height = 640, 480
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Conejos y Tejones")

# Control de la velocidad de actualización del juego.
clock = pg.time.Clock()
FPS = 60

# Estado de las teclas W, A, S y D, en ese orden.
keys = [False, False, False, False]

# Posición inicial del jugador.
playerpos = [100, 100]

# Variables para registrar los disparos:
# acc[0] = cantidad de aciertos; acc[1] = cantidad de disparos.
acc = [0, 0]
arrows = []

# Variables para controlar la aparición de los tejones.
badtimer = 100
badtimer1 = 0
badguys = [[640, 100]]

# Salud inicial.
healthvalue = 194


# ---------------------------------------------------------------------
# 2. Carga de imágenes
# ---------------------------------------------------------------------

# Construimos las rutas a partir de la carpeta donde está este archivo.
# La estructura esperada es:
# carpeta_del_juego/
#   juego.py
#   resources/
#       images/
#           dude.png
#           grass.png
#           castle.png
#           bullet.png
#           badguy.png

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "resources", "images")


def cargar_imagen(nombre):
    """Carga una imagen ubicada en resources/images."""
    ruta = os.path.join(IMAGE_DIR, nombre)
    return pg.image.load(ruta).convert_alpha()


player = cargar_imagen("dude.png")
grass = cargar_imagen("grass.png")
castle = cargar_imagen("castle.png")
arrow = cargar_imagen("bullet.png")
badguyimg = cargar_imagen("badguy.png")


# ---------------------------------------------------------------------
# 3. Función para dibujar el paisaje
# ---------------------------------------------------------------------

def dibujar_paisaje():
    """Cubre la pantalla con pasto y dibuja los castillos."""
    # Repetimos el pasto hasta cubrir toda la ventana.
    for x in range((width // grass.get_width()) + 1):
        for y in range((height // grass.get_height()) + 1):
            screen.blit(grass, (x * grass.get_width(),
                                y * grass.get_height()))

    # Ubicamos los castillos en el lado izquierdo de la pantalla.
    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))


# ---------------------------------------------------------------------
# 4. Bucle principal del juego
# ---------------------------------------------------------------------

running = True

while running:

    # -------------------------------------------------------------
    # 4.1. Revisar los eventos del juego
    # -------------------------------------------------------------

    for event in pg.event.get():

        # Si se cierra la ventana, terminamos el juego.
        if event.type == pg.QUIT:
            running = False

        # Detectamos cuando se presiona una tecla.
        elif event.type == pg.KEYDOWN:
            if event.key in (pg.K_w, pg.K_UP):
                keys[0] = True
            elif event.key in (pg.K_a, pg.K_LEFT):
                keys[1] = True
            elif event.key in (pg.K_s, pg.K_DOWN):
                keys[2] = True
            elif event.key in (pg.K_d, pg.K_RIGHT):
                keys[3] = True

        # Detectamos cuando se deja de presionar una tecla.
        elif event.type == pg.KEYUP:
            if event.key in (pg.K_w, pg.K_UP):
                keys[0] = False
            elif event.key in (pg.K_a, pg.K_LEFT):
                keys[1] = False
            elif event.key in (pg.K_s, pg.K_DOWN):
                keys[2] = False
            elif event.key in (pg.K_d, pg.K_RIGHT):
                keys[3] = False

        # Cuando se hace clic con el mouse, creamos una flecha.
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_position = pg.mouse.get_pos()

                # Calculamos el ángulo entre el jugador y el mouse.
                angle = math.atan2(
                    mouse_position[1] - (playerpos[1] + 32),
                    mouse_position[0] - (playerpos[0] + 26)
                )

                # Guardamos el ángulo y la posición inicial de la flecha.
                arrows.append([
                    angle,
                    playerpos[0] + 32,
                    playerpos[1] + 32
                ])

                # Registramos un disparo.
                acc[1] += 1

    # -------------------------------------------------------------
    # 4.2. Actualizar la posición del jugador
    # -------------------------------------------------------------

    # El jugador se mueve 5 píxeles según las teclas presionadas.
    if keys[0]:
        playerpos[1] -= 5
    if keys[2]:
        playerpos[1] += 5
    if keys[1]:
        playerpos[0] -= 5
    if keys[3]:
        playerpos[0] += 5

    # Evitamos que el conejo salga de los límites de la pantalla.
    playerpos[0] = max(0, min(playerpos[0], width - player.get_width()))
    playerpos[1] = max(0, min(playerpos[1], height - player.get_height()))

    # -------------------------------------------------------------
    # 4.3. Dibujar el paisaje y rotar al conejo
    # -------------------------------------------------------------

    dibujar_paisaje()

    # Obtenemos la posición del mouse para calcular hacia dónde mira.
    position = pg.mouse.get_pos()

    angle = math.atan2(
        position[1] - (playerpos[1] + 32),
        position[0] - (playerpos[0] + 26)
    )

    # Convertimos el ángulo de radianes a grados y rotamos la imagen.
    playerrot = pg.transform.rotate(player, 360 - angle * 57.29)

    # Ajustamos la posición para que la rotación no desplace al jugador.
    playerpos1 = (
        playerpos[0] - playerrot.get_rect().width / 2,
        playerpos[1] - playerrot.get_rect().height / 2
    )

    screen.blit(playerrot, playerpos1)

    # -------------------------------------------------------------
    # 5. Actualizar y dibujar las flechas
    # -------------------------------------------------------------

    for bullet in arrows[:]:
        # Calculamos la velocidad horizontal y vertical de la flecha.
        velx = math.cos(bullet[0]) * 10
        vely = math.sin(bullet[0]) * 10

        # Actualizamos su posición.
        bullet[1] += velx
        bullet[2] += vely

        # Eliminamos la flecha cuando sale de la pantalla.
        if (bullet[1] < -64 or bullet[1] > width or
                bullet[2] < -64 or bullet[2] > height):
            arrows.remove(bullet)
            continue

        # Rotamos la imagen de la flecha según su ángulo.
        arrowrot = pg.transform.rotate(arrow, 360 - bullet[0] * 57.29)
        screen.blit(arrowrot, (bullet[1], bullet[2]))

    # -------------------------------------------------------------
    # 6. Crear y mover los tejones
    # -------------------------------------------------------------

    # Disminuimos el temporizador en cada vuelta del bucle.
    badtimer -= 1

    # Cuando llega a cero, aparece un nuevo tejón.
    if badtimer <= 0:
        badguys.append([width, random.randint(50, 430)])

        # A medida que avanza el juego, aparecen más seguido.
        badtimer = 100 - (badtimer1 * 2)

        if badtimer1 >= 35:
            badtimer1 = 35
        else:
            badtimer1 += 5

    # Movemos los tejones hacia la izquierda.
    for badguy in badguys[:]:
        badguy[0] -= 7

        # Si el tejón llega al castillo, reduce la salud.
        badrect = badguyimg.get_rect(topleft=(badguy[0], badguy[1]))

        if badrect.left < 64:
            healthvalue -= random.randint(5, 20)
            badguys.remove(badguy)
            continue

        # Dibujamos el tejón en su nueva posición.
        screen.blit(badguyimg, badguy)

    # -------------------------------------------------------------
    # 7. Detectar colisiones entre flechas y tejones
    # -------------------------------------------------------------

    for badguy in badguys[:]:
        badrect = badguyimg.get_rect(topleft=(badguy[0], badguy[1]))

        for bullet in arrows[:]:
            bullrect = arrow.get_rect(topleft=(bullet[1], bullet[2]))

            # Si la flecha toca al tejón, eliminamos a ambos.
            if badrect.colliderect(bullrect):
                acc[0] += 1
                badguys.remove(badguy)
                arrows.remove(bullet)
                break

    # -------------------------------------------------------------
    # 8. Actualizar la pantalla
    # -------------------------------------------------------------

    pg.display.flip()
    clock.tick(FPS)


# ---------------------------------------------------------------------
# 9. Cerrar el juego
# ---------------------------------------------------------------------

pg.quit()
sys.exit()
