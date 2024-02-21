import Constants
from Helpers import *
import numpy as np
from Tile import Tile

class Board:
    def __init__(self, screen, sprites):
        self.screen = screen
        self.tile_sprites = sprites.tile

        self.__initialize_tiles__()
        self.__initialize_limits__()
        self.__initialize_mines__()
        self.__set_adjacent_tiles__()


    def __initialize_tiles__(self):
        self.tiles = np.array([
            [
                Tile(self.tile_sprites.unopened, ((j + Constants.HORIZONTAL_OFFSET) * Constants.TILE_WIDTH, (i + Constants.VERTICAL_OFFSET) * Constants.TILE_HEIGHT +  Constants.NUMBER_HEIGHT))
                for j in range(Constants.HORIZONTAL_TILE_COUNT)
            ]
            for i in range(Constants.VERTICAL_TILE_COUNT)
        ])

        self.flattened_tiles = self.tiles.flatten()

    def __initialize_limits__(self):
        # (x_low, x_high, y_low, y_high)
        x_low = Constants.HORIZONTAL_OFFSET * Constants.TILE_WIDTH
        x_high = x_low + Constants.HORIZONTAL_TILE_COUNT * Constants.TILE_WIDTH
        y_low = Constants.VERTICAL_OFFSET * Constants.TILE_HEIGHT + Constants.NUMBER_HEIGHT
        y_high = y_low + Constants.VERTICAL_TILE_COUNT * Constants.TILE_HEIGHT
        self.limits = (x_low, x_high, y_low, y_high)

    def __initialize_mines__(self):
        all_indices = np.array(range(len(self.flattened_tiles)))
        np.random.shuffle(all_indices)
        indices = all_indices[:Constants.MINE_COUNT]
        tiles_to_make_mines = self.flattened_tiles[indices]
        for tile in tiles_to_make_mines:
            tile.set_is_mine(True)


    def __set_adjacent_tiles__(self):
        for i in range(Constants.VERTICAL_TILE_COUNT):
            for j in range(Constants.HORIZONTAL_TILE_COUNT):
                lower_bound_i = np.max([0, i - 1])
                upper_bound_i = np.min([Constants.VERTICAL_TILE_COUNT, i + 2])
                lower_bound_j = np.max([0, j - 1])
                upper_bound_j = np.min([Constants.HORIZONTAL_TILE_COUNT, j + 2])

                tile_in_question = self.tiles[i, j]
                tiles_in_range = self.tiles[lower_bound_i:upper_bound_i, lower_bound_j:upper_bound_j]
                adjacent_tiles = np.delete(tiles_in_range, np.where(tiles_in_range == tile_in_question))
                tile_in_question.set_adjacent_tiles(adjacent_tiles)
    
    def __get_tile_from_mouse_position__(self, mouse_position):
        x, y = mouse_position
        j, i = (int((x - Constants.HORIZONTAL_OFFSET * Constants.TILE_WIDTH) / Constants.TILE_WIDTH),
                  int((y - Constants.VERTICAL_OFFSET * Constants.TILE_HEIGHT - Constants.NUMBER_HEIGHT) / Constants.TILE_HEIGHT))

        return self.tiles[i, j]

    def draw(self):
        for tile in self.flattened_tiles:
            self.screen.blit(tile.get_sprite(), tile.get_position())

    def handle_click(self, mouse_position, mouse_press):
        tile = self.__get_tile_from_mouse_position__(mouse_position)
        if is_left_click(mouse_press):
            if not tile.is_shown() and not tile.is_mine():
                tile.show()
