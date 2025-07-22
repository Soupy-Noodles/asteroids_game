import pygame
from circle_shape import CircleShape

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