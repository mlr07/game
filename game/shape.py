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


class Translate(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.circle_angle = 0
        self.circle_radius = 20
        self.circle_speed = 0.075

    def translate_update(self, A_state, D_state):
        '''logic for translating in a circle around a fixed point'''
        if A_state and not D_state:
            self.center_x = 400+self.circle_radius*math.cos(self.circle_angle)
            self.center_y = 400+self.circle_radius*math.sin(self.circle_angle)
            self.circle_angle -= self.circle_speed

        if D_state and not A_state:
            self.center_x = 400+self.circle_radius*math.cos(self.circle_angle)
            self.center_y = 400+self.circle_radius*math.sin(self.circle_angle)
            self.circle_angle += self.circle_speed



