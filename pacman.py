
import arcade
from characters import *
from const import *





class PacmanGame(arcade.View):
    def __init__(self):
        super().__init__()
        self.change_x = 0
        self.change_y = 0
        self.game_over = False
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()
        self.background_color = arcade.color.BLACK

    def setup(self):
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
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
                    self.ghost = Ghost(x,y)
                    self.ghost_list.append(self.ghost)
                elif char == "P":
                    self.player = Player(x,y)
                    self.player_list.append(self.player)

    def on_key_press(self, key, modifiers):
        if not self.game_over:
            if arcade.key.UP == key:
                self.change_y = 1
            elif arcade.key.DOWN == key:
                self.change_y = -1
            elif arcade.key.RIGHT == key:
                self.change_x = 1
            elif arcade.key.LEFT == key:
                self.change_x = -1
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
        for coin in arcade.check_for_collision_with_list(self.player, self.coin_list):
            coin.remove_from_sprite_lists()


        for i in self.ghost_list:
            ghost_x = self.ghost.center_y
            ghost_y = self.ghost.center_x
            i.ghost_move(delta_time)
            if arcade.check_for_collision_with_list(i, self.wall_list):
                i.center_x = ghost_x
                i.center_y = ghost_y



    def on_draw(self):
        self.clear()
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

