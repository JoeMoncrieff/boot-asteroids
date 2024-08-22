from constants import *
import pygame


class Score():
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None,48)
        
    
    def draw(self, window):
        text = self.font.render(f"Score: {self.score}",True,"White")
        pygame.surface.Surface.blit(window,text,(10,10))