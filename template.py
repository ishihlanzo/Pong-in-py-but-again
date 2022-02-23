import pygame
import random


NSFW = 'off'
if NSFW == 'on' :
    NSFW = '-NSFW'
else :
    NSFW = ''


class Player:
    def __init__(self,x ,y) :
        self.image = pygame.image.load(f'texture/player{NSFW}.png')
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 15
        self.velocity = [0, 0]
    
    def move(self) :
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw(self, screen) :
        screen.blit(self.image, self.rect)

class Square:
    def __init__(self,x ,y) :
        self.image = pygame.image.load(f'texture/square{NSFW}.png')
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 15
        self.velocity = [0, 0]
    
    def move(self) :
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw(self, screen) :
        screen.blit(self.image, self.rect)

class Backgroud:
    def __init__(self,x ,y) :
        self.image = pygame.image.load(f'texture/background{NSFW}.png')
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 15
        self.velocity = [0, 0]
    
    def move(self) :
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw(self, screen) :
        screen.blit(self.image, self.rect)

score = [0,0]

class Score:
    def __init__(self,x ,y) :
        self.font = pygame.font.Font('font/Cascadia.ttf', 32)
        self.text = self.font.render(str(score), True, (255,255,255))
        self.rect = self.text.get_rect(x=x, y=y)
        self.speed = 15
        self.velocity = [0, 0]
    
    def move(self) :
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw(self, screen) :
        screen.blit(self.text, self.rect)
        score[1] +=1
        print(score)
