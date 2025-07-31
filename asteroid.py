import pygame

from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def draw(self, screen):
        pygame.draw.circle()
        pygame.draw.circle(screen, "white", self.triangle(), 2)