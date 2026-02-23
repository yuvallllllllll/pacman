import arcade
from const import *
from characters import *


class PacmanGame(arcade.View):
    def __init__(self):
        super().__init__()
        self.change_x = 0
        self.change_y = 0
        self.game_over = False
        self.point = 0
        self.i = 1
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()

    def setup(self):
        self.game_over = False
        self.change_x = 0
        self.change_y = 0
        self.point = 0
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()

        rows = len(maps[f"MAP_{self.i}"])
        print(maps[f"MAP_{self.i}"])
        for row_index, row in enumerate(maps[f"MAP_{self.i}"]):
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
                    self.player = Player(x, y)
                    self.player_list.append(self.player)

    def on_draw(self):
        self.clear()
        self.wall_list.draw()
        self.coin_list.draw()
        self.ghost_list.draw()
        self.player_list.draw()

        arcade.draw_text(f"Points: {self.point}" , x =  10, y = WINDOW_HEIGHT -25,font_size = 20.0)
        arcade.draw_text(f"Level: {self.i}" , x =  10, y = WINDOW_HEIGHT -50,font_size = 20.0)

        if self.game_over:
            arcade.draw_text("GAME OVER: YOU LOSE", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 50,arcade.color.RED, font_size=40, anchor_x="center")

            arcade.draw_text("Press SPACE to Play Again", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 5,arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if self.game_over:
            if key == arcade.key.SPACE:
                self.setup()
            return

        if key == arcade.key.UP:
            self.change_y = 1
        elif key == arcade.key.DOWN:
            self.change_y = -1
        elif key == arcade.key.RIGHT:
            self.change_x = 1
        elif key == arcade.key.LEFT:
            self.change_x = -1

    def on_key_release(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.change_y = 0
        elif key in [arcade.key.RIGHT, arcade.key.LEFT]:
            self.change_x = 0

    def on_update(self, delta_time):

        if self.game_over:
            self.i = 0
            return
        if len(self.coin_list) == 0:
            self.i = self.i + 1
            self.setup()
            if self.i > 3:
                arcade.draw_text("GAME OVER: YOU WON!!!", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 50, arcade.color.RED,
                                 font_size=40, anchor_x="center")

        old_px, old_py = self.player.center_x, self.player.center_y
        self.player.player_move(self.change_x, self.change_y)
        if arcade.check_for_collision_with_list(self.player, self.wall_list):
            self.player.center_x, self.player.center_y = old_px, old_py

        coins_hit = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for coin in coins_hit:
            coin.remove_from_sprite_lists()
            if arcade.check_for_collision(self.player, coin):
                self.point = self.point + 1
        for ghost in self.ghost_list:
            old_gx, old_gy = ghost.center_x, ghost.center_y
            ghost.ghost_move(delta_time)

            if arcade.check_for_collision_with_list(ghost, self.wall_list):
                ghost.center_x, ghost.center_y = old_gx, old_gy
                ghost.time_to_change = 0

            if arcade.check_for_collision(self.player, ghost):
                self.game_over = True