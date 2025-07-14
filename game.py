
from random import randint
from pygame import *
from random import randint
font.init()
if randint(0,1):
    forward = 1
else:
    forward = -1

font_s = font.SysFont("Arial", 40)

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
        self.rect = Rect(x-radius*2, y-radius*2, radius*2, radius*2)
        self.sd_y = speed * gobal
        self.sd_x = speed * forward
        self.disp = disp
        self.radius = radius

    def reset_ball(self):
        self.rect.x += self.sd_x
        self.rect.y+= self.sd_y
        if self.rect.y >= 440 or self.rect.y <=20:
            self.sd_y *= -1
        if sprite.spritecollide(self,players, False):
            self.sd_x *= -1
#        draw.rect(okno, (0,0,0), self.rect)
        draw.circle(self.disp, (250, 200, 0), self.rect.center, self.radius)

ball = Ball(300, 200, 5, 40)






game = True
lose = False
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    okno.fill(color_disp)
    
    if not lose:

        okno.fill(color_disp)
        ball.reset_ball()

        first_player.rul()
        second_player.rul(K_w, K_s)


        
        if ball.rect.x < 0:
            lose = True
            text = font_s.render(
                "Правый победил", True, (0,0,0)
            )
        elif ball.rect.x > 700:
            lose = True
            text = font_s.render(
                "Левый победил", True, (0,0,0)
            )
    else:
        okno.blit(text, (100,100))




    clock.tick(FPS)
    display.update()
