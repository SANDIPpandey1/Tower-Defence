import pygame as pg
from pygame.math import Vector2
import constant as c
class Enemy(pg.sprite.Sprite):
    def __init__(self, waypoints, image):
        pg.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.speed = 2
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        
    def update(self):
        self.move()
        
    def move(self):
        #define a target wavepoint 
        self.target = Vector2(self.waypoints[self.target_waypoint])
        self.movement = self.target - self.pos
        #calculate target distance
        dist = self.movement.length()
    
        #check the remaining dstance greater than enemy speed
        if dist >= self.speed:
            self.pos += self.movement.normalize() * self.speed
        self.rect.center = self.pos      