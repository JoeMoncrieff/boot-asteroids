import pygame
from asteroid import Asteroid
from player import Player
from constants import *
from asteroidfield import AsteroidField
from shot import Shot
from score import Score


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

    Player.containers = (updatable,drawable)
    Asteroid.containers = (updatable,drawable,asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable,drawable,shots)

    #Initializing variables
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    af = AsteroidField()
    score = Score()

    #Initializing Game Over text
    font = pygame.font.Font(None,64)
    
    #Game Loop start here
    run = True
    main_game = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for sprite in updatable:
            sprite.update(dt)
        if main_game:
            
            for sprite in asteroids:
                if sprite.check_collision(player):
                    print("Game Over!")
                    main_game = False
                    player.kill()
            
            for sprite in shots:
                for ast in asteroids:
                    if sprite.check_collision(ast):
                        ast.split()
                        sprite.kill()
                        score.score +=1
                    
            pygame.Surface.fill(window, color=(0,0,0))

            score.draw(window)


        else:
            pygame.Surface.fill(window, color=(0,0,0))
            
            game_over_text = f"Game Over!"
            final_score_text =  f"Final Score: {score.score}"
            got_render = font.render(game_over_text,True,"white")
            final_score_render = font.render(final_score_text, True, "white")
            pygame.surface.Surface.blit(window,got_render,((SCREEN_WIDTH-got_render.get_width())/2,(SCREEN_HEIGHT-got_render.get_height())/2))
            pygame.surface.Surface.blit(window,final_score_render,((SCREEN_WIDTH-final_score_render.get_width())/2,((SCREEN_HEIGHT-final_score_render.get_height())/2)+got_render.get_height()))

        for sprite in drawable:
                sprite.draw(window)   

            
        pygame.display.flip()
        pygame.display.update()    
        dt = clock.tick(60)/1000

    pygame.quit()

if __name__ == "__main__":
    main()