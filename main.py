import pygame
from asteroid import Asteroid, AsteroidDecoration
from player import Player
from constants import *
from asteroidfield import AsteroidField
from shot import Shot
from score import Score
from button import Button
from controller import Controller

def main():
    pygame.init()

    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    clock = pygame.time.Clock()
    dt = 0

    #Initialising update and draw groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    ui_drawable = pygame.sprite.Group()

    c = Controller(\
        updatable=updatable,\
        drawable=drawable,\
        asteroids=asteroids,\
        shots=shots,\
        ui_drawable = ui_drawable
        )
    
    Player.containers = (c.updatable,c.drawable)
    Asteroid.containers = (c.updatable,c.drawable,c.asteroids)
    AsteroidField.containers = (c.updatable)
    Shot.containers = (c.updatable,c.drawable,c.shots)
    Button.containers = (c.ui_drawable,c.updatable)
    Score.containers = (c.ui_drawable)
    

    #Initializing variables
    c.player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    c.asteroidfield = AsteroidField()
    c.score = Score()
    restart_button = None

    font = pygame.font.Font(None,64)
    
    run = True
    c.main_game = True
    
    #Game Loop start here
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for sprite in c.updatable:
            sprite.update(dt)
        
        pygame.Surface.fill(window, color=(0,0,0))

        if c.main_game:
            
            for sprite in c.asteroids:
                if sprite.check_collision(c.player):
                    if c.player.check_collision(sprite):
                        print("Game Over!")
                        c.main_game = False
                        
                        #Set up code for Game Over Screen
                        c.player.kill()
                        restart_button = Button(SCREEN_WIDTH/2 -100,SCREEN_HEIGHT/2 +75,200,100,"Restart?",c,restart_game)
                        
            
            for sprite in c.shots:
                for ast in c.asteroids:
                    if sprite.check_collision(ast):
                        ast.split()
                        sprite.kill()
                        c.score.score +=1
            
            for sprite in c.drawable:
                sprite.draw(window)
                    
        else:

            for sprite in c.drawable:
                sprite.draw(window)

            game_over_text = f"Game Over!"
            final_score_text =  f"Final Score: {c.score.score}"
            got_render = font.render(game_over_text,True,"white")
            final_score_render = font.render(final_score_text, True, "white")
            pygame.surface.Surface.blit(window,got_render,((SCREEN_WIDTH-got_render.get_width())/2,(SCREEN_HEIGHT-got_render.get_height())/2))
            pygame.surface.Surface.blit(window,final_score_render,((SCREEN_WIDTH-final_score_render.get_width())/2,((SCREEN_HEIGHT-final_score_render.get_height())/2)+got_render.get_height()))
  
        for sprite in ui_drawable:
            sprite.draw(window)
   
        pygame.display.flip()
        pygame.display.update()    
        dt = clock.tick(60)/1000

    pygame.quit()

def restart_game(controller):
    controller.main_game = True
    for a in controller.asteroids:
        a.kill()
    controller.player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    controller.score.score = 0
    

if __name__ == "__main__":
    main()