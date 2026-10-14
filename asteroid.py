import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)

        one = self.velocity.rotate(new_angle)
        two = self.velocity.rotate(-new_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = one * 1.2
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two.velocity = two * 1.2
