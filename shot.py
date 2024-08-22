from circleshape import CircleShape
import pygame
from constants import *


class Shot(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def draw(self,window):
        pygame.draw.circle(window,"white",self.position,self.radius,2)
