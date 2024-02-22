import Constants

class Face:
    def __init__(self, screen, sprites):
        self.screen = screen
        self.face_sprites = sprites.face

        self.sprite = self.face_sprites.smile
        self.position = self.__initialize_position__()
        self.limits = self.__initialize_limits__()

    def __initialize_position__(self):
        y = (Constants.VERTICAL_OFFSET * Constants.TILE_HEIGHT + Constants.NUMBER_HEIGHT) / 2 - Constants.FACE_HEIGHT / 2
        x = self.screen.get_width() / 2 - Constants.FACE_WIDTH / 2
        return (x, y)

    def __initialize_limits__(self):
        x, y = self.position
        return (x, x + Constants.FACE_WIDTH, y, y + Constants.FACE_HEIGHT)

    def draw(self):
        self.screen.blit(self.sprite, self.position)

    def reset(self):
        self.sprite = self.face_sprites.smile

    def set_winning_sprite(self):
        self.sprite = self.face_sprites.winner

    def set_losing_sprite(self):
        self.sprite = self.face_sprites.dead
