import arcade

import shape
import pause

from random import randint

TITLE = "Moving Bird"
CONTROL_CAMO = "Hit Q to toggle camo"
CONTROL_BIRD = "Hit E to move bird"


class HiddenBird(arcade.View):
    '''class for hidden bird illusion'''

    def __init__(self, width, height):
        super().__init__()
        self.camo = None
        self.bird = None
        self.width = width
        self.height = height
        arcade.set_background_color(arcade.color.WHITE)

    
    def setup(self):
        self.camo = arcade.Sprite("./resources/camo.png")
        self.camo.center_x = self.width*0.5 
        self.camo.center_y = self.height*0.5

        self.bird = shape.Shape("./resources/bird.png")
        self.bird.center_x = self.width*0.5
        self.bird.center_y = self.height*0.3


    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        self.camo.draw()
        self.bird.draw()

        arcade.draw_text(TITLE, 5, 775, (0,0,0), 18)
        arcade.draw_text(CONTROL_CAMO, 5, 30, (0,0,0), 14)
        arcade.draw_text(CONTROL_BIRD, 5, 7, (0,0,0), 14)


    def on_update(self, delta_time):
        self.camo.update()
        self.bird.update(self.width, self.height)
    
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.E:
            self.move_bird()


        elif key == arcade.key.Q:
            if self.camo.alpha == 0:
                self.camo.alpha = 255
            else:
                self.camo.alpha = 0


        elif key == arcade.key.ESCAPE:
            pause = pause.Pause(self, self.width, self.height)
            self.window.show_view(pause)


    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.Q or key == arcade.key.E:
            # determine if needed
            pass


    def move_bird(self):
        self.bird.center_x = randint(0, self.width)
        self.bird.center_y = randint(0, self.height)
        

def main():
    pass


if __name__ == "__main__":
    main()
