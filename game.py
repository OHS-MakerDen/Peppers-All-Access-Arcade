import displayio

game_group = displayio.Group()

tie_fighter = displayio.OnDiskBitmap("trench_game/tie_fighter.bmp")
x_wing = displayio.OnDiskBitmap("trench_game/X-wing for Star wars escape2.bmp")
tie_bullet = displayio.OnDiskBitmap("trench_game/bullet for tie fighter-Recovered.bmp")
trench = displayio.OnDiskBitMap("trech_game/backround for Star wars escape.bmp")
trench_grid = displayio.OnDiskBitMap("trench_game/grid for backround of Star wars escape.bmp")

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
def game_setup():
    """this is called once to initialize your game features"""
    pass

def game_frame(p1_button:bool,p2_button:bool) -> bool:
    """this is called every frame, you need to update all your grame objects
        returns True when the game is over, else return false"""
    return False


def game_over():
    """this should display your game over screen with score also clean up the game_group"""
    pass

