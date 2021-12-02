import arcade


class Shape(arcade.Sprite):
    '''extended class for shapes in illusion'''
    

    def update(self):
        '''move the sprite and check for out of bounds'''
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > self.width-1:
            self.right = self.width-1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > self.height-1:
            self.top = self.height-1

