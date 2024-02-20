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