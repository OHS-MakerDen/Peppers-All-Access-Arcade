import displayio

game_group = displayio.Group()

# Constants
GROUND_HEIGHT = -16
SLIME_JUMP_HEIGHT = 5
OBSTACLE_FREQUENCY = 0.03
OBSTACLE_SPEED = 4
FRAME_DELAY = 0.05

# Set up the screen
screen = turtle.Screen()
screen.title("Slime Jump")
screen.bgcolor("white")
screen.setup(width=64, height=64)

#backround
backround = displayio.TileGrid("caveBack.bmp")

#spawn slime
slime = displayio.OnDiskBitmap("slime/slime_jump.bmp")
slime.goto(-30, GROUND_HEIGHT)

# Obstacle
def create_obstacle():
    obstacle = turtle.Turtle()
    obstacle.goto(30, GROUND_HEIGHT)
    return obstacle

obstacles = []

# Functions
def jump():
    if p1_clicked = True:
        global slime_jump
        if not slime_jump:
            slime_jump = True

# Game loop
slime_jump = False
running = True
while running:
    # Move slime
    if slime_jump:
        slime.sety(slime.ycor() + 4)
        if slime.ycor() >= GROUND_HEIGHT + SLIME_JUMP_HEIGHT:
            slime_jump = False
    else:
        if slime.ycor() > GROUND_HEIGHT:
            slime.sety(slime.ycor() - 4)
            if slime.ycor() <= GROUND_HEIGHT:
                slime.sety(GROUND_HEIGHT)

    # Create new obstacles
    if random.random() < OBSTACLE_FREQUENCY:
        obstacle = create_obstacle()
        obstacles.append(obstacle)

    # Move obstacles
    for obstacle in obstacles:
        obstacle.setx(obstacle.xcor() - OBSTACLE_SPEED)

    # Remove off-screen obstacles
    obstacles = [obstacle for obstacle in obstacles if obstacle.xcor() > -32]

    # Check for collisions
    for obstacle in obstacles:
        if (
            slime.xcor() - 2 < obstacle.xcor() < slime.xcor() + 2
            and slime.ycor() - 2 < obstacle.ycor() < slime.ycor() + 2
        ):
            print("Game Over!")
            running = False
            
# Close the window when the game ends
turtle.bye()# Write your code here :-)
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

