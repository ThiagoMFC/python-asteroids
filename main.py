import pygame
from game_constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroid_field import AsteroidField
from shot import Shot
import sys

 
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"SCREEN_WIDTH : {SCREEN_WIDTH}")
    print(f"SCREEN_HEIGHT : {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    #draw player in the middle of the screen
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    #create asteroid field
    asteroid_field = AsteroidField()


    while True:
        log_state()
        for event in pygame.event.get():
            #user clicks X on game window
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        #update player position
        updatable.update(dt)

        #iterate over asteroids to check for collision
        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                print("game over")
                sys.exit()

        #draw objects to screen
        for obj in drawable:
            obj.draw(screen)

        #refresh screen
        pygame.display.flip()

        #time passed since last call
        dt = clock.tick(60)/1000
        

main()


__name__ == "__main__"