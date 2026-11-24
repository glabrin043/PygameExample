import pygame as pg
import os
import random

pg.init()

width, heigth = 840,480
screen = pg.display.set_mode(width,heigth)
keys = [False, False, False, False]
playerpos=[100,100]

badtimer=100
badtimer1=0
badguys=[[640,100]]
healthvalue=194

badguyimg1 = pygame.image.load("resources/images/badguy.png")
badguyimg=badguyimg1

path_player_image = os.path.join("resources", "images", "dude.png")
player = pygame.image.load(path_player_image)

grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")


for x in range(int(width/grass.get_width()+1)):
        for y in range(int(height/grass.get_height()+1)):
            screen.blit(grass,(x*100,y*100))
            
screen.blit(castle,(0,30))
screen.blit(castle,(0,135))
screen.blit(castle,(0,240))
screen.blit(castle,(0,345 ))

while 1:
    screen.fill(0) #Colocar en color negro el fondo de pantalla
    screen.blit(player, playerpos)
    badtimer-=1
    acc=[0,0]
    arrows=[]
    
    for bullet in arrows:
        index=0
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        index+=1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))

    pg.display.flip() 

    for event in pg.event.get():
        if event.type == pg.QUIT
            pg.quit()
            exit
        
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
                
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False

        if keys[0]:
                playerpos[1]-=5
        elif keys[2]:
                playerpos[1]+=5
        if keys[1]:
                playerpos[0]-=5
        elif keys[3]:
                playerpos[0]+=5

        if event.type==pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            acc[1]+=1
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])

        if badtimer==0:
        badguys.append([640, random.randint(50,430)])
        badtimer=100-(badtimer1*2)
        if badtimer1>=35:
            badtimer1=35
        else:
            badtimer1+=5
        index=0

        for badguy in badguys:
        if badguy[0]<-64:
            badguys.pop(index)
        badguy[0]-=7
        index+=1
        for badguy in badguys:
        screen.blit(badguyimg, badguy)

        # 6.3.1 - Attack castle
        badrect=pygame.Rect(badguyimg.get_rect())
        badrect.top=badguy[1]
        badrect.left=badguy[0]
        if badrect.left<64:
            healthvalue -= random.randint(5,20)
            badguys.pop(index)
        # 6.3.3 - Next bad guy

        index1=0
        for bullet in arrows:
            bullrect=pygame.Rect(arrow.get_rect())
            bullrect.left=bullet[1]
            bullrect.top=bullet[2]
            if badrect.colliderect(bullrect):
                acc[0]+=1
                badguys.pop(index)
                arrows.pop(index1)
            index1+=1




    
