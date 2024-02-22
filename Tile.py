class Tile:
    def __init__(self, sprite_map, position):
        self.sprite_map = sprite_map
        self.sprite = sprite_map['unopened']
        self.position = position
        self.is_mine = False
        self.is_flagged = False
        self.is_shown = False

    def __set_number_of_adjacent_mines__(self):
        count = 0
        for tile in self.adjacent_tiles:
            if tile.get_is_mine(): count += 1
        self.adjacent_mine_count = count

    def get_position(self):
        return self.position
    
    def get_sprite(self):
        return self.sprite

    def get_is_shown(self):
        return self.is_shown
    
    def get_is_mine(self):
        return self.is_mine
    
    def get_is_flagged(self):
        return self.is_flagged

    def set_adjacent_tiles(self, adjacent_tiles):
        self.adjacent_tiles = adjacent_tiles
        self.__set_number_of_adjacent_mines__()

    def set_sprite(self, sprite):
        self.sprite = sprite

    def set_is_shown(self, is_shown):
        self.is_shown = is_shown

    def set_is_mine(self, is_mine):
        self.is_mine = is_mine

    def toggle_flag(self, counter):
        if self.get_is_flagged():
            self.sprite = self.sprite_map['unopened']
            counter.increment()
        elif counter.get_count_value() == 0:
            return
        else:
            self.sprite = self.sprite_map['flag']
            counter.decrement()
        self.is_flagged = not self.is_flagged
    
    def show(self, board):
        if self.get_is_flagged(): return

        board.increment_tiles_shown_count()

        self.is_shown = True
        if not self.get_is_mine():
            self.sprite = self.sprite_map[str(self.adjacent_mine_count)]
            if self.adjacent_mine_count == 0:
                for tile in self.adjacent_tiles:
                    if not tile.get_is_shown(): tile.show(board)
        else:
            self.sprite = self.sprite_map['mine_red']
