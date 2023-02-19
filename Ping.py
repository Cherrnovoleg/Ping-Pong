from pygame import *
from random import randint, choice
import math 
window = display.set_mode((1000,800))
display.set_caption('ping-pong')
background = transform.scale(image.load('space.jpg'),(1000,800))
font.init()
font = font.Font(None,50)

#переменные 
game = True 
fps = 60
clock = time.Clock()
list_1 = 0
list_2 = 0
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed            
        if keys_pressed[K_s] and self.rect.y < 680:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed            
        if keys_pressed[K_DOWN] and self.rect.y < 680:
            self.rect.y += self.speed
    def update3(self):
        ball.rect.x+=ball_speed_x
        ball.rect.y+=ball_speed_y
        


#создаю 
player1 = Player('rok.png',25, 25,40,120,15)
player2 = Player('rok2.png',945, 25,40,120,15)
ball = Player('ball.png',500, 300,100,100,15)


ball_speed1 = choice([-6, 6])
ball_speed_x = ball_speed1
ball_speed_y = ball_speed1
while game:   #цикл игры
    for i in event.get(): #выход
        if i.type == QUIT:
            game = False
    if finish != True:    
        if ball.rect.y >= 700:
            ball_speed_y *= -1
        if ball.rect.y <= 10:
            ball_speed_y *= -1
        if sprite.collide_rect(player1, ball) and ball.rect.x <= 40 or sprite.collide_rect(player2, ball) and ball.rect.x <= 965 :
            ball_speed_x *= -1
        if ball.rect.x <= -60: #ЛЕВАЯ ГРАНИЦА счет и возврат 
            list_2+=1
            ball.rect.x = 500
            ball.rect.y = 300
            ball_speed_x *= -1.05
            ball_speed_y *= -1.05
        if ball.rect.x >= 1060: #правая граница счет и возврат 
            list_1+=1
            ball.rect.x = 500
            ball.rect.y = 300
            ball_speed_x *= -1.05
            ball_speed_y *= -1.05
        
        
        h = 10
        player1.update1()
        player1.reset()
        player2.update2()
        player2.reset()
        ball.update3()
        ball.reset()
        
        counter1 = font.render('' + str(list_1), 1, (255,255,255))
        counter2 = font.render('' + str(list_2), 1, (255,255,255))
        speed_window = font.render(str(abs(round((ball_speed_x),1))), 1,(255,255,255))
        window.blit(speed_window,(10,10))
        window.blit(counter1,(470,10))
        window.blit(counter2,(520,10))
        if list_1 == 20:
            win = font.render('PLAYER 1 WIN', True, (0,255,0))
            window.blit(win,(300,200))
            finish = True
        if list_2 == 20:
            win = font.render('PLAYER 2 WIN', True, (0,255,0))
            window.blit(win,(500,200))
            finish = True
    clock.tick(fps)
    display.update()
