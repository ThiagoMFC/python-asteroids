import pygame
from circle_shape import CircleShape
from game_constants import LINE_WIDTH, SHIELD_RADIUS, SHIELD_SPAWN_RATE_SECONDS, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SHIELD_RADIUS, SHIELD_WIDTH_STRONG, SHIELD_WIDTH_MEDIUM, SHIELD_WIDTH_WEAK, PLAYER_SPEED
import random


class Shield(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHIELD_RADIUS)
        self.spawn_timer = 0.0

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "cyan", self.position, self.radius, LINE_WIDTH)

    def spawn(self, radius: float, position: pygame.Vector2) -> None:
        shield = Shield(position.x, position.y)

    def update(self, dt: float) -> None:
        self.spawn_timer += dt
        if self.spawn_timer > SHIELD_SPAWN_RATE_SECONDS:
            self.kill()
            self.spawn_timer = 0

            random_x = random.randint(0, SCREEN_WIDTH - 30)
            random_y = random.randint(0, SCREEN_HEIGHT - 30)

            self.spawn(SHIELD_RADIUS, pygame.Vector2(random_x, random_y))


class PlayerShield(CircleShape):
    def __init__(self, player_obj) -> None:
       super().__init__(player_obj.position[0], player_obj.position[1], PLAYER_SHIELD_RADIUS)
       
       self.player = player_obj
       

    def draw(self, screen: pygame.Surface) -> None:
        if self.player.shields == 3:
            pygame.draw.circle(screen, "cyan", self.position, self.radius, SHIELD_WIDTH_STRONG)
        if self.player.shields == 2:
            pygame.draw.circle(screen, "cyan", self.position, self.radius, SHIELD_WIDTH_MEDIUM)
        if self.player.shields == 1:
            pygame.draw.circle(screen, "cyan", self.position, self.radius, SHIELD_WIDTH_WEAK)

    def spawn(self, radius: float) -> None:
        shield = PlayerShield(self.player.position[0], self.player.position[1])

    def update(self, dt: float):
        self.position = pygame.Vector2(self.player.position)

    