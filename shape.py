import arcade


class Shape(arcade.Sprite):
    '''extended class for shapes in illusion'''
    
    def __init__(self, width, height):
        super.__init__()
        self.width = width
        self.height = height


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

