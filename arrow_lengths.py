import arcade

TITLE = "Arrow Lengths"
CONTROL_IN = "Hold W to move arrows together"
CONTROL_OUT = "HOlD S to move arrows apart"

#TODO: inherit screen dims from start menu

#NOTE: this class could probably just use the base shape
class Arrow(arcade.Sprite):
    '''extended class for arrows'''

    def update(self):
        '''move arrow sprite and check for out of bounds'''
        self.center_y += self.change_y

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > 800-1:
            self.top = SCREEN_HEIGHT-1


class ArrowLengths(arcade.View):
    '''class for arrow length illusions'''

    def __init__(self):
        super().__init()
        self.outer_arrow = None
        self.inner_arrow = None
        arcade.set_background_color(arcade.color.WHITE)

    
    def setup(self):
        self.outer_arrow = arcade.Sprite("./resources/outer_arrow.png")
        self.outer_arrow.center_x = 800/2
        self.outer_arrow.center_y = 800/2


    def on_draw(self):
        arcade.start_render()


    def on_update(self):
        pass

