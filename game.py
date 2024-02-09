import displayio
import random 
from time import sleep
from adafruit_display_text import label

game_group = displayio.Group()

score = 0

note = displayio.OnDiskBitmap("graphics/notetile.bmp")
background = displayio.OnDiskBitmap("graphics/background.bmp")
bkgnd = displayio.TileGrid(map, pixel_shader=background.pixel_shader)


SPACE_FIELD.pixel_shader.make_transparent(29)
SPACE_FIELD.y = 8

def game_setup(p1_button,p2_button, coin_button):
    """this is called once to initialize your game features"""
    pass

def game_frame(p1_button: bool, p2_button: bool, coin_button: bool):
    if p1_button:
        score += 1
        print(score)
    
    return False


def game_over(p1_button,p2_button, coin_button):
    gamegroup.remove(bkgnd)
    print(score)
