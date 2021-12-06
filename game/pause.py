import arcade


class Pause(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view


    def on_show(self):
        arcade.set_background_color(arcade.color.GRAY)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("PAUSED", 800*0.5, 800*0.5+50, (0,0,0), 18, anchor_x="center")
        arcade.draw_text("Hit ESC to return", 800*0.5, 800*0.5, (0,0,0), 16, anchor_x="center")
        arcade.draw_text("Hit ENTER to quit", 800*0.5, 800*0.5-50, (0,0,0), 16, anchor_x="center")


    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:   # resume game
            self.window.show_view(self.game_view)
        elif key == arcade.key.ENTER:  # reset game
            game = GameView()
            self.window.show_view(game)
