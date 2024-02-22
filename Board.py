import Constants
from Helpers import *
import numpy as np
from Tile import Tile
from Counter import Counter

class Board:
    def __init__(self, screen, sprites):
        self.screen = screen
        self.tile_sprite_map = sprites.tile_sprite_map
        self.counter = Counter(screen, sprites)
        self.tiles_shown_count = 0

        self.__initialize_tiles__()
        self.__initialize_limits__()
        self.__initialize_mines__()
        self.__set_adjacent_tiles__()


    def __initialize_tiles__(self):
        self.tiles = np.array([
            [
                Tile(self.tile_sprite_map, ((j + Constants.HORIZONTAL_OFFSET) * Constants.TILE_WIDTH, (i + Constants.VERTICAL_OFFSET) * Constants.TILE_HEIGHT +  Constants.NUMBER_HEIGHT))
                for j in range(Constants.HORIZONTAL_TILE_COUNT)
            ]
            for i in range(Constants.VERTICAL_TILE_COUNT)
        ])

        self.flattened_tiles = self.tiles.flatten()

    def __initialize_limits__(self):
        x_low = Constants.HORIZONTAL_OFFSET * Constants.TILE_WIDTH
        x_high = x_low + Constants.HORIZONTAL_TILE_COUNT * Constants.TILE_WIDTH
        y_low = Constants.VERTICAL_OFFSET * Constants.TILE_HEIGHT + Constants.NUMBER_HEIGHT
        y_high = y_low + Constants.VERTICAL_TILE_COUNT * Constants.TILE_HEIGHT
        self.limits = (x_low, x_high, y_low, y_high)

    def __initialize_mines__(self):
        all_indices = np.array(range(len(self.flattened_tiles)))
        np.random.shuffle(all_indices)
        indices = all_indices[:Constants.MINE_COUNT]
        self.mines = self.flattened_tiles[indices]
        for tile in self.mines:
            tile.set_is_mine(True)

    def __set_adjacent_tiles__(self):
        for i in range(Constants.VERTICAL_TILE_COUNT):
            for j in range(Constants.HORIZONTAL_TILE_COUNT):
                adjacent = []
                for k in range(i - 1, i + 2):
                    for l in range (j - 1, j + 2):
                        if (k == i and l == j) or (k < 0 or k >= Constants.VERTICAL_TILE_COUNT) or (l < 0 or l >= Constants.HORIZONTAL_TILE_COUNT): continue
                        adjacent += [self.tiles[k, l]]
                self.tiles[i, j].set_adjacent_tiles(adjacent)
    
    def __get_tile_from_mouse_position__(self, mouse_position):
        x, y = mouse_position
        j, i = (int((x - Constants.HORIZONTAL_OFFSET * Constants.TILE_WIDTH) / Constants.TILE_WIDTH),
                  int((y - Constants.VERTICAL_OFFSET * Constants.TILE_HEIGHT - Constants.NUMBER_HEIGHT) / Constants.TILE_HEIGHT))

        return self.tiles[i, j]
    
    def __show_all_mines__(self, clicked_tile):
        for tile in self.mines:
            if tile == clicked_tile: continue

            tile.set_is_shown(True)
            if tile.get_is_flagged():
                tile.set_sprite(self.tile_sprite_map['mine_red_cross'])
            else:
                tile.set_sprite(self.tile_sprite_map['mine'])

    def __flag_all_mines__(self):
        self.counter.set_count_to_zero()
        for tile in self.mines:
            tile.set_sprite(self.tile_sprite_map['flag'])

    def was_game_won(self):
        return self.tiles_shown_count == Constants.TILE_COUNT and (len(self.mines) == 0 or not self.mines[0].get_is_shown())

    def draw(self):
        self.counter.draw()
        for tile in self.flattened_tiles:
            self.screen.blit(tile.get_sprite(), tile.get_position())

    def increment_tiles_shown_count(self):
        self.tiles_shown_count += 1

    def handle_click(self, mouse_position, mouse_press):
        tile = self.__get_tile_from_mouse_position__(mouse_position)
        if is_left_click(mouse_press):
            if not tile.get_is_shown() and not tile.get_is_flagged():
                tile.show(self)
                if tile.get_is_mine():
                    self.__show_all_mines__(tile)
                    return False
                if self.was_game_won():
                    self.__flag_all_mines__()
                    return False
        elif is_right_click(mouse_press):
            if not tile.get_is_shown():
                tile.toggle_flag(self.counter)
        return True

