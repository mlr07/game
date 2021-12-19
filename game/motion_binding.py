import arcade

import shape
import pause

BLUE_SQUARE_SCALE = 1
GRAY_SQUARE_SCALE = 1

POS_SPEED = 0.75

TITLE = "Motion Binding"
CONTROL_MOVE = "Hold A or D to move the blue lines"
CONTROL_ALPHA = "Hold W or S to change alpha"
CONTROL_PAUSE = "Hit ESC to pause"


class MotionBinding(arcade.View):
    '''class for motion binding'''

    def __init__(self, width, height):
        super().__init__()
        self.sprite_list = None
        self.b_square = None
        self.width = width
        self.height = height
        arcade.set_background_color(arcade.color.WHITE)


    def setup(self):
        self.sprite_list = arcade.SpriteList()

        img_blue = "./resources/blue_outline.png"
        self.b_square = arcade.Sprite(img_blue , BLUE_SQUARE_SCALE)
        self.b_square.center_x = self.width*0.5
        self.b_square.center_y = self.height*0.5
        # change angle
        self.sprite_list.append(self.b_square)

        # coords need updating
        coords = [
            [self.width*0.25,self.height*0.25],
            [self.width*0.75,self.height*0.25],
            [self.width*0.25,self.height*0.75],
            [self.width*0.75,self.height*0.75]
        ]

        #img_orng = "./resources/gray_outline.png"
        #for coord in coords:
        #    sqr = shape.Shape(img_orng, ORANGE_SQUARE_SCALE)
        #    sqr.position = coord
        #    # change angle
        #    self.sprite_list.append(sqr)


    def on_draw(self):
        arcade.start_render()
        self.sprite_list.draw()
        arcade.draw_text(TITLE, 5, 775, (0,0,0), 18)
        arcade.draw_text(CONTROL_MOVE, 5, 30, (0,0,0), 14)
        arcade.draw_text(CONTROL_ALPHA, 5, 7, (0,0,0), 14)
        arcade.draw_text(CONTROL_PAUSE, 635, 7, (0,0,0), 14)


    def on_update(self, delta_time):
        pass


    def on_key_press(self, key, key_modifiers):
        pass


    def on_key_release(self, key, key_modifiers):
        pass


def main():
    pass


if __name__ == "__main__":
    main()

