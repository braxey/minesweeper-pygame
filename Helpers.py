import Constants

def is_left_click(mouse_press):
    return mouse_press[0]

def is_right_click(mouse_press):
    return mouse_press[1]

def is_click_on_board(mouse_position, board):
    return within_limits(mouse_position, board.limits)

def is_click_on_face(mouse_position, face):
    return within_limits(mouse_position, face.limits)

def within_limits(position, limits):
    x, y = position
    x_low, x_high, y_low, y_high = limits
    return x >= x_low and x <= x_high and y >= y_low and y <= y_high
