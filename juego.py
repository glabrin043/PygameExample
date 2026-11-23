import pygame as pg
import os

pg.init()

width, heigth = 840,480
screen = pg.display.set_mode(width,heigth)

path_image = os.path.join("examples", "data", "alien1.png")
player = pygame.image.load(path_image)

while 1:
    screen.fill(0) #Colocar en color negro el fondo de pantalla
    screen.blit(player,100,100) #Coloca la imagen del jugar en x=100 , y=100
    pg.display.flip() 

    for event in pg.event.get():
        if event.type == pg.QUIT
            pg.quit()
            exit
