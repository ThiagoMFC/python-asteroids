import pygame
from game_constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

 
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"SCREEN_WIDTH : {SCREEN_WIDTH}")
    print(f"SCREEN_HEIGHT : {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pygame.event.get():
            #user clicks X on game window
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        #refresh screen
        pygame.display.flip()

main()


__name__ == "__main__"