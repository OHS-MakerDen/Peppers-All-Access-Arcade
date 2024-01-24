import displayio

game_group = displayio.Group()

players = displayio.OnDiskBitmap("""Add Bitmap when ready""")
land = displayio.OnDiskBitmap("""Add Bitmap when ready""")
bkgnd = displayio.TileGrid(land, pixel_shader=land.pixel_shader)

LandW = """Define with graphics"""
LandH = """Define with graphics"""

battle_field = displayio.TileGrid(
    players,
    pixel_shader=players.pixel_shader,
    width=LandW,
    height=LandH,
    tile_width="""Define with graphics""",
    tile_height="""Define with graphics""",
)

battle_field.pixel_shader.make_transparent(29)
battle_field.y = 8

the_warriors = Warriors(2, 2)
game_tick = 0
p1_score = 0
p2_score = 0

def game_setup(p1_button:bool,p2_button:bool, coin_button:bool):
    global game_tick
    game_group.append(bkgnd)
    game_group.append(battle_field)
    game_tick = 0
    pass

def game_frame(p1_button: bool, p2_button: bool, coin_button:bool):
    if p1_button:
        p1_score+=1
    elif p2_button:
        p2_score+=1
    if p1_score>p2_score:
        the_warriors.x-=1
    elif p1_score<p2_score:
        the_warriors.x+=1

    return False


def game_over(p1_button:bool,p2_button:bool, coin_button:bool):
    global game_tick
    global the_warriors

    game_group.remove(battle_field)
    game_group.append(text_area)
    sleep(5)
    game_group.remove(text_area)
    game_group.remove(bkgnd)
