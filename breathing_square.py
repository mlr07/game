import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Breathing Square"


class BreathingSquare(arcade.Window):
 
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.shape_list = None

        arcade.set_background_color(arcade.color.WHITE)


    def setup(self):
        self.shape_list = arcade.ShapeElementList()

        shape = arcade.create_rectangle_filled(self.width/2, 
                                               self.height/2,
                                               200,
                                               200,
                                               arcade.color.BLUE
        )

        self.shape_list.append(shape)


    def on_draw(self):
        arcade.start_render()
        
        self.shape_list.draw()


    def on_update(self, delta_time):
        pass


    def on_key_press(self, key, key_modifiers):
        pass


    def on_key_release(self, key, key_modifiers):
        pass


def main():
    game = BreathingSquare()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
