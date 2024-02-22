from Sprites import Sprites
from Board import Board
from Face import Face
from Helpers import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.sprites = Sprites()
        self.board = Board(screen, self.sprites)
        self.face = Face(screen, self.sprites)
        self.game_over = False

    def __reset_game__(self):
        self.board = Board(self.screen, self.sprites)
        self.face.reset()
        self.game_over = False

    def draw(self):
        self.board.draw()
        self.face.draw()

    def handle_click(self, mouse_position, mouse_press):
        if is_click_on_board(mouse_position, self.board):
            if self.game_over: return
            game_should_continue = self.board.handle_click(mouse_position, mouse_press)
        elif is_click_on_face(mouse_position, self.face) and is_left_click(mouse_press):
            self.__reset_game__()
            return
        else: game_should_continue = True

        if not game_should_continue:
            self.game_over = True
            if self.board.was_game_won():
                self.face.set_winning_sprite()
            else:
                self.face.set_losing_sprite()