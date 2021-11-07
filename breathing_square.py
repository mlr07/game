import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Breathing Square"

BLUE_SQUARE_SCALE = 2.5
ORANGE_SQUARE_SCALE = 2


class BreathingSquare(arcade.Window):
 
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.scene = None

        self.b_square = None

        self.shape_list = None

        arcade.set_background_color(arcade.color.WHITE)


    def setup(self):
        
        self.scene = arcade.Scene()

        img_src = "./resources/blue_square.png"
        self.b_square = arcade.Sprite(img_src, BLUE_SQUARE_SCALE)
        self.b_square.center_x = self.width/2
        self.b_square.center_y = self.height/2
        self.scene.add_sprite("blue_square", self.b_square)

        coords = [[self.width/4,self.height/4],
                  [self.width*0.75,self.height*0.25],
                  [self.width*0.25,self.height*0.75],
                  [self.width*0.75,self.height*0.75]
        ]

        for coord in coords:
            sqr = arcade.Sprite("./resources/orange_square.png", ORANGE_SQUARE_SCALE)
            sqr.position = coord
            self.scene.add_sprite("orange_square", sqr)

        print(self.b_square.center_x)
        print(self.b_square.center_y)


    def on_draw(self):
        arcade.start_render()
        
        self.scene.draw()


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
