import pygame
from Sprites import Sprites
import Constants
from Board import Board
from Face import Face
from Counter import Counter
from Helpers import *

pygame.init()

SCREEN_WIDTH = (Constants.HORIZONTAL_TILE_COUNT + 2) * Constants.TILE_WIDTH
SCREEN_HEIGHT = (Constants.VERTICAL_TILE_COUNT + 3) * Constants.TILE_HEIGHT + Constants.NUMBER_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

sprites = Sprites()
board = Board(screen, sprites)
face = Face(screen, sprites)
counter = Counter(screen, sprites)

run = True
mouse_press = ''
while run:

    screen.fill((0, 0, 0))
    board.draw()
    face.draw()
    counter.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()
            if is_click_on_board(mouse_position, board):
                board.handle_click(mouse_position, mouse_press)
            elif is_click_on_face(mouse_position, face) and is_left_click(mouse_press):
                face.handle_click()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_press = pygame.mouse.get_pressed()

    pygame.display.update()

pygame.quit()
