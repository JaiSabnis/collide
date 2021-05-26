TITLE = "Jumpy!"
WIDTH = 1280
HEIGHT = 600
FPS = 60

# Player properties
PLAYER_ACC = 1
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20
playerRadius = 30
playerThiccness = round(playerRadius/10)

# Starting platforms (x, y, width, height)
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH * 0.5, 40, 1, 1),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, 2, 0),
                 (125, HEIGHT - 350, 100, 20, 1.5, 0),
                 (350, 200, 100, 20, 0, 0),
                 (175, 100, 50, 20, 0, 0)]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)

BOU_RED = "#DE4839"
BOU_BLUE = "#03C6C7"