import arcade

TITLE = "Arrow Lengths"
CONTROL_IN = "Hold W to move arrows together"
CONTROL_OUT = "HOlD S to move arrows apart"
CONTROL_SPEED = 1

#TODO: inherit screen dims from start menu


#NOTE: this class could probably just use the base shape
class Arrow(arcade.Sprite):
    '''extended class for arrow sprites'''

    def update(self):
        '''move arrow sprite and check for out of bounds'''
        self.center_y += self.change_y

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > 800-1:
            self.top = 800-1


class ArrowLengths(arcade.View):
    '''class for arrow length illusions'''

    def __init__(self):
        super().__init__()
        self.outer_arrow = None
        self.inner_arrow = None
        arcade.set_background_color(arcade.color.WHITE)

    
    def setup(self):
        self.outer_arrow = Arrow("./resources/outer_arrow.png")
        self.outer_arrow.center_x = 800*0.5
        self.outer_arrow.center_y = 800*0.7

        self.inner_arrow = Arrow("./resources/inner_arrow.png")
        self.inner_arrow.center_x = 800*0.5
        self.inner_arrow.center_y = 800*0.3


    def on_draw(self):
        arcade.start_render()
        self.outer_arrow.draw()
        self.inner_arrow.draw()


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
