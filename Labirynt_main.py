#import init
## Initiator function, mices in one class, events class
## checkpoints
## textboxes and buttons
                        ###### GLOBAL VARIABLES ######
### initiate ###


from pygame.locals import *
import pygame, sys, time, random
import graph, board, mice


class initiate():
    #begin = 0
    #mode = 'create'

    def __init__(self):
        pygame.init()
        #self.mode = 'create'
        #self.begin = 0
        #ex = 2
        #ey = 2
        self.WINDOW_SIZE = (800, 600)
        self.SCREEN = pygame.display.set_mode(self.WINDOW_SIZE)
        self.POP = pygame.display.set_mode(self.WINDOW_SIZE)
        #15x15 pixeli na jedno pole
        pygame.display.set_caption('Labirynt')
        self.CLOCK = pygame.time.Clock()
        self.plansza = board.class_board(30,30)
        self.myszka = mice.mice_destroyer(self.plansza.board,random.randrange(1,(self.plansza.N-1)*2,2),random.randrange(1,(self.plansza.M-1)*2,2))
        self.myszka_find = mice.mice_finder(self.plansza.board, 59, 59
                                       )
        self.myszka.reverse_node()
        graph.graphics.draw_board(self.SCREEN, self.plansza.board, self.WINDOW_SIZE,self)
        pygame.display.flip()


        


                ###### GAME ######

def events():
        events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                # elif event.key == pygame.K_F4 and alt_pressed:
                #     quit_attempt = True
                elif event.key == pygame.K_SPACE:
                    if mice.var.begin == 0:   
                        mice.var.begin = 1
                    else:
                        mice.var.begin = 0
            '''elif event.type == MOUSEMOTION and event.type == MOUSEBUTTONUP:
                engine.mousex, engine.mousey = event.pos
                mouse.click(engine.mousex, engine.mousey)'''
            if quit_attempt:
                mice.var.running = False
            else:
                events.append(event) 

def game():
    engine = initiate()

    while mice.var.running:
        events()
        if mice.var.begin == 1:
            if mice.var.mode == 'create':
                engine.plansza.board = engine.myszka.start_mice()
            if mice.var.mode == 'find':
                engine.plansza.board = engine.myszka_find.start_mice()
            if mice.var.mode == 'menu':
                pass
            graph.graphics.draw_board(engine.SCREEN, engine.plansza.board, engine.WINDOW_SIZE,engine)
            pygame.display.flip()
            engine.CLOCK.tick(120)
    
def end(string = "Poprawnie zakończono działanie programu!"):
    print(string)
    pygame.quit()
    sys.exit()
    
                        ###### MOUSE ######

class Mouse():
    
    def __init__(self):
       mode =  self.mode
        
game()
end()
