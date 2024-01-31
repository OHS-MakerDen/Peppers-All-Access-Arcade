import displayio
import random
import terminalio
from adafruit_display_text import label
from time import sleep
class coords:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.x1 = x + width
        self.y1 = y + height

class police:
    def __init__(self, x, y, width, height, spotlight_range):
        self.guard = displayio.OnDiskBitmap("getaway/guard.bmp")
        self.actualguard = displayio.TileGrid(
            self.guard,
            pixel_shader=self.guard.pixel_shader,
            width=1,
            height=1,
            tile_width=8,
            tile_height=18,default_tile = 2
        )
        self.walking = False
        self.actualguard.pixel_shader.make_transparent(29)
        self.guardheight = height
        self.guardwidth = width


        self.spotlight_range = spotlight_range
        self.actualguard.x = 1000000000
        self.actualguard.y = 43
        self.changedirection = 0

        self.whentoappear = 5
        self.timetoreset = False
        self.timetomove = False
        self.counter = 0
        self.changedirection = 0
        self.letsdothis = False


    def appear(self):
        place = random.randint(1, 2)
        if place == 1:
            self.actualguard.x = 70
            self.timetogetcaught = False
            self.timetomove = True




    def move(self):
        self.actualguard.x += -3
        if self.actualguard.x <= -6:
            self.timetoreset = True

        if self.walking == True:
            self.actualguard[0] = 3
            self.walking = False
        elif self.walking == False:
            self.actualguard[0] = 2
            self.walking = True
    def counters(self):
        self.counter += 1
        if self.counter >= self.whentoappear:
            self.timetogetcaught = True
            self.letsdothis = True

            self.whentoappear = 10000000000000000000000000000000000
    def reset(self):
        self.whentoappear = self.counter + 10
        self.letsdothis = False
        self.timetoreset = False
        self.walking = True



police = police(4, 9, 4, 4, 4)



game_group = displayio.Group()


background = displayio.OnDiskBitmap("getaway/jailbackground.bmp")
background1 = displayio.OnDiskBitmap("getaway/Policerooms.bmp")
guard = displayio.OnDiskBitmap("getaway/guard.bmp")
prisoner = displayio.OnDiskBitmap("getaway/prisoner sprite.bmp")
startscreen = displayio.OnDiskBitmap("getaway/Getawaytitle.bmp")
Box = displayio.OnDiskBitmap("getaway/Box.bmp")
background2 = displayio.OnDiskBitmap("getaway/TheHOLEOrdeal.bmp")
realbackground2 = displayio.TileGrid(background2, pixel_shader = background2.pixel_shader, width = 1, height = 1, tile_width = 64, tile_height = 64)


prisoner.pixel_shader.make_transparent(4)
realbackground2.pixel_shader.make_transparent(29)

actualprisoner = displayio.TileGrid(
    prisoner,
    pixel_shader=prisoner.pixel_shader,
    width=1,
    height=1,
    tile_width=8,
    tile_height=18,
)
realbackground = displayio.TileGrid(background, pixel_shader=background.pixel_shader)
policerooms = displayio.TileGrid(background1, pixel_shader = background1.pixel_shader)
actualguard = displayio.TileGrid(
    guard,
    pixel_shader=guard.pixel_shader,
    width=1,
    height=1,
    tile_width=8,
    tile_height=18,
)
actualBox = displayio.TileGrid(Box,pixel_shader = Box.pixel_shader, width = 1, height = 1,tile_width = 20, tile_height = 20)
actualBox.x = 25
actualBox.y = 42

realstartscreen = displayio.TileGrid(startscreen, pixel_shader=startscreen.pixel_shader)


FIELD_W = 1
FIELD_H = 1

game_group = displayio.Group()
game_group.append(realbackground)

game_group.append(actualprisoner)
game_group.append(actualBox)


game_group.append(police.actualguard)
actualprisoner.y = 44
staying_still = False
hiding = False
guard_coords = coords(police.actualguard.x,police.actualguard.y,8,18)
box_coords = coords(actualBox.x,actualBox.y,20,20)

amount_of_boxes = [box_coords]
rotatebackground = True
endgame = 0
def game_setup(p1_button, p2_button, coin_button):
    """this is called once to initialize your game features"""
    # while coin_button=false
    # game_group.append(realstartscreen)

    yes = True


def game_frame(p1_button, p2_button, coin_button) -> bool:
    """this is called every frame, you need to update all your grame objects
    returns True when the game is over, else return false"""
    global staying_still
    global rotatebackground
    global endgame
    police.counters()
    prisoner_coords = coords(actualprisoner.x,actualprisoner.y,8,12)
    guard_coords = coords(police.actualguard.x,police.actualguard.y,8,18)
    box_coords = coords(actualBox.x,actualBox.y,20,20)
    hiding = False
    if police.letsdothis == True:

    
        if police.timetogetcaught == True:
            police.appear()

        if police.timetomove == True:
            police.move()
        if police.timetoreset == True:
            police.reset()
  
  
    for i in amount_of_boxes:
        if hiding == True:
            continue
        if prisoner_coords.x >= i.x and prisoner_coords.x <= i.x1 and prisoner_coords.x1 >= i.x and prisoner_coords.x1<= i.x1:
            hiding = True
    
    
    print(hiding)
            
    if prisoner_coords.x >= guard_coords.x and prisoner_coords.x <= guard_coords.x1 and hiding == False:
        print("caught")
        return True
    elif prisoner_coords.x1 >= guard_coords.x and prisoner_coords.x1 <= guard_coords.x1 and hiding == False:
        print("caught")
        return True
    






    if p1_button:
        actualprisoner.x -= 0
        actualprisoner[0] = 0
        staying_still = True
        
    if actualprisoner.x >= 64 and endgame == 4:
        game_group.pop(0)
        game_group.insert(0,realbackground2)
        actualBox.x = 20
        endgame = 10
        rotatebackground = -1000013
    elif actualprisoner.x >=64 and rotatebackground == True:
        actualprisoner.x = 3
        game_group.remove(realbackground)
        game_group.insert(0,policerooms)
        rotatebackground = False
    elif actualprisoner.x >= 64 and rotatebackground == False:
        actualprisoner.x = 3
        game_group.remove(policerooms)
        game_group.insert(0,realbackground)
        rotatebackground = True
        endgame += 1
    elif endgame == 10 and prisoner_coords.x >= 60:
        return True
        print("YOU DID IT")
        
    
        
    if not p1_button:
        actualprisoner.x += 30
        if staying_still == True:
            actualprisoner[0] = 0
            staying_still = False
            
            
        if staying_still == False:
            actualprisoner[0] = 1
            staying_still = True
    return False

def game_over(p1_button, p2_button, coin_button) -> bool:
    """this should display your game over screen with score also clean up the game_group"""
    game_group.insert(0,
    pass
