import displayio
import random
import time

bkgnd = displayio.OnDiskBitmap("jamal_graphics/bkgnd.bmp")
bkgnd = displayio.TileGrid(
    bkgnd,
    pixel_shader=bkgnd.pixel_shader,
    width=511,
    height=1,
    tile_width=64,
    tile_height=64,
)

gmover = displayio.OnDiskBitmap("jamal_graphics/game_over.bmp")
gmover = displayio.TileGrid(
    gmover,
    pixel_shader=gmover.pixel_shader,
    width=1,
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

jamal = displayio.OnDiskBitmap("jamal_graphics/jamal_good.bmp")
jamal = displayio.TileGrid(
    jamal,
    pixel_shader=jamal.pixel_shader,
    width=1,
    height=1,
    tile_width=16,
    tile_height=14
)
jamal.pixel_shader.make_transparent(30)
jamal.x = 8
jamal.y = 29

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
animate = 0


def game_setup(p1_clicked, p2_clicked, coin_clicked):
    """this is called once to initialize your game features"""
    game_group.append(bkgnd)
    game_group.append(obstacle)
    game_group.append(jamal)

    global obstacle_wait
    global hitboxes
    global jumping
    global hitbox_wait
    global animate

    jumping = False
    obstacle_wait = 0
    hitbox_wait = 0
    hitboxes = []
    bkgnd.x = 0
    obstacle.x = 64
    animate = 0

    # free spaces at start
    for i in range(8):
        hitboxes.append(0)

    # creates obstacles and hitboxes
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

def game_frame(p1_clicked, p2_clicked, coin_clicked) -> bool:
    """this is called every frame, you need to update all your grame objects
    returns True when the game is over, else return false"""
    global jumping
    global hitbox_wait
    global hitboxes
    global animate

    # decides if jumping
    if p1_clicked and jamal.y == 29:
        jumping = True
    elif jamal.y == 13:
        jumping = False

    # movement when jumping
    if jumping:
        jamal.y -= 4
    elif jamal.y != 29:
        jamal.y += 4

    # every other frame hitboxes advance
    if hitbox_wait > 0:
        hitbox_wait -= 1
    else:
        hitbox_wait = 1
        hitboxes.pop(0)

    # moves background and obstacles
    bkgnd.x -= 4
    obstacle.x -= 4

    # animation
    jamal[0, 0] = animate
    if animate == 6:
        animate = 0
    else:
        animate += 1

    # checks if jamal is touching hitbox
    if jamal.y == 29 and (hitboxes[0] == 1 or hitboxes[1] == 1 or hitboxes[2] == 1):
        return True
    else:
        return False

def game_over(p1_clicked, p2_clicked, coin_clicked):
    """this should display your game over screen with score also clean up the game_group"""

    # deletes all in game_group
    for i in range(len(game_group)):
        game_group.pop()

    # shows game over screen for 5 seconds then hides and restarts
    game_group.append(gmover)
    time.sleep(5)
    game_group.pop()

    pass
