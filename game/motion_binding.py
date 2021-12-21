import arcade
import math
import shape

BLUE_SQUARE_SCALE = 1
GRAY_SQUARE_SCALE = 1.6
SPEED = 0.75

TITLE = "Motion Binding"
CONTROL_MOVE = "Hold A or D to rotate blue lines"
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
        self.translate_angle = 0
        arcade.set_background_color(arcade.color.WHITE)


    def setup(self):
        self.sprite_list = arcade.SpriteList()

        img_blue = "./resources/blue_outline.png"
        self.b_square = shape.Shape(img_blue , BLUE_SQUARE_SCALE)
        self.b_square.center_x = self.width*0.5+10
        self.b_square.center_y = self.height*0.5
        self.b_square.angle = 45
        #self.sprite_list.append(self.b_square)
        
        # XY location of square corners, calculated in place
        coords = [
            [(self.width-400*2**(1/2))/2, self.height*0.5],
            [self.width*0.5, (self.height-400*2**(1/2))/2],
            [self.width*0.5, 400*2**(1/2)+(self.height-400*2**(1/2))/2],
            [400*2**(1/2)+(self.width-400*2**(1/2))/2,self.height*0.5],
        ]

        img_gray = "./resources/gray_square.png"
        for coord in coords:
            sqr = arcade.Sprite(img_gray, GRAY_SQUARE_SCALE)
            sqr.position = coord
            sqr.angle = 45
            self.sprite_list.append(sqr)


    def on_draw(self):
        arcade.start_render()
        self.b_square.draw()
        self.sprite_list.draw()
        arcade.draw_text(TITLE, 5, 775, (0,0,0), 18)
        arcade.draw_text(CONTROL_MOVE, 5, 30, (0,0,0), 14)
        arcade.draw_text(CONTROL_ALPHA, 5, 7, (0,0,0), 14)
        arcade.draw_text(CONTROL_PAUSE, 635, 7, (0,0,0), 14)


    def on_update(self, delta_time):
        self.b_square.update(self.width, self.height)
        self.sprite_list.update()


    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.A:
            self.b_square.translate(100, self.translate_angle, self.width, self.height)
            self.translate_angle= self.translate_angle+10
        elif key == arcade.key.D:
            pass
        elif key == arcade.key.W:
            pass
        elif key == arcade.key.S:
            pass


    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.A:
            pass
        elif key == arcade.key.D:
            pass

    def translate(self, angle):
        self.b_square.center_x = 1*math.cos(angle)
        self.b_square.center_y = 1*math.sin(angle)


def main():
    pass


if __name__ == "__main__":
    main()

