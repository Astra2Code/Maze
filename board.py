###### PLANSZA ######

import random
import sys 
    
class class_board:
    
    def __init__(self, N, M):
        self.N = N
        self.M = M
        finish = self.wejscie()
        enterance = self.wejscie()
        ex = enterance[0]
        ey = enterance[1]
        fx = finish[0]
        fy = finish[1]
        self.create_board()
        
    def create_board(self):
        self.board = []
        for i in range(self.M*2+2):
            self.board.append('')
            self.board[i] = [1 for j in range(self.N*2+2)]
        #self.set()
        self.sciany()
        #print(board)
        return;
    
    def show_board(self, board):
       for i in range(class_board.M*2+1):
            for j in range(class_board.N*2+1):
                '''if i % 2 == 0:
                    sys.stdout.write('_')
                elif j % 2 == 0:
                    sys.stdout.write('|')
                else:'''
                sys.stdout.write(str(board[i][j]))
            print('')

    def sciany(self):
        for i in range(self.M*2+1):
           self.board[i][0] = 3
           self.board[i][self.N*2] = 3
        for j in range(1,self.N*2):
            self.board[0][j] = 3
            self.board[self.M*2][j] = 3
        return;

    def set_piervious(self):
        if self.enterance[0] < 0 and self.enterance[0] > len(self.board[0])-1:
            self.end('Niepoparawny przedział wartości dla wejścia!')
        elif self.goal[0] < 0 and self.goal[0] > len(self.board[0]):
            self.end('Niepoparawny przedział wartości dla wyjścia!')
        elif self.enterance[1] < 0 and self.enterance[1] > len(self.board)-1:
            self.end('Niepoparawny przedział wartości dla wejścia!')
        elif self.goal[1] < 0 and self.goal[1] > len(self.board)-1:
            self.end('Niepoparawny przedział wartości dla wyjścia!')

    def set(self): # warunki do poprawy
        #self.board[self.ex][self.ey] = 3
        #board[goal[1]][goal[0]] = 4
        return;
    
    
    def losuj(self, board):
        M = len(board)
        N = len(board[0])
        sciany = 0
        for i in range(1,M-2):
            for j in range(1,N-2):
                if i % 2 == 1 and j % 2 == 1:
                    pass
                elif i % 2 == 0 and j % 2 == 0:
                    if board[i][j-1] == 1:
                        sciany +=1
                    if board[i][j+1] == 1:
                        sciany +=1
                    if board[i-1][j] == 1:
                        sciany +=1
                    if board[i+1][j] == 1:
                        sciany +=1
                    board[i][j] = sciany
                else:
                    x = random.randint(1,6)
                    if x < 5:
                        board[i][j] = 2
                sciany = 0 
                
        return board;

    def wejscie(self):
        x = random.randrange(1,(self.N-1)*2,2)
        y = random.randrange(1,(self.M-1)*2,2)
        return (x,y);