import circleshape
import pygame
from constants import *
from shot import Shot

class Player(circleshape.CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x,y)
        self.rotation = 0
        self.shoot_timer = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, window):
        pygame.draw.polygon(window,"white",self.triangle(),2)

    def rotate(self,dt):
        self.rotation += 300*dt
    
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        self.shoot_timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def shoot(self):
        if self.shoot_timer < 0:
            new_shot = Shot(self.position.x,self.position.y)
            new_shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def check_collision(self, other_circle):
        triangle_points = self.triangle()
        line_array = [[triangle_points[0],triangle_points[1]],
                      [triangle_points[2],triangle_points[0]],
                      [triangle_points[1],triangle_points[2]]]
        
        is_collided = False
        for line in line_array:
            # Calc Gradient
            line = sorted(line,key=lambda x: x.x)
            gradient = [line[1].x - line[0].x, line[1].y - line[0].y]

            # Calc reverse gradient

            reverse_gradient = [gradient[1],-gradient[0]] if gradient[1] > 0 else [-gradient[1],gradient[0]]

            # Edgecases when x or y == 0

            grad_multiple = ( (other_circle.position.y - line[0].y) * gradient[0] )/( (gradient[1]*reverse_gradient[0]) - (reverse_gradient[1]*gradient[0])) 
            # Calc shortest point
            shortest_point = pygame.Vector2(other_circle.position.x + grad_multiple*reverse_gradient[0], other_circle.position.y + grad_multiple*reverse_gradient[1])
            
            if  (line[0].x <= shortest_point.x <= line[1].y) and (min(line[0].y,line[1].y) <= shortest_point.y <= max(line[0].y,line[1].y)):
                is_collided = pygame.Vector2.distance_to(shortest_point,other_circle.position) <= other_circle.radius
            else:
                dist1 = pygame.Vector2.distance_to(line[0],other_circle.position)
                dist2 = pygame.Vector2.distance_to(line[1],other_circle.position)
                is_collided = min(dist1,dist2) <= other_circle.radius
            if is_collided:
                return True
        return False
            
            

            # Check if on line
            # Else check both end points and see if either are in collision range

