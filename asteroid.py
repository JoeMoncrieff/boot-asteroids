from circleshape import CircleShape
import pygame
from constants import *
import random
import math

class Asteroid(CircleShape):

    def __init__(self, x, y, radius,create_lumps = True):
        super().__init__(x,y,radius)
        self.offspring = None
        self.parent = None
        
        self.decorations = []
        #TODO: If of a certain size add babies on the outside
        #Fill over the top with black so it looks like one asteroid.
        
        if create_lumps:
            number_of_iterations = random.randint(3,7)
            for i in range(0,number_of_iterations):
                if radius >= ASTEROID_MIN_RADIUS * 2:
                    random_angle = random.randint(0,360)
                    x_offset = math.sin(random_angle*180/math.pi) * (radius - (ASTEROID_MIN_RADIUS*1/2)) 
                    y_offset = math.cos(random_angle*180/math.pi) * (radius - (ASTEROID_MIN_RADIUS*1/2)) 
                    self.decorations.append(AsteroidDecoration(x_offset,y_offset,ASTEROID_MIN_RADIUS,main_asteroid=self))
            

    
    def draw(self,window):
        pygame.draw.circle(window,"white",self.position,self.radius,2)
        for d in self.decorations:
            d.draw(window)
        pygame.draw.circle(window,"black",self.position,self.radius-2)
    
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
                can_make = True
                if self.parent:
                    if self.parent.alive():
                        can_make = False
                if can_make:
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

                    self.offspring = Asteroid(new_x,new_y,self.radius,create_lumps=False)
                    self.offspring.velocity = self.velocity
                    self.offspring.parent = self
                    
                    #Incorrect doesn't pass the things in the array by value
                    for d in self.decorations:
                        self.offspring.decorations.append(d.make_copy(self.offspring))
        
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
            ast2.velocity = vec.rotate(-deg) * 1.2


class AsteroidDecoration():

    def __init__(self,x_offset,y_offset,radius,main_asteroid):
        
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.radius = radius
        self.main_asteroid = main_asteroid
        self.position = pygame.Vector2(x_offset,y_offset)
    
    def draw(self, window):

        pygame.draw.circle(window,"black",self.main_asteroid.position + self.position,self.radius)
        pygame.draw.circle(window,"white",self.main_asteroid.position + self.position,self.radius,2)
    
    def make_copy(self,new_main):
        return AsteroidDecoration(self.x_offset,self.y_offset,self.radius,new_main)

