# This game was made in part by following the tutorial to create a pong game
# using pygame at:
# https://www.101computing.net/pong-tutorial-using-pygame-getting-started/

import pygame
from objects.paddle import Paddle

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # draw net, the vertical bar throught the center of the screen
    pygame.draw.line(screen, "white", [screen.get_width() / 2, 0],
                     [screen.get_width() / 2, screen.get_height() ], 5)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

