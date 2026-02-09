
import arcade
from characters import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TILE_SIZE = 32

MAP = [
    "########################",
    "#..........##..........#",
    "#.####.###.##.###.####.#",
    "#P....................G#",
    "########################",
]


class PacmanGame(arcade.View):
    def __init__(self):
        super().__init__()
        self.game_over = False
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()
        self.background_color = arcade.color.BLACK

    def setup(self):
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()
        rows = len(MAP)
        for row_index, row in enumerate(MAP):
            for col_index, char in enumerate(row):
                x = col_index * TILE_SIZE + TILE_SIZE / 2
                y = (rows - row_index - 1) * TILE_SIZE + TILE_SIZE / 2

                if char == "#":
                    self.wall_list.append(Wall(x, y))
                elif char == ".":
                    self.coin_list.append(Coin(x, y))
                elif char == "G":
                    self.ghost_list.append(Ghost(x, y))
                elif char == "P":
                    self.player = Player(x,y)

    def on_key_press(self, key, modifiers):
        if self.game_over == False:
            if arcade.key.UP == key:
                self.change_y = + 1
            elif arcade.key.DOWN == key:
                self.change_y = - 1
            elif arcade.key.RIGHT == key:
                self.change_x = + 1
            elif arcade.key.LEFT == key:
                self.change_x = - 1
        else:
            if arcade.key.SPACE == key:
                self.game_over = False

    def on_update(self, delta_time):
        Temporary_center_y = self.player.center_y
        Temporary_center_x = self.player.center_x
        self.player.player_move(self.change_x,self.change_y)
        if arcade.check_for_collision_with_list(self.player, self.wall_list):
            self.player.center_x = Temporary_center_x
            self.player.center_y = Temporary_center_y



    def on_draw(self):
        self.clear(self.background_color)
        self.wall_list.draw()
        self.coin_list.draw()
        self.ghost_list.draw()
        self.player_list.draw()


    def on_key_release(self, key, modifiers):
        if arcade.key.UP == key:
            self.change_y = 0
        elif arcade.key.DOWN == key:
            self.change_y = 0
        elif arcade.key.RIGHT == key:
            self.change_x = 0
        elif arcade.key.LEFT == key:
            self.change_x = 0

