import pygame
from minesweeper import sprites

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 50, 50))

def view_scores(screen):
    monochrome = sprites.ScoreSheets(sprites.ScoreSheets.monochrome)

    builder = sprites.ScoreBuilder() # kwarg: sheet=two_thousand
    score = builder.zero(monochrome).two(monochrome).four(monochrome).build()

    screen.blit(score.zero, (13 * 0, 0))
    screen.blit(score.one, (13 * 1, 0))
    screen.blit(score.two, (13 * 2, 0))
    screen.blit(score.three, (13 * 3, 0))
    screen.blit(score.four, (13 * 4, 0))
    screen.blit(score.five, (13 * 5, 0))
    screen.blit(score.six, (13 * 6, 0))
    screen.blit(score.seven, (13 * 7, 0))
    screen.blit(score.eight, (13 * 8, 0))
    screen.blit(score.nine, (13 * 9, 0))

    tiles = score["9876543210"]
    [screen.blit(tile, (13 * idx, 23)) for idx, tile in enumerate(tiles)]

    pygame.display.update()

run = True
while run:

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), player)

    view_scores(screen)

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
