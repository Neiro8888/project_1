from pygame import *
import time as t
run = True
display.set_caption('N-F-P')


icon_image = image.load('Icon.png')



display.set_icon(icon_image)

bg = image.load('bg1.png')

winez = image.load('win.png')
lose = image.load('Loss.png')








mouse.set_visible(False)

window = display.set_mode((400,400))

window.blit(bg,(0,0))

back = (52,52,52)

window.fill(back)
class Abc(sprite.Sprite):
    def __init__(self,w,h,x,y,color=None):
        super().__init__()
        
        self.rect = Rect(x,y,w,h)
        self.color = color
    def dra(self):
        draw.rect(window,self.color,self.rect)
class Pic(sprite.Sprite):
    def __init__(self,pic,w,h,x,y):
        super().__init__()
        self.image = transform.scale(image.load(pic), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def fire(self,b):
        b.rect.x = self.rect.x
        b.rect.y = self.rect.y

class Enemy(Pic):
    def __init__(self,picture, w, h, x, y, speed):
        super().__init__(picture, w, h, x, y)
        self.speed = speed
    def update(self, left, right):
        self.rect.x += self.speed
        if self.rect.x < left:
            self.speed *= -1
        if self.rect.x > right:
            self.speed *= -1
class Bullet(Pic):
    def __init__(self,picture, w, h, x, y, speed):
        super().__init__(picture, w, h, x, y)
        self.speed = speed
    def update(self,parametr):
        self.rect.x += self.speed
        if self.rect.x > 400:
            self.kill()
            parametr = False

        


    

x = 200
y = 200
  
width = 20
height = 20
g1 = Abc(1,400,-10,0,back)
g2 = Abc(400,1,0,-10,back)
g3 = Abc(1,400,-10,0,back)
g4 = Abc(400,1,0,-10,back)
a = Pic('wall.png',100,400,100,125)

a1 = Pic('wall2.png',100,150,70,0)

a2 = Pic('wall3.png',40,50,-10,100)

a3 = Pic('wall4.png',180,25,30,185)
a5 = Pic('wall4.png',180,25,160,100)
a4 = Pic('wall5.png',100,300,-32,250)
a6 = Pic('wall4.png',180,25,250,170)
a7 = Pic('wall4.png',180,25,160,230)
port = Pic('portal.png',20,40,75,346)

port1 = Pic('portal 2.png',20,40,170,10)

b = Pic('mh.png',25,20,0,0)

enemy = Enemy('enemy.png',50,40,300,50,1)

pl = Bullet('bullet.png',20,30,0,0,3)

finish = Pic('finish.png',40,40,300,300)
bullet = Bullet('bullet.png', 15, 10, b.rect.x, b.rect.y, 10)
life = Pic('life.png', 25,25,375,0)
life1 = Pic('life.png', 25,25,350,0)
life2 = Pic('life.png', 25,25,325,0)
app = 0
cheat = True
abc = False
win = False
loss = False
count_life = 3
gun = False
en = True
while run:
    window.blit(bg,(0,0))
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    kes = key.get_pressed()
    if kes[K_d]:
        b.rect.x += 1
    if kes[K_a]:
        b.rect.x -= 1
    if kes[K_s]:
        b.rect.y += 1
    if kes[K_w]:
        b.rect.y -= 1
    if kes[K_q]:
        cheat = True
    if kes[K_e]:
        cheat = False
    if kes[K_SPACE]:
        if app > 50:
            b.fire(bullet)
            app = 0
            gun = True
        


    if cheat == True:
        #коллизия
        if sprite.collide_rect(b,a):
            b.rect.x = 0
            b.rect.y = 0
            count_life -= 1
        if sprite.collide_rect(b,a1):
            b.rect.x = 0
            b.rect.y = 0
            count_life -= 1
        if sprite.collide_rect(b,a2):
            b.rect.x = 0
            b.rect.y = 0
            count_life -= 1
        if sprite.collide_rect(b,a3):
            b.rect.x = 0
            b.rect.y = 0
            count_life -= 1
        if sprite.collide_rect(b,a4):
            b.rect.x = 0
            b.rect.y = 0
            count_life -= 1
        if sprite.collide_rect(b,port):
            b.rect.x = port1.rect.x
            b.rect.y = port1.rect.y
        if sprite.collide_rect(b,enemy):
            b.rect.x = 0
            b.rect.y = 0
        if sprite.collide_rect(b,finish):
            run = False
            win = True
        if sprite.collide_rect(b,g1):
            b.rect.x = 0
            b.rect.y = 0
            count_life -= 1
        if sprite.collide_rect(b,g2):
            b.rect.x = 0
            b.rect.y = 0
            count_life -= 1
        if sprite.collide_rect(b,g3):
            b.rect.x = 0
            b.rect.y = 0
            count_life -= 1
        if sprite.collide_rect(b,g4):
            b.rect.x = 0
            b.rect.y = 0
            count_life -= 1
        if sprite.collide_rect(a,bullet):
            gun = False
        if sprite.collide_rect(a1,bullet):
            gun = False
        if sprite.collide_rect(a2,bullet):
            gun = False
        if sprite.collide_rect(a3,bullet):
            gun = False
        if sprite.collide_rect(a4,bullet):
            gun = False
        if sprite.collide_rect(enemy,bullet):
            gun = False
            en = False
            enemy.rect.x = 1400
    
    
    #By Neiro 

    b.reset()
    a.reset()
    a1.reset()
    a2.reset()
    a3.reset()
    a4.reset()
    a5.reset()
    a6.reset()
    a7.reset()
    g1.dra()
    g2.dra()
    g3.dra()
    g4.dra()
    finish.reset()
    if en == True:
        enemy.reset()
        enemy.update(300,350)
    
    port.reset()
    if gun == True:
        bullet.reset()
        bullet.update(gun)
    if count_life == 3:
        life.reset()
        life1.reset()
        life2.reset()
    elif count_life == 2:
        
        life1.reset()
        life2.reset()
    elif count_life == 1:
        life2.reset()
    if count_life == 0:
        loss = True
        run = False
        
    app += 1
    port1.reset()
    print(app)
    time.Clock().tick(60)
    display.update()
if win == True:
    window.blit(winez,(0,0))
    display.update()
    t.sleep(2.5)
if loss == True:
    window.blit(lose,(0,0))
    display.update()
    t.sleep(2.5)