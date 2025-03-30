from pygame import *
from random import choice


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
    def updateL(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y>0:
            self.rect.y-=self.speed
        if keys[K_s] and self.rect.y<350:
            self.rect.y += self.speed

    def updateR(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>0:
            self.rect.y-=self.speed
        if keys[K_DOWN] and self.rect.y<350:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__(img, x, y, w, h, speed)
        self.direct = [0,0]

    def update(self):
        global score_l, score_r
        self.rect.x += self.speed*self.direct[0]
        self.rect.y += self.speed*self.direct[1]
        if self.rect.y <= 0 or self.rect.y >= 500-self.rect.height:
            self.direct[1] *= -1
        #if self.rect.x <= 0 or self.rect.x >= 700-self.rect.width:
            #self.direct[0] *= -1
        if self.rect.colliderect(playerL) or self.rect.colliderect(playerR):
            self.direct[0] *= -1
        if self.rect.x <= 0:
            score_r += 1
            self.start()
        if self.rect.x >= 700-self.rect.width:
            score_l += 1
            self.start()




    def start(self):
        self.rect.x = 325
        self.rect.y = 225
        ball.direct[0] = choice([-1,1])
        ball.direct[1] = choice([-1,1])











window = display.set_mode((700,500))
display.set_caption("MinePong")

background = transform.scale(image.load('fonh.jpg'), (700,500))
playerL = Player('mech-Photoroom.png', 5,350,70,150,5)
playerR = Player('mech-Photoroom.png', 625,350,70,150,5)

btn = GameSprite('btn.png', 200,100,350,200,0)

font.init()
font_1 = font.SysFont('Arial',36)
win = ''

ball = Ball('tnt.png', 350-25, 250-25, 80, 80, 5)
ball.direct[0] = choice([-1,1])
ball.direct[1] = choice([-1,1])


clock = time.Clock()
fps = 60


game = True
score_r = 0
score_l = 0
rule = 3
finish = True
menu = True


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if menu:
        window.blit(background, (0,0))
        btn.reset()
        pressed = mouse.get_pressed()
        pos = mouse.get_pos()
        if pressed[0]:
            if btn.rect.collidepoint(pos[0], pos[1]):
                menu = False
                finish = False
                win = ''
                score_l = 0
                score_r = 0
        if win != '':
            winner = font_1.render('Победил '+win+'!', 1, (255,255,255))
            window.blit(winner, (150, 350))
            scr = font_1.render('со счетом '+str(max(score_l,score_r))+':'+str(min(score_l,score_r)), 1, (255,255,255))
            window.blit(scr, (250,400))

    if not finish:
        window.blit(background, (0,0))


        playerL.updateL()
        playerL.reset()
        scr_right = font_1.render(str(score_r), 1, (255,255,255))
        window.blit(scr_right, (670,10))

        

        playerR.updateR()
        playerR.reset()
        scr_left = font_1.render(str(score_l), 1, (255,255,255))
        window.blit(scr_left, (10,10))



        ball.update()
        ball.reset()

        if score_l >= 3:
            win = 'Левый игрок'
            menu = True
            finish = True
        if score_r >= 3:
            win = 'Правый игрок'
            menu = True
            finish = True

    clock.tick(fps)
    display.update()