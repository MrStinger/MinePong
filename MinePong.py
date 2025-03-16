from pygame import *
from random import randint


class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y>0:
            self.rect.y-=self.speed
        if keys[K_s] and self.rect.y>100:
            self.rect.y += self.speed






window = display.set_mode((700,500))
display.set_caption("MinePong")

background = transform.scale(image.load('fonh.jpg'), (700,500))
player = Player('mech.png', 20,400,200,170,5)

clock = time.Clock()
fps = 60


game = True
finish = True


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0,0))


    player.update()
    player.reset()


    clock.tick(fps)
    display.update()