import displayio
import random 
from time import sleep
from adafruit_display_text import label

game_group = displayio.Group()



map = displayio.OnDiskBitmap("graphics/background.bmp")
background = displayio.TileGrid(map, pixel_shader=farm.pixel_shader





def game_setup(p1_button,p2_button, coin_button):
    """this is called once to initialize your game features"""
    pass

def game_frame(p1_button,p2_button, coin_button) -> bool:
    """this is called every frame, you need to update all your grame objects
        returns True when the game is over, else return false"""
    return False


def game_over(p1_button,p2_button, coin_button):
    """this should display your game over screen with score also clean up the game_group"""
    pass
