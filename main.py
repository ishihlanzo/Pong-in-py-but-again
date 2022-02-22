from re import X
from shutil import move
from player_template import*



import pygame


FPS = 60

movement = True

class game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.player1 = player(30, 405)
        self.player2 = player(970, 405)
        self.square = square(100, 100)

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
        
        if movement == True :
            self.square.velocity[1] = 0
            self.square.velocity[0] = 0.25
        
        



    def update(self) :
        self.player1.move()
        self.player2.move()
        self.square.move()
        '''
        if self.player2.colliderect(self.player2, self.square) :
            print('aaa')
        '''

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