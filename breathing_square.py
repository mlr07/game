import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Breathing Square"

BLUE_SQUARE_SCALE = 1
ORANGE_SQUARE_SCALE = 1

ANGLE_SPEED = 5
POS_SPEED = 5


class BreathingSquare(arcade.Window):
 
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.sprite_list = None

        self.b_square = None

        arcade.set_background_color(arcade.color.WHITE)


    def setup(self):
        
        self.sprite_list = arcade.SpriteList()

        img_src = "./resources/blue_square.png"
        self.b_square = arcade.Sprite(img_src, BLUE_SQUARE_SCALE)
        self.b_square.center_x = self.width/2
        self.b_square.center_y = self.height/2
        self.sprite_list.append(self.b_square)

        coords = [[self.width/4,self.height/4],
                  [self.width*0.75,self.height*0.25],
                  [self.width*0.25,self.height*0.75],
                  [self.width*0.75,self.height*0.75]
        ]

        for coord in coords:
            sqr = arcade.Sprite("./resources/orange_square.png", ORANGE_SQUARE_SCALE)
            sqr.position = coord
            self.sprite_list.append(sqr)

        print(len(self.sprite_list))


    def on_draw(self):
        arcade.start_render()
        
        self.sprite_list.draw()


    def on_update(self, delta_time):
        self.sprite_list.update()


    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.b_square.change_angle = ANGLE_SPEED

        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.b_square.change_angle = -ANGLE_SPEED

        elif key == arcade.key.UP or key == arcade.key.W:
            self.sprite_list[1].change_x = POS_SPEED
            self.sprite_list[1].change_y = POS_SPEED
            self.sprite_list[2].change_x = -POS_SPEED
            self.sprite_list[2].change_y = POS_SPEED
            self.sprite_list[3].change_x = POS_SPEED
            self.sprite_list[3].change_y = -POS_SPEED
            self.sprite_list[4].change_x = -POS_SPEED
            self.sprite_list[4].change_y = -POS_SPEED

        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.sprite_list[1].change_x = -POS_SPEED
            self.sprite_list[1].change_y = -POS_SPEED
            self.sprite_list[2].change_x = POS_SPEED
            self.sprite_list[2].change_y = -POS_SPEED
            self.sprite_list[3].change_x = -POS_SPEED
            self.sprite_list[3].change_y = POS_SPEED
            self.sprite_list[4].change_x = POS_SPEED
            self.sprite_list[4].change_y = POS_SPEED


    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.b_square.change_angle = 0

        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.b_square.change_angle = 0

        elif key == arcade.key.UP or key == arcade.key.W:
            self.sprite_list[1].change_x = 0
            self.sprite_list[1].change_y = 0
            self.sprite_list[2].change_x = 0
            self.sprite_list[2].change_y = 0
            self.sprite_list[3].change_x = 0
            self.sprite_list[3].change_y = 0
            self.sprite_list[4].change_x = 0
            self.sprite_list[4].change_y = 0


        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.sprite_list[1].change_x = 0
            self.sprite_list[1].change_y = 0
            self.sprite_list[2].change_x = 0
            self.sprite_list[2].change_y = 0
            self.sprite_list[3].change_x = 0
            self.sprite_list[3].change_y = 0
            self.sprite_list[4].change_x = 0
            self.sprite_list[4].change_y = 0

def main():
    game = BreathingSquare()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
