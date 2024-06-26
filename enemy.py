import pygame as pg
from pygame.math import Vector2
import math
import constant as c
class Enemy(pg.sprite.Sprite):
    def __init__(self, waypoints, image):
        pg.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.speed = 2
        self.angle = 0
        self.original_image = image
        self.image = pg.transform.rotate(self.original_image,self.angle )
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        
    def update(self):
        self.move()
        self.rotate()
        
    def move(self):
        #define a target wavepoint 
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        else:
            #enemy arrive at final point
            self.kill()
        #calculate target distance
        dist = self.movement.length()
    
        #check the remaining dstance greater than enemy speed
        if dist >= self.speed:
            self.pos += self.movement.normalize() * self.speed
        else:
            if dist != 0:
                self.pos += self.movement.normalize() * dist
            self.target_waypoint += 1

                
    
    def rotate(self):
        #calculate distance of next waypoint
        dist = self.target - self.pos
        
        #calculate angle
        self.angle = math.degrees(math.atan2(-dist.y, dist.x))
        #rotate angle and update image
        self.image = pg.transform.rotate(self.original_image,self.angle )
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        