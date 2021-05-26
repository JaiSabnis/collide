import pygame as pg
from settings import *
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((50, 50))
        self.image.fill(BOU_RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)


    def jump(self):
        # jump only if standing on a platform
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP

    def draw(self):
        pg.draw.circle(self.image, YELLOW, (self.pos.x , self.pos.y), playerRadius, playerThiccness)

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        if keys[pg.K_UP]:
            self.jump()

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, velX, velY):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.set_alpha(150)
        self.velX = velX
        self.velY = velY

    def update(self):
        self.rect.x += self.velX
        self.rect.y -= self.velY

        if self.rect.midright[0] > WIDTH or self.rect.midleft[0] < 0:
            self.velX = -self.velX

        if self.rect.midtop[1] < 0 or self.rect.midbottom[1] > HEIGHT:
            self.velY = -self.velY



        '''
        
            
        
        if self.pos.y < HEIGHT:
            self.pos.y = 0
        if self.pos.y > 0:
            self.pos.x = HEIGHT

    '''

