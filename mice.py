###### MICE_FINDER ######


import random
from board import class_board

class var():
    mode = 'create'
    begin = 0
    running = True
    ex = 1
    ey = 1
    fx = 1
    fy = 1
    mousex = 0
    mousey = 0

class mice_finder:
    path = []
    nodes = 2

    def __init__(self,board,x,y):
        self.board = board
        self.x = x
        self.y = y

    def start_mice(self):
        self.win_check()
        kierunki = self.wallcheck()
        if kierunki[0] == 1:
            self.x = self.x - 2
            self.reverse_node()
        elif kierunki[1] == 1:
            self.y = self.y - 2
            self.reverse_node()
        elif kierunki[2] == 1:
            self.x = self.x + 2
            self.reverse_node()
        elif kierunki[3] == 1:      
            self.y = self.y + 2
            self.reverse_node()
        else:
            if len(self.path) > 0:
                self.del_nodes(len(self.board[0]), len(self.board))
                self.nodes -= 1
                node = self.path.pop()
                self.x = node[0]
                self.y = node[1]
            else:
                print("Lost")
                var.begin = 0
        
        return self.board;

    def wallcheck(self):
        kierunki = [0,0,0,0]
        if self.board[self.y][self.x-2] >= 0 and self.board[self.y][self.x-1] == 2:
            kierunki[0] = 1          
        if self.board[self.y-2][self.x] >= 0 and self.board[self.y-1][self.x] == 2:
            kierunki[1] = 1    
        if self.board[self.y][self.x+2] >= 0 and self.board[self.y][self.x+1] == 2:
            kierunki[2] = 1    
        if self.board[self.y+2][self.x] >= 0 and self.board[self.y+1][self.x] == 2:
            kierunki[3] = 1
        if sum(kierunki) > 1:
            self.path.append((self.x,self.y))
            self.nodes += 1
        if sum(kierunki) > 1:
            return self.losuj_kierunek(kierunki);
        else:
            return kierunki;

    def losuj_kierunek(self, kierunki):
        while sum(kierunki) > 1:
            it = random.randint(0,3)
            kierunki[it] = 0
        return kierunki;
        

    def del_nodes(self,N,M):
        for i in range(M-1):
            for j in range(N-1):
                if self.board[i][j] == -self.nodes:
                    self.board[i][j] = -1
        return;

    def reverse_node(self):
        if self.y == var.ey and self.x == var.ex:
            print("Win")
            var.begin = 0
        else:
            self.board[self.y][self.x] = -self.nodes
        

    def win_check(self):
        if self.y == var.ey and self.x == var.ex:
            print("Win")
            var.begin = 0


                        ###### MICE_DESTROYER ######


class mice_destroyer:
    path = []
    nodes = 2

    def __init__(self,board,x,y):
        self.board = board
        self.x = x
        self.y = y
        #self.N = len(self.board[0])
        #self.M = len(self.board)

    def start_mice(self):
        kierunki = self.wallcheck()       
        if sum(kierunki) > 0:
            direction = self.random_direction(kierunki) 
            if direction == 0:
                self.board[self.y][self.x-1] = 2 
                self.x = self.x - 2
                self.reverse_node()
            elif direction == 1:
                self.board[self.y-1][self.x] = 2 
                self.y = self.y - 2
                self.reverse_node()
            elif direction == 2:
                self.board[self.y][self.x+1] = 2 
                self.x = self.x + 2
                self.reverse_node()
            elif direction == 3:
                self.board[self.y+1][self.x] = 2 
                self.y = self.y + 2
                self.reverse_node()

            self.path.append((self.x,self.y))
            self.nodes += 1
        else:
            dlugosc = len(self.path)
            if dlugosc > 0:
                #self.del_nodes()
                while sum(self.wallcheck()) == 0:
                    self.nodes -= 1
                    if len(self.path) > 0:
                        node = self.path.pop()
                    else:
                        self.created()
                        break
                    self.x = node[0]
                    self.y = node[1]
        
        
        return self.board;

    def wallcheck(self):
        kierunki = [0,0,0,0]
        if self.board[self.y][self.x-2] > 0 and self.board[self.y][self.x-1] == 1:
            kierunki[0] = 1          
        if self.board[self.y-2][self.x] > 0 and self.board[self.y-1][self.x] == 1:
            kierunki[1] = 1    
        if self.board[self.y][self.x+2] > 0 and self.board[self.y][self.x+1] == 1:
            kierunki[2] = 1    
        if self.board[self.y+2][self.x] > 0 and self.board[self.y+1][self.x] == 1:
            kierunki[3] = 1
        if sum(kierunki) > 1:
            return self.losuj_kierunek(kierunki);
        else:
            return kierunki;

    def del_nodes(self):
        
        for i in range(class_board.M*2-1):
            for j in range(class_board.N*2-1):
                if self.board[i][j] == -self.nodes:
                    self.board[i][j] = -1
        return;

    def losuj_kierunek(self, kierunki):
        while sum(kierunki) > 1:
            it = random.randint(0,3)
            kierunki[it] = 0
        return kierunki;

    def reverse_node(self):
        '''if self.board[self.y][self.x] == 3:
            print("Win")
            engine.begin = 0
        else:'''
        self.board[self.y][self.x] = 0

    def random_direction(self,kierunki):
        dostepne_kierunki = []
        for i in range(4):
            if kierunki[i] == 1:
                dostepne_kierunki.append(i)
        return dostepne_kierunki[random.randint(0,len(dostepne_kierunki)-1)];
        

    def win_check(self):
        if self.board[self.y][self.x] == 3:
            print("Win")
            #engine.begin = 0


    def created(self):
        var.mode = 'find'
        var.begin = 0
        print('Created')
        #for i in range(plansza.M):
            #for j in range(plansza.N):
                #if self.board[i][j] < 0
