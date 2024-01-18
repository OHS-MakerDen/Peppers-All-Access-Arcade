import displayio

game_group = displayio.Group()

tie_fighter = displayio.OnDiskBitmap("trench_game/tie_fighter.bmp")
x_wing = displayio.OnDiskBitmap("trench_game/X-wing for Star wars escape2.bmp")
tie_bullet = displayio.OnDiskBitmap("trench_game/bullet for tie fighter-Recovered.bmp")
trench = displayio.OnDiskBitMap("trech_game/backround for Star wars escape.bmp")
trenches = displayio.TileGrid(trench, pixel_shader = trench.pixel_shader)

TRENCH_W = 7
TRENCH_H = 6

trench_grid = displayio.TileGrid(
    x_wing,
    pixel_shader=x_wing.pixel_shader,
    width=TRENCH_W,
    height=TRENCH_H,
    tile_width=12,
    tile-height=12,
)

the_x_wing = Wing(3, 5)
the_tie_fighter = Fighter(3, 2)
game_score = 0
game_tick = 0



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
    
    return False


def game_over():
    """this should display your game over screen with score also clean up the game_group"""
    global game_score
    global game_tick

    game_group.remove(trenches)
    
    

