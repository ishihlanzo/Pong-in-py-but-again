from multiprocessing.sharedctypes import Value
import pygame
import random

class Player:
    def __init__(self,x ,y) :
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 15
        self.velocity = [0, 0]
    
    def move(self) :
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw(self, screen) :
        screen.blit(self.image, self.rect)

class Square:
    def __init__(self,x ,y) :
        self.image = pygame.image.load('square.png')
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 15
        self.velocity = [0, 0]
    
    def move(self) :
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw(self, screen) :
        screen.blit(self.image, self.rect)

class Backgroud:
    def __init__(self,x ,y) :
        self.image = pygame.image.load('background.png')
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 15
        self.velocity = [0, 0]
    
    def move(self) :
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw(self, screen) :
        screen.blit(self.image, self.rect)

class Score:
    def __init__(self,x ,y) :
        self.score = Value
        self.font = pygame.font.Font('Elmono-regular.ttf', 32)
        self.text = self.font.render(str(self.score), True, (255,255,255))
        self.rect = self.text.get_rect(x=x, y=y)

    def draw(self, screen) :
        screen.blit(self.text, self.rect)
