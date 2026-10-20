import pygame
from circle_shape import CircleShape
from game_constants import PLAYER_BOMB_RADIUS, LINE_WIDTH, BOMB_RADIUS, BOMB_SPAWN_RATE_SECONDS, SCREEN_WIDTH, SCREEN_HEIGHT
import random


class Bomb(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, BOMB_RADIUS)
        self.spawn_timer = 0.0

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "yellow", self.position, self.radius, LINE_WIDTH)

    def spawn(self, radius: float, position: pygame.Vector2) -> None:
        shield = Bomb(position.x, position.y)

    def update(self, dt: float) -> None:
        self.spawn_timer += dt
        if self.spawn_timer > BOMB_SPAWN_RATE_SECONDS:
            self.kill()
            self.spawn_timer = 0
    
            random_x = random.randint(0, SCREEN_WIDTH - 30)
            random_y = random.randint(0, SCREEN_HEIGHT - 30)
    
            self.spawn(BOMB_RADIUS, pygame.Vector2(random_x, random_y))



class PlayerBomb(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_BOMB_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "yellow", self.position, self.radius, LINE_WIDTH)