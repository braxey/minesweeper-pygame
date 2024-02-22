import pygame
import Constants
from Game import Game
from Helpers import *

pygame.init()

SCREEN_WIDTH = (Constants.HORIZONTAL_TILE_COUNT + 2) * Constants.TILE_WIDTH
SCREEN_HEIGHT = (Constants.VERTICAL_TILE_COUNT + 3) * Constants.TILE_HEIGHT + Constants.NUMBER_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

game = Game(screen)

run = True
mouse_press = ''
while run:

    screen.fill((0, 255, 255))
    game.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()
            game.handle_click(mouse_position, mouse_press)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_press = pygame.mouse.get_pressed()

    pygame.display.update()

pygame.quit()
