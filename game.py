import displayio
import terminalio
from adafruit_display_text import label
import time
from axe.AxeClass import *

game_group = displayio.Group()

axe = displayio.OnDiskBitmap("axe/axe.bmp")
startingbg = displayio.OnDiskBitmap("axe/STARTINGBG.bmp")
meter = displayio.OnDiskBitmap("axe/Meter.bmp")
ndl = displayio.OnDiskBitmap("axe/Needle.bmp")
first_map = displayio.OnDiskBitmap("axe/map_1.bmp")
game_over= displayio.OnDiskBitmap("axe/game_over.bmp")

map_1 = displayio.TileGrid(first_map, pixel_shader=first_map.pixel_shader)
mtr = displayio.TileGrid(meter, pixel_shader=meter.pixel_shader)
bkgnd = displayio.TileGrid(startingbg, pixel_shader=startingbg.pixel_shader)
gameover = displayio.TileGrid(game_over, pixel_shader=game_over.pixel_shader)
needle = displayio.TileGrid(ndl, pixel_shader=ndl.pixel_shader)

FIELD_W = 64
FIELD_H = 64

forest_bg = displayio.TileGrid(
    axe,
    pixel_shader=axe.pixel_shader,
    width=FIELD_W,
    height=FIELD_H,
    tile_width=64,
    tile_height=64,
)
needle.pixel_shader.make_transparent(29)
forest_bg.pixel_shader.make_transparent(29)
forest_bg.y = 64
mtr.pixel_shader.make_transparent(29)
the_axes = []
game_score = 0
game_tick = 0
running = False
game_end = False


def game_setup(p1_button: bool, p2_button: bool, coin_button: bool):
    game_group.append(bkgnd)
    pass

def game_frame(p1_button: bool, p2_button: bool, coin_button: bool) -> bool:
    global running
    if p1_button and not running:
        game_group.append(map_1)
        game_group.append(mtr)
        game_group.append(needle)
        running = True
    elif p1_button and running:
        game_end = True
    elif p1_button and game_end == True:
        game_group.append(gameover)
    return False

def game_over(p1_button: bool, p2_button: bool, coin_button: bool):
    global game_score
    pass
