import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


class Shape(arcade.Sprite):
    '''extended class for shapes in illusion'''

    def update(self):
        '''move the sprite and check for out of bounds'''
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH-1:
            self.right = SCREEN_WIDTH-1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT-1:
            self.top = SCREEN_HEIGHT-1

