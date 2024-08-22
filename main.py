
import pygame
from asteroid import Asteroid
from player import Player
from constants import *
from asteroidfield import AsteroidField


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

    Player.containers = (updatable,drawable)
    Asteroid.containers = (updatable,drawable,asteroids)
    AsteroidField.containers = (updatable)

    #initializing player
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    af = AsteroidField()
    #Game Loop start here
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        for sprite in updatable:
            sprite.update(dt)
        
        pygame.Surface.fill(window, color=(0,0,0))

        for sprite in drawable:
            sprite.draw(window)
        
        pygame.display.update()
        
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()