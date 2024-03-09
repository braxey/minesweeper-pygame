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
        self.count_value = Constants.MINE_COUNT
        self.count = str(Constants.MINE_COUNT).rjust(Constants.NUMBER_COUNT, '0')

    def __initialize_numbers__(self):
        numbers = []
        left_offset = (Constants.HORIZONTAL_OFFSET + 0.5) * Constants.TILE_WIDTH

        for i in range(len(self.count)):
            numbers += [Number(self.number_map[self.count[i]], (left_offset + i * Constants.NUMBER_WIDTH, Constants.TILE_HEIGHT))]

        self.numbers = np.array(numbers)
        self.flattened_numbers = self.numbers.flatten()

    def __update_counter_with_count_value__(self):
        self.count = str(self.count_value).rjust(3, '0')
        for i in range(len(self.numbers)):
            self.numbers[i].set_sprite(self.number_map[self.count[i]])

    def get_count_value(self):
        return self.count_value

    def increment(self):
        self.count_value += 1
        self.__update_counter_with_count_value__()

    def decrement(self):
        self.count_value -= 1
        self.__update_counter_with_count_value__()

    def set_count_to_zero(self):
        self.count_value = 0
        self.__update_counter_with_count_value__()

    def draw(self):
        for number in self.flattened_numbers:
            self.screen.blit(number.sprite, number.position)
