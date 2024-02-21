#tile (sprite, position)


class Tile:
    def __init__(self, sprite, position):
        self.sprite = sprite
        self.position = position
        self.is_mine = False
        self.is_flagged = False
        self.is_shown = False

    def get_position(self):
        return self.position
    
    def get_sprite(self):
        return self.sprite

    def is_shown(self):
        return self.is_shown
    
    def is_mine(self):
        return self.is_mine
    
    def is_flagged(self):
        return self.is_flagged

    def set_adjacent_tiles(self, adjacent_tiles):
        self.adjacent_tiles = adjacent_tiles

    def set_is_mine(self, is_mine):
        self.is_mine = is_mine        
