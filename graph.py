###### GRAPHICS ######

import pygame

from mice import mice_finder, var


class graphics():
    BLACK = (  0,   0,   0)
    WHITE = (255, 255, 255)
    RED   = (255,   0,   0)
    GREEN = (  0, 255,   0)
    BLUE  = (  0,   0, 255)
    GRAY = (220,220,255)
    STARTING_POINT =(0,0)
    linet = 2
    tiles = 14
    jump = linet + tiles
    
    def draw_board(SCREEN, board, WINDOW_SIZE,engine):
        M = len(board)
        N = len(board[0])
        graphics.STARTING_POINT = ((WINDOW_SIZE[0] - (graphics.linet*(N//2) + ((N-1)//2)* graphics.tiles ))//2, (WINDOW_SIZE[1] - (graphics.linet * (M//2) + ((M-1)//2)* graphics.tiles))//2)
        SCREEN.fill(graphics.WHITE)
        for i in range(M-1):
            for j in range(N-1):
                if i % 2 == 0 and not j % 2 == 0:
                    if board[i][j] == 1 or board[i][j] == 3:
                        pygame.draw.line(SCREEN, graphics.BLACK, graphics.startlineH(i, j), graphics.endlineH(i, j), graphics.linet)
                elif j % 2 == 0 and not i % 2 == 0:
                    if board[i][j] == 1 or board[i][j] == 3:
                        pygame.draw.line(SCREEN, graphics.BLACK, graphics.startlineD(i, j), graphics.endlineD(i, j), graphics.linet)
                    #if i == M - 3:
                     #   pygame.draw.line(SCREEN, graphics.BLACK, graphics.startlineH(i+2, j), graphics.endlineH(i+2, j), graphics.linet)
                    #if j == N - 3:
                     #   pygame.draw.line(SCREEN, graphics.BLACK, graphics.startlineD(i, j+2), graphics.endlineD(i, j+2), graphics.linet)
                #if board[i][j] == 4:
                    #x = j//2*(graphics.jump) + graphics.STARTING_POINT[0] + graphics.jump//2 +1
                    #y = i//2*(graphics.jump) + graphics.STARTING_POINT[1] + graphics.jump//2 +1
                    #pygame.draw.circle(SCREEN, graphics.RED,(x,y),4)
                elif board[i][j] < -1:
                    x = j//2*(graphics.jump) + graphics.STARTING_POINT[0] + graphics.jump//2 +1
                    y = i//2*(graphics.jump) + graphics.STARTING_POINT[1] + graphics.jump//2 +1
                    pygame.draw.circle(SCREEN, graphics.BLUE,(x,y),4)
                elif board[i][j] == -1:
                    x = j//2*(graphics.jump) + graphics.STARTING_POINT[0] + graphics.jump//2 +1
                    y = i//2*(graphics.jump) + graphics.STARTING_POINT[1] + graphics.jump//2 +1
                    pygame.draw.circle(SCREEN, graphics.GRAY,(x,y),4)
                if i == var.ex and j == var.ey:
                    x = j//2*(graphics.jump) + graphics.STARTING_POINT[0] + graphics.jump//2 +1
                    y = i//2*(graphics.jump) + graphics.STARTING_POINT[1] + graphics.jump//2 +1
                    pygame.draw.circle(SCREEN, graphics.GREEN,(x,y),4)
                
                    

    def startlineH(i, j):
        x = (j//2)*(graphics.jump) + graphics.STARTING_POINT[0] + graphics.linet 
        y = (i//2)*(graphics.jump) + graphics.STARTING_POINT[1]
        return(x,y)

    def endlineH(i, j):
        x = (j//2)*(graphics.jump) + graphics.STARTING_POINT[0] + graphics.tiles  
        y = (i//2)*(graphics.jump) + graphics.STARTING_POINT[1]
        return(x,y)
    
    def startlineD(i, j):
        x = (j//2)*(graphics.jump) + graphics.STARTING_POINT[0]  
        y = (i//2)*(graphics.jump) + graphics.STARTING_POINT[1] + graphics.linet
        return(x,y)

    def endlineD(i, j):
        x = (j//2)*(graphics.jump) + graphics.STARTING_POINT[0] 
        y = (i//2)*(graphics.jump) + graphics.STARTING_POINT[1] + graphics.tiles 
        return(x,y)