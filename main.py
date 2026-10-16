import pygame
from game_constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

 
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
    Player.containers = (updatable, drawable)

    #draw player in the middle of the screen
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


    while True:
        log_state()
        for event in pygame.event.get():
            #user clicks X on game window
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        #update player position
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        #player.draw(screen)

        #refresh screen
        pygame.display.flip()

        #time passed since last call
        dt = clock.tick(60)/1000
        

main()


__name__ == "__main__"