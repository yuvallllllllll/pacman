from const import *
import arcade
import random

class Wall(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.texture = arcade.make_soft_square_texture(TILE_SIZE, arcade.color.BLUE, 255, 0)
        self.center_x = x
        self.center_y = y


class Coin(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.texture = arcade.make_circle_texture(TILE_SIZE - 20, arcade.color.GOLD)
        self.center_x = x
        self.center_y = y


class Ghost(arcade.Sprite):
    def __init__(self, x, y,speed=1):
        super().__init__()
        self.texture = arcade.make_circle_texture(TILE_SIZE - 10, arcade.color.RED)
        self.center_x = x
        self.center_y = y
        self.speed = speed


class Player(arcade.Sprite):
    def __init__(self, x, y,speed=2):
        super().__init__()
        self.texture = arcade.make_circle_texture(TILE_SIZE - 10, arcade.color.YELLOW )
        self.center_x = x
        self.center_y = y
        self.speed = speed

    def player_move(self,change_x,change_y):
        self.center_x += change_x * self.speed
        self.center_y += change_y * self.speed
