import pygame
import math

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):

    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    
    def is_colliding(self, other_circle):
        distance = self.position.distance_to(other_circle)
        return distance < self.radius + other_circle.radius

    
    def calculate_distance(self, other_circle):
        x1 = self.position[0]
        x2 = other_circle.position[0]

        y1 = self.position[1]
        y2 = other_circle.position[1]

        distance = math.sqrt((
            math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2)
        ))

        return distance