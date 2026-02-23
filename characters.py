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
    def __init__(self, x, y, speed=2.5):
        super().__init__()
        self.texture = arcade.make_circle_texture(TILE_SIZE - 10, arcade.color.RED)
        self.center_x = x
        self.center_y = y
        self.speed = speed
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        self.time_to_change = 2

    def ghost_move(self, delta_time):
        self.time_to_change -= delta_time
        if self.time_to_change <= 0:
            directions = ["UP", "DOWN", "LEFT", "RIGHT"]
            self.direction = random.choice(directions)
            self.time_to_change = 2


        if self.direction == "UP":
            self.center_y += self.speed
        elif self.direction == "DOWN":
            self.center_y -= self.speed
        elif self.direction == "RIGHT":
            self.center_x += self.speed
        elif self.direction == "LEFT":
            self.center_x -= self.speed

class Player(arcade.Sprite):
    def __init__(self, x, y, speed=2):
        super().__init__()
        self.texture = arcade.make_circle_texture(TILE_SIZE - 10, arcade.color.YELLOW)
        self.center_x = x
        self.center_y = y
        self.speed = speed

    def player_move(self, change_x, change_y):
        self.center_x += change_x * self.speed
        self.center_y += change_y * self.speed