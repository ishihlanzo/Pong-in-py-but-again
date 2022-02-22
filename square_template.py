#oui c'est exactement le même que le player, juste le skin change mais chutttt

import pygame

class player1:
    def __init__(self,x ,y) :
        self.image = pygame.image.load('square.png')
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 15
        self.velocity = [0, 0]
    
    def move(self) :
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw(self, screen) :
        screen.blit(self.image, self.rect)