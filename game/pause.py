import arcade
import start

class Pause(arcade.View):
    def __init__(self, game_view, width, height):
        super().__init__()
        self.game_view = game_view
        self.width = width
        self.height = height


    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.GRAY)
        arcade.draw_text("PAUSED", self.width*0.5, self.height*0.5+50, (0,0,0), 18, anchor_x="center")
        arcade.draw_text("Hit ESC to return", self.width*0.5, self.height*0.5, (0,0,0), 16, anchor_x="center")
        arcade.draw_text("Hit ENTER to quit", self.width*0.5, self.height*0.5-50, (0,0,0), 16, anchor_x="center")


    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            self.window.show_view(self.game_view)

        elif key == arcade.key.ENTER:
            game = GameView()
            self.window.show_view(game)

        elif key == arcade.key.R:
            self.start = start.StartView()
            self.window.show_view(self.start)
