import Constants
import numpy as np
from Number import Number

class Counter:
    def __init__(self, screen, sprites):
        self.screen = screen
        self.number_sprites = sprites.number
        self.number_map = sprites.number_map

        self.__initialize_count__()
        self.__initialize_numbers__()

    def __initialize_count__(self):
        self.count = str(Constants.MINE_COUNT).rjust(3, '0')

    def __initialize_numbers__(self):
        numbers = []
        left_offset = (Constants.HORIZONTAL_OFFSET + 0.5) * Constants.TILE_WIDTH

        for i in range(len(self.count)):
            numbers += [Number(self.number_map[self.count[i]], (left_offset + i * Constants.NUMBER_WIDTH, Constants.TILE_HEIGHT))]

        self.numbers = np.array(numbers)
        self.flattened_numbers = self.numbers.flatten()

    def draw(self):
        for number in self.flattened_numbers:
            self.screen.blit(number.sprite, number.position)
