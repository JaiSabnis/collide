import pygame as pg
from settings import *

playerRadius = 30
playerThiccness = round(playerRadius/10)

headRadius = round(playerRadius/2.2)
headDistance = playerRadius + (playerThiccness *6)

handRadius = 10


LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"
NONE = "none"

GRAVITY = 10

headPosition = {
        NONE: 0,
        LEFT: -30,
        RIGHT: 30,
    }

gameWidth = 1280
gameHeight = 720


class Player(pg.sprite.Sprite):
    def __init__(self, window):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = -150
        self.location = (self.x, self.y)
        self.rect.center = self.location

        self.color = WHITE

        self.headMoving = True
        self.headLocation = 0
        self.vel = 8
        self.window = window
        self.direction = NONE

    def draw(self):
        self.drawHead()
        pg.draw.circle(self.window, self.color, self.location, playerRadius, playerThiccness)

    def drawHead(self):
        headOffset = headPosition.get(self.direction, 0)
        headLocation = (self.x + headOffset, self.y - headDistance)
        pg.draw.circle(self.window, self.color, headLocation, headRadius, playerThiccness)

    def move(self):
        keys = pg.key.get_pressed()
        '''
        noKeysPressed = not (keys[pg.K_LEFT] or keys[pg.K_LEFT] or keys[pg.K_UP] or keys[pg.K_DOWN] or keys[pg.K_SPACE])
        if noKeysPressed:
            self.direction = NONE
            '''

        if keys[pg.K_LEFT]:
            self.x -= self.vel
            self.direction = LEFT

        if keys[pg.K_RIGHT]:
            self.x += self.vel
            self.direction = RIGHT

        if not keys[pg.K_RIGHT] and not keys[pg.K_LEFT]:
            self.direction = NONE

        if keys[pg.K_UP]:
            self.y -= self.vel

        if keys[pg.K_DOWN]:
            self.y += self.vel

        self.y += GRAVITY
        self.update()

    def update(self):
        if self.x <= playerRadius:
            self.x = playerRadius
        elif self.x >= gameWidth - playerRadius:
            self.x = gameWidth - playerRadius

        self.location = (self.x, self.y)
