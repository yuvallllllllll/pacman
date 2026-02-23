import arcade
from pacman import *
WINDOW_WIDTH = 800

WINDOW_HEIGHT = 600
TILE_SIZE = 32
window = arcade.Window(WINDOW_WIDTH,WINDOW_HEIGHT)
game = PacmanGame()
game.setup()
window.show_view(game)
arcade.run()