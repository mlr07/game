import arcade

import shape
import pause

BLUE_SQUARE_SCALE = 1
GRAY_SQUARE_SCALE = 1

POS_SPEED = 0.75

TITLE = "Motion Binding"
CONTROL_MOVE = "Hold A or D to rotate the blue lines"
CONTROL_ALPHA = "Hold W or S to change alpha"
CONTROL_PAUSE = "Hit ESC to pause"


class MotionBinding(arcade.View)
    '''class for motion binding'''

    def __init__(self, width, height):
        super().__init__()
        self.sprite_list = None
        self.b_square = None
        self.width = None
        self.height = None
        aracade.set_background_color(arcade.color.WHITE)


    def setup(self):
        self.sprite_list = arcade.sprite_list()


