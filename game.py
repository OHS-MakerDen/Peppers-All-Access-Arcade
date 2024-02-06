import displayio
import random
from trench_game.Movement import*
import terminalio
from adafruit_display_text import label
from time import sleep


game_group = displayio.Group()

# display bitmaps and tilegrid

tie_fighter = displayio.OnDiskBitmap("trench_game/tie_fighter.bmp")
x_wing = displayio.OnDiskBitmap("trench_game/x_wing.bmp")
tie_bullet = displayio.OnDiskBitmap("trench_game/bullet.bmp")
trench = displayio.OnDiskBitmap("trench_game/background.bmp")
death_star = displayio.OnDiskBitmap("trench_game/star.bmp")
star_explosion = displayio.OnDiskBitmap("trench_game/blownstar.bmp")
menu_screen = displayio.OnDiskBitmap("trench_game/menuscreen.bmp")
tile_grid = displayio.TileGrid(trench, pixel_shader=trench.pixel_shader)

TRENCH_W = 6
TRENCH_H = 3

x_field = displayio.TileGrid(
    x_wing,
    pixel_shader=x_wing.pixel_shader,
    width=TRENCH_W,
    height=TRENCH_H,
    tile_width=10,
    tile_height=10,
)

tie_field = displayio.TileGrid(
    tie_fighter,
    pixel_shader=tie_fighter.pixel_shader,
    width=TRENCH_W,
    height=TRENCH_H,
    tile_width=10,
    tile_height=10,
)

bullet_field = displayio.TileGrid(
    tie_bullet,
    pixel_shader=tie_bullet.pixel_shader,
    width=TRENCH_W,
    height=TRENCH_H,
    tile_width=2,
    tile_height=2,
)

x_field.pixel_shader.make_transparent(29)
tie_field.pixel_shader.make_transparent(29)
bullet_field.pixel_shader.make_transparent(29)
x_field.y = 6
tie_field.y = 6
bullet_field.y = 6


# sets coordinates, game score, and the X-wing health
the_x_wing = Wing(5, 2)
the_tie_fighter = Fighter(2, 2)
the_tie_bullet = Bullet(2, 2)
game_tick = 0
x_health = 3


def x_movement(i):
    # choses random # from 1-2
    Wing.move = random(0,1)
    # moves down if # is 0
    if Wing.move == 0:
        self.y -= 1
    # moves up if # is 1
    if Wing.move == 1:
        self.y += 1

def bullet_hit_wing():
    # checks if the bullet hits the x-wing and if so subtracts a point from the health
    if tie_bullet == the_x_wing:
        x_health -= 1


def bullet_move(self):
    # how the bullet will move after you shoot it
    self.x += 1
    self.x += 1
    self.x += 1

def game_setup(p1_button,p2_button, coin_button):
    """this is called once to initialize your game features"""
    global game_tick
    game_group.append(menu_screen)
    time.sleep(15)
    if p2_button:
        game_group.remove(menu_screen)
    game_group.append(trenches)
    game_group.append(trench)
    game_tick = 0

def game_frame(p1_button,p2_button, coin_button) -> bool:
    """this is called every frame, you need to update all your grame objects
        returns True when the game is over, else return false"""
    global game_tick
    x_movement()
    if p1_button:
        game_group.append(tie_bullet)
        bullet_move()
        game_tick += 1
        bullet_hit_wing()


    #check if either the health is at 0 or the game tick is over 25, if neither: false, if one or both: true
    if x_health == 0 or game_tick == 25:
        return True
    return False


def game_over(p1_button, p2_button, coin_button):
    """this should display your game over screen with score also clean up the game_group"""
    global game_tick
    win = x_health

    lose = game_tick
    game_group.remove(tile_grid)
    game_group.remove(trench)
    game_group.append(death_star)
    if lose == 25:
        game_group.remove(death_star)
        game_group.append(star_explosion)
    if win == 0:
        game_group.remove(death_star)



