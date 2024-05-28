import pygame as pg
from enemy import Enemy
import constant as c

#initilize pygame
pg.init()

#create clock 
clock = pg.time.Clock()



# create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH,c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defence")

#load image 
enemy_image = pg.image.load('assets\\enemy\\enemy_1.png').convert_alpha()

#create enemy group
enemy_group = pg.sprite.Group()

enemy = Enemy((200,300), enemy_image)
enemy_group.add(enemy)


run = True
while run:
    clock.tick(c.FPS)
    #event handler 
    for event in pg.event.get():
        #quite game
        if event.type == pg.QUIT:
            run = False
pg.quit()