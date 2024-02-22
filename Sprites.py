from minesweeper import sprites

class Sprites:
    def __init__(self):
        tile_two_thousand = sprites.TileSheets(sprites.TileSheets.two_thousand)
        tile_builder = sprites.TileBuilder(tile_two_thousand)
        self.tile = tile_builder.build()

        number_builder = sprites.ScoreBuilder() # kwarg: sheet=two_thousand
        self.number = number_builder.build()

        face_two_thousand = sprites.FaceSheets(sprites.FaceSheets.two_thousand)
        face_builder = sprites.FaceBuilder(face_two_thousand)
        self.face = face_builder.build()

        self.__initialize_number_map__()
        self.__initialize_tile_sprite_map__()

    def __initialize_number_map__(self):
        self.number_map = {
            '0': self.number.zero,
            '1': self.number.one,
            '2': self.number.two,
            '3': self.number.three,
            '4': self.number.four,
            '5': self.number.five,
            '6': self.number.six,
            '7': self.number.seven,
            '8': self.number.eight,
            '9': self.number.nine
        }

    def __initialize_tile_sprite_map__(self):
        self.tile_sprite_map = {
            'unopened'      : self.tile.unopened,
            'flag'          : self.tile.flag,
            'mine'          : self.tile.mine,
            'mine_red'      : self.tile.mine_red,
            'mine_red_cross': self.tile.mine_red_cross,
            '0'             : self.tile.empty,
            '1'             : self.tile.one,
            '2'             : self.tile.two,
            '3'             : self.tile.three,
            '4'             : self.tile.four,
            '5'             : self.tile.five,
            '6'             : self.tile.six,
            '7'             : self.tile.seven,
            '8'             : self.tile.eight
        }
