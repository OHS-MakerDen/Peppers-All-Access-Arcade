import displayio
import random
from trench_game.Movement import*
import terminalio
import time


game_group = displayio.Group()

tie_fighter = displayio.OnDiskBitmap("trench_game/tie_fighter.bmp")
x_wing = displayio.OnDiskBitmap("trench_game/X-wing for Star wars escape2.bmp")
tie_bullet = displayio.OnDiskBitmap("trench_game/bullet for tie fighter-Recovered.bmp")
trench = displayio.OnDiskBitMap("trench_game/backround for Star wars escape.bmp")
death_star = displayio.OnDiskBitMap("trench_game/star.bmp")
death_star_explosion = displayio.OnDiskBitMap("trench_game/blown star.bmp")
menu_screen = displayio.OnDiskBitMap("trench_game/menu screen.bmp")
trenches = displayio.TileGrid(trench, pixel_shader = trench.pixel_shader)

TRENCH_W = 6
TRENCH_H = 3

trench_grid = displayio.TileGrid(
    x_wing,
    pixel_shader=x_wing.pixel_shader,
    width=TRENCH_W,
    height=TRENCH_H,
    tile_width=10,
    tile_height=10,
)


self.y == height


the_x_wing = Wing(5, 2)
the_tie_fighter = Fighter(2, 2)
the_tie_bullet = Bullet(2, 2)
game_tick = 0
x_health = 3
    

def x_wings_movement():
    Wing.move = random(0,1)
    if Wing.move == 0:
        self.y -= 1
    if Wing.move == 1:
        self.y += 1
        
def bullet_hit_x_wing():
    bullet_move == tie_move
    if tie_bullet == the_x_wing:
        x_health -= 1

    
def bullet_move():
    self.x += 1
    self.x += 1
    self.x += 1

def game_setup(p1_button,p2_button, coin_button):
    """this is called once to initialize your game features"""
    global game_tick
    game_group.append(menu_screen)
    if p2_button:
        game_group.remove(menu_screen)
    game_group.append(trenches)
    game_group.append(trench)
    game_tick = 0

def game_frame(p1_button,p2_button, coin_button) -> bool:
    """this is called every frame, you need to update all your grame objects
        returns True when the game is over, else return false"""
    global game_tick
    x_wings_movement()
    if p1_button:
        game_group.append(tie_bullet)
        bullet_move()
        game_tick += 1
        bullet_hit_x_wing()
        
   
    
    if x_health > 0 or game_tick < 25:
        return False
    else:
        return True


def game_over(p1_button, p2_button, coin_button):
    """this should display your game over screen with score also clean up the game_group"""
    global game_tick
    win = x_health
    
    lose = game_tick
    game_group.remove(trenches)
    game_group.remove(trench)
    game_group.append(death_star)
    if lose == 25:
        game_group.remove(death_star)
        game_group.append(death_star_explosion)
    if win == 0:
        game_group.remove(death_star)
    
    
    
