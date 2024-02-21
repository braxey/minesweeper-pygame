import Constants
import numpy as np
from Tile import Tile

class Board:
    def __init__(self, screen, sprites):
        self.screen = screen
        self.tile_sprites = sprites.tile

        self.tiles = np.array([
            [
                Tile(self.tile_sprites.unopened, ((j + Constants.HORIZONTAL_OFFSET) * Constants.TILE_WIDTH, (i + Constants.VERTICAL_OFFSET) * Constants.TILE_HEIGHT +  Constants.NUMBER_HEIGHT))
                for j in range(Constants.HORIZONTAL_TILE_COUNT)
            ]
            for i in range(Constants.VERTICAL_TILE_COUNT)
        ])

        self.flattened_tiles = self.tiles.flatten()
        self.limits = self.__initialize_limits__()

    def __initialize_limits__(self):
        # (x_low, x_high, y_low, y_high)
        x_low = Constants.HORIZONTAL_OFFSET * Constants.TILE_WIDTH
        x_high = x_low + Constants.HORIZONTAL_TILE_COUNT * Constants.TILE_WIDTH
        y_low = Constants.VERTICAL_OFFSET * Constants.TILE_HEIGHT + Constants.NUMBER_HEIGHT
        y_high = y_low + Constants.VERTICAL_TILE_COUNT * Constants.TILE_HEIGHT
        return (x_low, x_high, y_low, y_high)
    
    def __get_tile_from_mouse_position__(self, mouse_position):
        x, y = mouse_position
        j, i = (int((x - Constants.HORIZONTAL_OFFSET * Constants.TILE_WIDTH) / Constants.TILE_WIDTH),
                  int((y - Constants.VERTICAL_OFFSET * Constants.TILE_HEIGHT - Constants.NUMBER_HEIGHT) / Constants.TILE_HEIGHT))

        return self.tiles[i, j]

    def draw(self):
        for tile in self.flattened_tiles:
            self.screen.blit(tile.sprite, tile.position)

    def handle_click(self, mouse_position):
        tile = self.__get_tile_from_mouse_position__(mouse_position)
        print(tile.position)
