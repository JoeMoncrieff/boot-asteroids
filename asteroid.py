from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.offspring = None
        self.parent = None
    
    def draw(self,window):
        pygame.draw.circle(window,"white",self.position,self.radius,2)
    
    def update(self, dt):
        self.position += dt * self.velocity
        
        # Checks for if fully off screen then delete
        if (self.position.x - self.radius > SCREEN_WIDTH and self.velocity.x > 0) or (self.position.x + self.radius < 0 and self.velocity.x < 0) or\
            (self.position.y - self.radius > SCREEN_HEIGHT and self.velocity.y > 0) or (self.position.y + self.radius < 0 and self.velocity.y <0):
            self.kill()

        # Check for going off screen here
        if (self.position.x + self.radius > SCREEN_WIDTH and self.velocity.x > 0) or (self.position.x - self.radius < 0 and self.velocity.x < 0) or\
            (self.position.y + self.radius > SCREEN_HEIGHT and self.velocity.y > 0) or (self.position.y - self.radius < 0 and self.velocity.y < 0):
            if not self.offspring:
                #Need to figure out where the asteroid is so we can loop it.
                new_x = self.position.x
                new_y = self.position.y
                if self.position.x + self.radius > SCREEN_WIDTH:
                    new_x = 0 - (SCREEN_WIDTH - self.position.x)
                elif self.position.x - self.radius < 0:
                    new_x = SCREEN_WIDTH + self.position.x
                if self.position.y + self.radius > SCREEN_HEIGHT:
                    new_y = 0 - (SCREEN_HEIGHT - self.position.y)
                elif self.position.y - self.radius < 0 and self.velocity.y < 0:
                    new_y = SCREEN_HEIGHT + self.position.y

                self.offspring = Asteroid(new_x,new_y,self.radius)
                self.offspring.velocity = self.velocity
                self.offspring.parent = self
        
    def split(self):
        if self.offspring:
            self.offspring.kill()
        if self.parent:
            self.parent.kill()
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

