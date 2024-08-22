from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self,window):
        pygame.draw.circle(window,"white",self.position,self.radius,2)
    
    def update(self, dt):
        self.position += dt * self.velocity

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            deg = random.uniform(20,50)
            vec = self.velocity
            ast1 = Asteroid(self.position.x,self.position.y,self.radius - ASTEROID_MIN_RADIUS)
            ast2 = Asteroid(self.position.x,self.position.y,self.radius - ASTEROID_MIN_RADIUS)
            ast1.velocity = vec.rotate(deg) * 1.2
            ast2.velocity = vec.rotate(-deg) *1.2

