
from random import randint
from pygame import *
from random import randint
if randint(0,1):
    forward = 1
else:
    forward = -1

if randint(0,1):
    gobal = 1
else:
    gobal = -1

FPS = 60
clock = time.Clock()

okno = display.set_mode((700,500))
display.set_caption("Докатились")


color_disp = (173, 216, 230)
okno.fill(color_disp)


class Game_sprite(sprite.Sprite):
    def __init__(self, x, y, speed=None, wd=20, hd=180, disp=okno):
        super().__init__()
        self.rect = Rect(x, y, wd, hd)
        draw.rect(okno, (0,0,0), self.rect)
        self.sd = speed
        self.disp = disp
        self.image = None
    
    def reset(self):
        draw.rect(self.disp, (0,0,0), self.rect)



class Raketa(Game_sprite):
    def rul(self, up=K_UP, down=K_DOWN):
        keys_pressed = key.get_pressed()
        if keys_pressed[up] and self.rect.y > 0:
            self.rect.y -= self.sd
        if keys_pressed[down] and self.rect.y < 320:
            self.rect.y += self.sd
        self.reset()
    


first_player = Raketa(20, 100, 10)

second_player = Raketa(660, 100, 10)


players = sprite.Group()
players.add(first_player)
players.add(second_player)

class Ball(sprite.Sprite):
    def __init__(self, x, y, speed, radius, disp=okno):
        super().__init__()
        self.rect = draw.circle(okno, (250, 200, 0), (x,y), radius)
        self.sd_y = speed * gobal
        self.sd_x = speed * forward
        self.disp = disp
        self.radius = radius
#    def going(self):
    def reset_ball(self):
        
        self.rect.x += self.sd_x
        self.rect.y += self.sd_y
        if self.rect.y >= 480 or self.rect.y <=20:
            self.sd_y *= -1
        if sprite.spritecollide(self,players, False):
            self.sd_x *= -1
        draw.rect(okno, (0,0,0), self.rect)
        draw.circle(self.disp, (250, 200, 0), (self.rect.x, self.rect.y), self.radius)

ball = Ball(300, 200, 5, 40)




















































game = True

while game:

    okno.fill(color_disp)
    ball.reset_ball()

    first_player.rul()
    second_player.rul(K_w, K_s)

    for e in event.get():
        if e.type == QUIT:
            game = False


    clock.tick(FPS)
    display.update()
