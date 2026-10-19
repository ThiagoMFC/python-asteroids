import pygame
from circle_shape import CircleShape
from game_constants import BOMB_RADIUS, LINE_WIDTH


class Bomb(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, BOMB_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "yellow", self.position, self.radius, LINE_WIDTH)