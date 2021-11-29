import arcade
from shape import Shape

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Illusions Game"

BLUE_SQUARE_SCALE = 3.5
ORANGE_SQUARE_SCALE = 2.5

ANGLE_SPEED = 1
POS_SPEED = 0.75

MENU_1 = "Press 1 to start the Breathing Square!" 
MENU_2 = "Press 2 to start Motion Binding!"
MENU_3 = "Press 3 to start the Hidden Bird!"
MENU_4 = "Press 4 to start Arrow Lengths!"

TITLE = "Breathing Square"
CONTROL_ROTATE = "Hold A and D to rotate the blue square" 
CONTROL_MOVE = "Hold W and S to move the orange squares" 


class BreathingSquare(arcade.View):
    ''' class for breathing square illusion'''
 
    def __init__(self):
        super().__init__()

        self.sprite_list = None

        self.b_square = None

        arcade.set_background_color(arcade.color.WHITE)


    def setup(self):
        self.sprite_list = arcade.SpriteList()

        img_src = "./resources/blue_square.png"
        self.b_square = arcade.Sprite(img_src, BLUE_SQUARE_SCALE)
        self.b_square.center_x = SCREEN_WIDTH/2
        self.b_square.center_y = SCREEN_HEIGHT/2
        self.sprite_list.append(self.b_square)

        coords = [[SCREEN_WIDTH/4,SCREEN_HEIGHT/4],
                  [SCREEN_WIDTH*0.75,SCREEN_HEIGHT*0.25],
                  [SCREEN_WIDTH*0.25,SCREEN_HEIGHT*0.75],
                  [SCREEN_WIDTH*0.75,SCREEN_HEIGHT*0.75]
        ]

        for coord in coords:
            sqr = Shape("./resources/orange_square.png", ORANGE_SQUARE_SCALE)
            sqr.position = coord
            self.sprite_list.append(sqr)


    def on_draw(self):
        arcade.start_render()
        
        self.sprite_list.draw()

        arcade.draw_text(TITLE, 5, 775, (0,0,0), 18)
        arcade.draw_text(CONTROL_ROTATE, 5, 30, (0,0,0), 14)
        arcade.draw_text(CONTROL_MOVE, 5, 7, (0,0,0), 14)


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
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game_view = BreathingSquare()
    game_view.setup()
    window.show_view(game_view)
    arcade.run()


if __name__ == "__main__":
    main()
