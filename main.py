from template import*
import random
from random import uniform
from random import randint
import tkinter as tk
import tkinter.font as tkFont
import pygame
import time


def Pong():
    FPS = 60
    MOUVEMENT = True
    WIN = 5

    class Game:
        
        def __init__(self, screen):
            self.screen = screen
            self.running = True
            self.clock = pygame.time.Clock()
            self.player_1 = Player(100, 405-45)
            self.player_2 = Player(900, 405-45)
            self.square = Square(450, 425)
            self.background = Backgroud(0,0)
            self.score = [0, 0]
            self.direction = 1
            self.orientation = random.uniform(-0.5, 0.5)
            self.speed_up = 0
            
        def handling_event(self):
            for event in pygame.event.get() :
                    if event.type == pygame.QUIT :
                        self.running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_s] :
                self.player_1.velocity[1] = -1
            elif key[pygame.K_x] :
                self.player_1.velocity[1] = 1
            else : 
                self.player_1.velocity[1] = 0

            if key[pygame.K_j] :
                self.player_2.velocity[1] = -1
            elif key[pygame.K_n] :
                self.player_2.velocity[1] = 1
            else : 
                self.player_2.velocity[1] = 0
            
            if MOUVEMENT :
                self.square.velocity[1] = 1 * self.orientation
                self.square.velocity[0] = 0.5 * self.direction

            if (905 >= self.square.rect.x >= 850) and (len(set(range(self.square.rect.y-25, self.square.rect.y+25)) & set(range(self.player_2.rect.y, self.player_2.rect.y+180))) != 0 ):

                self.direction = 0
                self.direction = -1 - self.speed_up
                if self.direction > -3 :
                    self.speed_up += 0.03


            
            if (95 <= self.square.rect.x <= 110 ) and (len(set(range(self.square.rect.y-50, self.square.rect.y+50)) & set(range(self.player_1.rect.y, self.player_1.rect.y+180))) != 0 )  :

                self.direction = 0
                self.direction = 1 + self.speed_up
                if self.direction < 3 :
                    self.speed_up += 0.03

                
            
            if self.square.rect.y>=850 :
                wait = self.direction
                self.direction = 0
                if self.orientation < 0.40 :
                    self.orientation -= 0.025
                else :
                    self.orientation = -0.4
                self.direction = wait
            
            if self.square.rect.y<=0 :
                wait = self.direction
                self.direction = 0
                if self.orientation > -0.40 :
                    self.orientation += 0.025
                else :
                    self.orientation = 0.4
                self.direction = wait

            if self.square.rect.x <= 0 :
                self.direction = abs(self.direction)
                self.square = Square(450, 425)
                self.speed_up = 0
                self.direction = 1
                time.sleep(0.5)
                self.score[0] += 1
                print(f'--------------------\nPlayer gauche : {self.score[1]}\nPlayer droit : {self.score[0]}')
                if self.score[0] >= WIN :
                    self.running = False
                    print('--------------------\nLe joueur de droit a gagné !!')

                
            
            if self.square.rect.x >= 950 :
                self.direction = -abs(self.direction)
                self.square = Square(450, 425)
                self.speed_up = 0
                self.direction = -1
                time.sleep(0.5)
                
                self.score[1] += 1
                print(f'--------------------\nPlayer gauche : {self.score[1]}\nPlayer droit : {self.score[0]}')
                if self.score[1] >= WIN :
                    self.running = False
                    print('--------------------\nLe joueur de gauche a gagné !!')
            
        def update(self) :
            self.player_1.move()
            self.player_2.move()
            self.square.move()



        def display(self) :
            self.screen.fill('black')
            self.background.draw(self.screen)
            self.player_1.draw(self.screen)
            self.player_2.draw(self.screen)
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
    Game = Game(screen)
    Game.run()


    pygame.quit()






#Les variable : 
font="Helvetica"
backgroud_color = '#EBF6F4'
space = '                                                 '
title = "Are you stupid ?"
longueur = 11
largeur = 3
resizable = True
hide = 700
not_hide = 420
#mise en place de la fenetre

app = tk.Tk()
x=app.winfo_screenwidth()
y=app.winfo_screenheight()
app['background'] = backgroud_color
app.resizable(width=resizable, height=resizable)
app.title(space+title)

#contenu de la page 

AYS = tk.Label(app ,
                        text="Play the game",
                        font=(font,20))   
Yes = tk.Button(app,
                        text="Yes",
                        command=Pong,
                        font=(font,15))

Exit = tk.Button(app,
                        text="Exit",
                        command=app.destroy,
                        font=(font,15))



#affichage des éléments



AYS.pack()
Yes.pack()
Exit.pack()


app.mainloop()

