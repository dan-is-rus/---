
from random import randint
from pygame import *

FPS = 60
clock = time.Clock()

okno = display.set_mode((700,500))


color_disp = (173, 216, 230)
okno.fill(color_disp)


class Game_sprite(sprite.Sprite):
    def __init__(self, namepic, x, y, speed=None, wd=20, hd=100, disp=okno):
        super().__init__()
        self.rect = 
        self.sd = speed
        self.rect.x = x
        self.rect.y = y
        self.disp = disp
    
    def reset(self):
        self.disp.blit(self.image, (self.rect.x, self.rect.y))



class Raketa(Game_sprite):
    def rul(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.sd
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.sd
    

'''
class Enemy(Game_sprite):
    def update(self):


'''


first_player = Raketa()



























































game = True

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False


    clock.tick(FPS)
    display.update()