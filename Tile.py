import Constants
#tile (sprite, position)


class Tile:
    def __init__(self, sprites, position):
        self.sprite = sprites.tile.unopened
        self.position = position