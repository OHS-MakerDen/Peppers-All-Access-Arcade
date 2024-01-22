import displayio
import random
from trench_game.Movement import *
import terminalio
import time


game_group = displayio.Group()

tie_fighter = displayio.OnDiskBitmap("trench_game/tie_fighter.bmp")
x_wing = displayio.OnDiskBitmap("trench_game/X-wing for Star wars escape2.bmp")
tie_bullet = displayio.OnDiskBitmap("trench_game/bullet for tie fighter-Recovered.bmp")
trench = displayio.OnDiskBitMap("trech_game/backround for Star wars escape.bmp")
death_star = displayio.OnDiskBitMap("")
death_star_explosion = displayio.OnDiskBitMap("")
trenches = displayio.TileGrid(trench, pixel_shader = trench.pixel_shader)

TRENCH_W = 7
TRENCH_H = 5

trench_grid = displayio.TileGrid(
    x_wing,
    pixel_shader=x_wing.pixel_shader,
    width=TRENCH_W,
    height=TRENCH_H,
    tile_width=12,
    tile-height=12,
)
trench_grid.y = 8


the_x_wing = Wing(5, 3)
the_tie_fighter = Fighter(2, 3)
the_tie_bullet = Bullet(2, 3)
game_tick = 0
x_health = 3

def tie_fighter():
    random.move(0,1)

def bullet_tie_fighter():
    
    if tie_bullet == the_x_wing:
        x_health - 1

def bullet_counter():
    the_tie_bullet.move()
    game_tick += 1

def game_setup():
    """this is called once to initialize your game features"""
    global game_tick
    game_group.append(trenches)
    game_group.append(trench)
    game_tick = 0

def game_frame(p1_button:bool,p2_button:bool) -> bool:
    """this is called every frame, you need to update all your grame objects
        returns True when the game is over, else return false"""
    global game_tick
    if p1_button: True:
        the_x_wing.move()
        print(
    elif p1_button: False:
        the_x_wing.move()
   
    
    if len(x_health) > 0 or game_tick < 25:
        return False
    else:
        return True


def game_over():
    """this should display your game over screen with score also clean up the game_group"""
    global game_tick

    game_group.remove(trenches)
    game_group.remove(trench)
    game_group.append(death_star)
    if len(x_health) > 0:
        sleep(5)
        game_group.remove(death_star)
        game_group.append(death_star_explosion)
    elif game_tick < 25:
        sleep(5)
        game_group.remove(death_star)
    
    
    

