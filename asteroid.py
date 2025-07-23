import random
from circle_shape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape, pygame.sprite.Sprite):
    containers = ()

    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self, *self.containers)
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (200, 200, 200),
            (int(self.position.x), int(self.position.y)),
            int(self.radius),
            2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Immediately kill this asteroid
        self.kill()
        # If this is a small asteroid, don't split further
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Otherwise, split into two smaller asteroids
        random_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(random_angle) * 1.2
        v2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Spawn two new asteroids at the same position
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = v1
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = v2