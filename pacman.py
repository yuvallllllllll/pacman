
import arcade

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
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
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
                    self.ghost_list.append(Ghost(x, y))
                elif char == "P":
                    self.player_list.append(Player(x, y))

    def on_draw(self):
        self.clear(self.background_color)
        self.wall_list.draw()
        self.coin_list.draw()
        self.ghost_list.draw()
        self.player_list.draw()


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
    def __init__(self, x, y):
        super().__init__()
        self.texture = arcade.make_circle_texture(TILE_SIZE - 10, arcade.color.RED)
        self.center_x = x
        self.center_y = y


class Player(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.texture = arcade.make_circle_texture(TILE_SIZE - 10, arcade.color.YELLOW )
        self.center_x = x
        self.center_y = y
