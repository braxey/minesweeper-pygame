import Constants
import numpy as np
from Tile import Tile

class Board:
    def __init__(self, screen, sprites):
        self.screen = screen
        self.tiles = np.array([
            [
                Tile(sprites, ((j + 1) * Constants.TILE_WIDTH, (i + 2) * Constants.TILE_HEIGHT +  Constants.NUMBER_HEIGHT))
                for j in range(Constants.HORIZONTAL_TILE_COUNT)
            ]
            for i in range(Constants.VERTICAL_TILE_COUNT)
        ])

        self.flattened_tiles = self.tiles.flatten()

    def draw(self):
        for tile in self.flattened_tiles:
            self.screen.blit(tile.sprite, tile.position)