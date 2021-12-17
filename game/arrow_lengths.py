import arcade

import shape
import pause

TITLE = "Arrow Lengths"
CONTROL_IN = "Hold W to move arrows together"
CONTROL_OUT = "Hold S to move arrows apart"
CONTROL_SPEED = 1.5
CONTROL_PAUSE = "Hit ESC to pause"


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
        self.outer_arrow = shape.Shape("./resources/outer_arrow.png")
        self.outer_arrow.center_x = self.width*0.5 
        self.outer_arrow.center_y = self.height*0.7

        self.inner_arrow = shape.Shape("./resources/inner_arrow.png")
        self.inner_arrow.center_x = self.width*0.5
        self.inner_arrow.center_y = self.height*0.3


    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        self.outer_arrow.draw()
        self.inner_arrow.draw()

        arcade.draw_text(TITLE, 5, 775, (0,0,0), 18)
        arcade.draw_text(CONTROL_IN, 5, 30, (0,0,0), 14)
        arcade.draw_text(CONTROL_OUT, 5, 7, (0,0,0), 14)
        arcade.draw_text(CONTROL_PAUSE, 635, 7, (0,0,0), 14)


    def on_update(self, delta_time):
        self.outer_arrow.update(self.width, self.height)
        self.inner_arrow.update(self.width, self.height)

    
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.W:
            self.outer_arrow.change_y = CONTROL_SPEED
            self.inner_arrow.change_y = -CONTROL_SPEED
        
        elif key == arcade.key.S:
            self.outer_arrow.change_y = -CONTROL_SPEED
            self.inner_arrow.change_y = CONTROL_SPEED

        elif key == arcade.key.ESCAPE:
            pause_scr = pause.Pause(self, self.width, self.height)
            self.window.show_view(pause_scr)


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
