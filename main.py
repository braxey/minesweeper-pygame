import pygame
from minesweeper import sprites
from Sprites import Sprites
import Constants
from Board import Board

pygame.init()

# 16 tiles high, 30 tiles wide

SCREEN_WIDTH = (Constants.HORIZONTAL_TILE_COUNT + 2) * Constants.TILE_WIDTH
SCREEN_HEIGHT = (Constants.VERTICAL_TILE_COUNT + 3) * Constants.TILE_HEIGHT + Constants.NUMBER_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 50, 50))

s = Sprites()
board = Board(screen, s)
print(board.flattened_tiles.shape)

run = True
while run:

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), player)

    board.draw()

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-1, 0)
    elif key[pygame.K_d]:
        player.move_ip(1, 0)
    elif key[pygame.K_w]:
        player.move_ip(0, -1)
    elif key[pygame.K_s]:
        player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
