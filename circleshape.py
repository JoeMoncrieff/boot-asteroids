import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collision(self, other_circle):

        if abs(self.position.distance_to(other_circle.position)) < self.radius + other_circle.radius:
            #print(f"self.position.distance_to(other_circle.position): {self.position.distance_to(other_circle.position)}")
            #print(f"self.radius: {self.radius}")
            #print(f"other.radius: {other_circle.radius}")
            return True

        return False