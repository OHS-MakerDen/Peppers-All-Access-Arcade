import displayio
import random

bkgnd = displayio.OnDiskBitmap("jamal_graphics/bkgnd.bmp")
bkgnd = displayio.TileGrid(
    bkgnd,
    pixel_shader=bkgnd.pixel_shader,
    width=100,
    height=1,
    tile_width=64,
    tile_height=64,
)

font = displayio.OnDiskBitmap("jamal_graphics/font.bmp")
font = displayio.TileGrid(
    font,
    pixel_shader=font.pixel_shader,
    width=1,
    height=1,
    tile_width=5,
    tile_height=5
)
font.pixel_shader.make_transparent(2)
font.x = 3
font.y = 3

jamal = displayio.OnDiskBitmap("jamal_graphics/jamal.bmp")
jamal = displayio.TileGrid(
    jamal,
    pixel_shader=jamal.pixel_shader,
    width=1,
    height=1,
    tile_width=8,
    tile_height=8,
)
jamal.pixel_shader.make_transparent(30)
jamal.x = 8
jamal.y = 35

obstacle = displayio.OnDiskBitmap("jamal_graphics/obstacles.bmp")
obstacle = displayio.TileGrid(
    obstacle,
    pixel_shader=obstacle.pixel_shader,
    width=511,
    height=1,
    tile_width=8,
    tile_height=8,
)
obstacle.pixel_shader.make_transparent(30)
obstacle.x = 64
obstacle.y = 35

game_group = displayio.Group()
jumping = False
obstacle_wait = 0
hitbox_wait = 0
hitboxes = []


def game_setup(p1_button, p2_button, coin_button):
    """this is called once to initialize your game features"""
    game_group.append(bkgnd)
    game_group.append(obstacle)
    game_group.append(jamal)
    game_group.append(font)
    global obstacle_wait
    global hitboxes
    for col in range(511):
        if random.randint(0, 2) == obstacle_wait == 0:
            hitboxes.append(1)
            obstacle[col, 0] = random.randint(0, 4)
            obstacle_wait = 2
        else:
            hitboxes.append(0)
            obstacle[col, 0] = 5
            if obstacle_wait > 0:
                obstacle_wait -= 1
   
    pass

def game_frame(p1_button, p2_button, coin_button) -> bool:
    """this is called every frame, you need to update all your grame objects
    returns True when the game is over, else return false"""
    global jumping
    global hitbox_wait
    if p1_button and jamal.y == 35:
        jumping = True
    elif jamal.y == 20:
        jumping = False
    if jumping:
        jamal.y -= 5
    elif jamal.y != 35:
        jamal.y += 5
    if hitbox_wait == 1:
        hitbox_wait = 0
    else:
        hitbox_wait = 1
        hitboxes.pop(0)

    bkgnd.x -= 4
    obstacle.x -= 4
    
    if jamal.y == 35 and hitboxes[0] == 1:
        return True
    else:
        return False

def game_over(p1_button, p2_button, coin_button):
    """this should display your game over screen with score also clean up the game_group"""

    pass
