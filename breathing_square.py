import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Breathing Square"

BLUE_SQUARE_SCALE = 1
ORANGE_SQUARE_SCALE = 1

ANGLE_SPEED = 5


class BreathingSquare(arcade.Window):
 
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.scene = None

        self.b_square = None

        self.shape_list = None

        self.physics_engine = None

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

        self.physics_engine = arcade.PhysicsEngineSimple(self.b_square, arcade.SpriteList())


    def on_draw(self):
        arcade.start_render()
        
        self.scene.draw()


    def on_update(self, delta_time):
        self.physics_engine.update()
        

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.b_square.change_angle = ANGLE_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.b_square.change_angle = -ANGLE_SPEED


    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.b_square.change_angle = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.b_square.change_angle = 0


def main():
    game = BreathingSquare()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
