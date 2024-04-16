# This code was written using the following tutorial as a baseline:
# https://www.101computing.net/pong-tutorial-using-pygame-adding-the-paddles/

import pygame

class Paddle(pygame.sprite.Sprite):
    # This class represents a paddle. It derives from the "Sprite" class in Pygame.
    # See this reference for more info on the "Sprite" class in Pygame:
    # https://www.pygame.org/docs/ref/sprite.html?highlight=sprite#pygame.sprite.Sprite
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill("black")
        self.image.set_colorkey("black")

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
