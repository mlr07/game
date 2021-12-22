import arcade
import math


class Shape(arcade.Sprite):
    '''extended class for shapes in illusion'''


    def update(self, scr_width, scr_height):
        '''move the sprite and check for out of bounds'''
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > scr_width-1:
            self.right = scr_width-1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > scr_height-1:
            self.top = scr_height-1

    # does this need to be here?
    def translate(self, radius, translate_angle, scrn_width, scrn_height):
        self.center_x = scrn_width*0.5+radius*math.cos(math.radians(translate_angle))
        self.center_y = scrn_height*0.5+radius*math.sin(math.radians(translate_angle))
