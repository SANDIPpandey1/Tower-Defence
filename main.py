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


waypoints = [
    (100, 100),
    (400, 200),
    (400, 100),
    (200, 300)
]

enemy = Enemy(waypoints, enemy_image)
enemy_group.add(enemy)


run = True
while run:
    clock.tick(c.FPS)
    
    #fill screen with color
    screen.fill("white")
    
    #draw enemy path
    pg.draw.lines(screen, "grey0", False, waypoints)
    
    
    #update group
    enemy_group.update()
    
    
    
    #draw a group
    enemy_group.draw(screen)
    
    
    
    #event handler 
    for event in pg.event.get():
        
        #quite game
        if event.type == pg.QUIT:
            run = False
            
            
    #update display
    pg.display.flip()
pg.quit()