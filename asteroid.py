import pygame
from circle_shape import CircleShape
from game_constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "green", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self, player):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            player.increase_score(100)
            return

        log_event("asteroid_split")
        #generate a random angle between 20 and 50 degrees
        angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(angle)
        velocity2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid1.velocity = velocity1 * 1.2
        new_asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid2.velocity = velocity2 * 1.2
        player.increase_score(50)
