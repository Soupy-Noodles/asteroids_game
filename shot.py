import pygame
from circle_shape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape, pygame.sprite.Sprite):
    containers = ()

    def __init__(self, x, y, velocity):
        pygame.sprite.Sprite.__init__(self, *self.containers)
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 0),  # yellow
            (int(self.position.x), int(self.position.y)),
            int(self.radius),
            2
        )

    def update(self, dt):
        self.position += self.velocity * dt