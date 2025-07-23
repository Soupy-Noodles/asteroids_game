import pygame

# Base class for game objects
class CircleShape:
    def __init__(self, x, y, radius):
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def collides_with(self, other):
        # Returns True if this circle collides with another circle
        distance = self.position.distance_to(other.position)
        return distance < (self.radius + other.radius)
