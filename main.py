import pygame
from game_constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroid_field import AsteroidField
from shot import Shot
from bomb import Bomb
from shield import Shield, PlayerShield
import sys

 
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"SCREEN_WIDTH : {SCREEN_WIDTH}")
    print(f"SCREEN_HEIGHT : {SCREEN_HEIGHT}")

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    game_font = pygame.font.Font(None, 30)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    bombs = pygame.sprite.Group()
    shields = pygame.sprite.Group()
    player_shields = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    Bomb.containers = (bombs, drawable)
    Shield.containers = (shields, updatable, drawable)
    PlayerShield.containers = (player_shields, updatable, drawable)

    #draw player in the middle of the screen
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    #create asteroid field
    asteroid_field = AsteroidField()
    #initialize shield spawn
    shield = Shield(-100, -100)


    while True:
        log_state()
        for event in pygame.event.get():
            #user clicks X on game window
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        shield_text = f"Shield strenght: {player.shields}"
        lives_text = f"Lives: {player.lives}"
        score_text = f"Score: {player.score}"
        bomb_text = f"Bombs: {player.bomb_count}"
        #shoot_coldown_text = f"Gun cooldown: {player.shot_cooldown}"
        #bomb_sooldown_text = f"Bomb cooldown: {player.bomb_cooldown}"

        shield_text_surface = game_font.render(shield_text, True, "white")
        lives_text_surface = game_font.render(lives_text, True, "white")
        score_text_surface = game_font.render(score_text, True, "white")
        bomb_text_surface = game_font.render(bomb_text, True, "white")
        #shoot_coldown_text_surface = game_font.render(shoot_coldown_text, True, "white")
        #bomb_sooldown_text_surface = game_font.render(bomb_sooldown_text, True, "white")

        screen.blit(shield_text_surface, (20, 20))
        #screen.blit(shoot_coldown_text_surface, (20, 40))
        screen.blit(bomb_text_surface, (20, 40))
        #screen.blit(bomb_sooldown_text_surface, (20, 80))

        screen.blit(score_text_surface, (SCREEN_WIDTH - (game_font.size(score_text)[0]+20), 20))
        screen.blit(lives_text_surface, (SCREEN_WIDTH - (game_font.size(lives_text)[0]+20), 40))
        

        #update player position
        updatable.update(dt)

        #iterate over asteroids to check for collision
        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                player.lives -= 1
                print(f"player.lives {player.lives}")
                obj.kill()
            for bullet in shots:
                if obj.collides_with(bullet):
                    log_event("asteroid_shot")
                    obj.split(player)
                    bullet.kill()
            for bomb in bombs:
                if obj.collides_with(bomb):
                    log_event("asteroid_bombed")
                    obj.split(player)
                    bomb.kill()
            for shield_obj in player_shields:
                if obj.collides_with(shield_obj):
                    log_event("shield_hit")
                    shield_obj.kill()
                    player.shield_down()
                    print(f"player.shields {player.shields}")
                    obj.split(player)

        for obj in shields:
            if obj.collides_with(player):
                log_event("shield_up")
                player.shield_up()
                print(f"player.shields {player.shields}")
                obj.kill()

        #draw objects to screen
        for obj in drawable:
            obj.draw(screen)

        #refresh screen
        pygame.display.flip()

        #time passed since last call
        dt = clock.tick(60)/1000

        if player.lives == 0:
            print("Game Over. Score:", player.score)
            sys.exit()
        

main()


__name__ == "__main__"