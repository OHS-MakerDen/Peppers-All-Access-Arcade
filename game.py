import displayio

game_group = displayio.Group()

GROUND_HEIGHT = -16
SLIME_JUMP_HEIGHT = 5
OBSTACLE_FREQUENCY = 0.03
OBSTACLE_SPEED = 4
FRAME_DELAY = 0.05

backround = turtle.Screen()
backround = displayio.OnDiskBitmap(

def jump():
    global slime_jump
    if not slime_jump:
        slime_jump = True

def create_obstacle():
    obstacle = turtle.Turtle()
    obstacle.goto(400, GROUND_HEIGHT)
    return obstacle


    
def game_setup():
    """this is called once to initialize your game features"""
    pass

def game_frame(p1_button:bool,p2_button:bool) -> bool:
    """this is called every frame, you need to update all your grame objects
        returns True when the game is over, else return false"""
    if jump():
        jump
    return False


def game_over():
    """this should display your game over screen with score also clean up the game_group"""
    pass

