from player_template import*
import random


import pygame



FPS = 60

movement = True

class game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.player1 = player(100, 405-45)
        self.player2 = player(900, 405-45)
        self.square = square(450, 425)
        self.direction = 1
        self.orientation = random.uniform(0, 0.5)
        self.speed_up = 0


    def handling_event(self):
        for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    self.running = False
        key = pygame.key.get_pressed()
        if key[pygame.K_s] :
            self.player1.velocity[1] = -1
        elif key[pygame.K_x] :
            self.player1.velocity[1] = 1
        else : 
            self.player1.velocity[1] = 0

        if key[pygame.K_j] :
            self.player2.velocity[1] = -1
        elif key[pygame.K_n] :
            self.player2.velocity[1] = 1
        else : 
            self.player2.velocity[1] = 0
        
        if movement :
            self.square.velocity[1] = 1 * self.orientation
            self.square.velocity[0] = 0.5 * self.direction

        if (905 >= self.square.rect.x >= 850) and (len(set(range(self.square.rect.y-25, self.square.rect.y+25)) & set(range(self.player2.rect.y, self.player2.rect.y+180))) != 0 ):
            self.direction = -1 - self.speed_up
            self.speed_up += 0.01

        
        if (95 <= self.square.rect.x <= 110 ) and (len(set(range(self.square.rect.y-50, self.square.rect.y+50)) & set(range(self.player1.rect.y, self.player1.rect.y+180))) != 0 )  :
            self.direction = 1 + self.speed_up
            self.speed_up += 0.01
        
        if self.square.rect.y>=850 :
            wait = self.direction
            self.direction = 0
            if self.orientation < 0.40 :
                self.orientation -= 0.025
            else :
                self.orientation = -0.4
            self.direction = wait
            
            print(self.orientation)
        
        if self.square.rect.y<=0 :
            wait = self.direction
            self.direction = 0
            if self.orientation > -0.40 :
                self.orientation += 0.025
            else :
                self.orientation = 0.4
            self.direction = wait
            print(self.orientation)
        
        



    def update(self) :
        self.player1.move()
        self.player2.move()
        self.square.move()

    def display(self) :
        self.screen.fill('black')
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)
        self.square.draw(self.screen)
        pygame.display.flip()

    def run(self) :
        while self.running :
            self.handling_event()
            self.update()
            self.display()
            self.clock.tick(FPS)

pygame.init()
screen = pygame.display.set_mode((1000, 900))
game = game(screen)
game.run()


pygame.quit()