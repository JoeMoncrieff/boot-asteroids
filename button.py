import pygame
from constants import *

class Button(pygame.sprite.Sprite):
    def __init__(self,x,y, width, height, text,controller,onclick):
        
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.surf = pygame.Surface([width,height], pygame.SRCALPHA)
        self.surf.fill(pygame.Color(0,0,0,0))
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.coords = pygame.Rect(self.x,self.y,self.width,self.height)

        self.rect_transparency = 0
        self.font = pygame.font.Font(None,60)
        self.text = text
        self.text_colour = "white"

        self.pressed = False
        self.onclick = onclick
        self.controller = controller

    
    def draw(self,window):

        pygame.draw.rect(self.surf,(255,255,255,self.rect_transparency),self.rect)
        pygame.draw.rect(self.surf,"white",self.rect,width=2)
        txt = self.font.render(self.text,True,self.text_colour)
        self.surf.blit(txt,(self.rect.centerx - txt.get_width()/2 ,self.rect.centery - txt.get_height()/2))

        window.blit(self.surf,self.coords)
        

    def update(self,dt):
        mouse_position = pygame.mouse.get_pos()
        if self.coords.collidepoint(mouse_position):
            self.rect_transparency = 255
            self.text_colour = "black"
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    self.onclick(self.controller)
                    self.kill()
                    self.pressed = False
        else:
            self.rect_transparency = 0
            self.text_colour = "white"
        