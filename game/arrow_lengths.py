import arcade
from shape import Shape

TITLE = "Arrow Lengths"
CONTROL_IN = "Hold W to move arrows together"
CONTROL_OUT = "Hold S to move arrows apart"
CONTROL_SPEED = 1.5


class ArrowLengths(arcade.View):
    '''class for arrow length illusions'''

    def __init__(self, width, height):
        super().__init__()
        self.outer_arrow = None
        self.inner_arrow = None
        self.width = width
        self.height = height
        arcade.set_background_color(arcade.color.WHITE)

    
    def setup(self):
        self.outer_arrow = Shape(self.width, self.height, "./resources/outer_arrow.png")
        self.outer_arrow.center_x = self.width*0.5
        self.outer_arrow.center_y = self.height*0.7

        self.inner_arrow = Shape(self.width, self.height, "./resources/inner_arrow.png")
        self.inner_arrow.center_x = self.width*0.5
        self.inner_arrow.center_y = self.height*0.3


    def on_draw(self):
        arcade.start_render()
        self.outer_arrow.draw()
        self.inner_arrow.draw()

        arcade.draw_text(TITLE, 5, 775, (0,0,0), 18)
        arcade.draw_text(CONTROL_IN, 5, 30, (0,0,0), 14)
        arcade.draw_text(CONTROL_OUT, 5, 7, (0,0,0), 14)


    def on_update(self, delta_time):
        self.outer_arrow.update()
        self.inner_arrow.update()

    
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.W:
            self.outer_arrow.change_y = CONTROL_SPEED
            self.inner_arrow.change_y = -CONTROL_SPEED
        
        elif key == arcade.key.S:
            self.outer_arrow.change_y = -CONTROL_SPEED
            self.inner_arrow.change_y = CONTROL_SPEED


    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.outer_arrow.change_y = 0
            self.outer_arrow.change_y = 0
        if key == arcade.key.W or key == arcade.key.S:
            self.inner_arrow.change_y = 0
            self.inner_arrow.change_y = 0


def main():
    pass


if __name__ == "__main__":
    main()
