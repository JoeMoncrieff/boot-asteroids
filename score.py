from constants import *
import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.score = 0
        self.font = pygame.font.Font(None,48)
        
    def draw(self, window):
        text = self.font.render(f"Score: {self.score}",True,"White")
        pygame.surface.Surface.blit(window,text,(10,10))