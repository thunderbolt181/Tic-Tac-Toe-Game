import pygame, sys
import numpy as np

pygame.init()

CLOSE = True
BACKGROUND = (4,22,35)
WIDTH = 600
HEIGHT = 600
LINE_COLOR = (20,175,229)
LINE_WIDTH = 13
BOARD_ROWS = 3
BOARD_COL = 3
CROSS_IMG = pygame.image.load("cross.png")
CIRCLE_IMG = pygame.image.load("Circle.png")
CROSS = True

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BACKGROUND)
font = pygame.font.SysFont("Times New Roman, Arial", 30) #font

def check_tie(game):
    for row in game:
        if 0 in row:
            return False
    return True

def check_win(game):
    win = False
    if game[1][1] !=0:
        if game[0][0]==game[1][1] and game[1][1]==game[2][2]:
            win = True
        elif game[0][2]==game[1][1] and game[1][1]==game[2][0]:
            win = True
        if win:
            return win
    l=[0,0,0]
    for row in game:
        if (1 not in row or -1 not in row) and 0 not in row:
            win = True
            return win
        else:
            for i in range(3):
                if row[i]!=0:
                    l[i]+=row[i]
    if -3 in l or 3 in l:
        win = True
    return win

def draw_board():
    pygame.draw.line(screen, LINE_COLOR ,(0,200) ,(600,200),LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR ,(0,400) ,(600,400),LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR ,(200,0) ,(200,600),LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR ,(400,0) ,(400,600),LINE_WIDTH)
draw_board()

def update_board(clicked_row,clicked_col,cross):
    if game[clicked_col][clicked_row] == 0:
        # Row Position
        if clicked_row == 0:posX = 25
        elif clicked_row == 1:posX = 225
        elif clicked_row == 2:posX = 425

        # Column Position
        if clicked_col == 0:posY = 25
        elif clicked_col == 1:posY = 225
        elif clicked_col == 2:posY = 425

        if cross:
            screen.blit(CROSS_IMG,(posX,posY))
            game[clicked_col][clicked_row] = 1
        else:
            screen.blit(CIRCLE_IMG,(posX,posY))
            game[clicked_col][clicked_row] = -1

game = np.zeros((BOARD_ROWS,BOARD_COL))

# MAINLOOP
while CLOSE:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CLOSE=False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0] # x
            mouseY = event.pos[1] # y
            clicked_col = int(mouseY//200)
            clicked_row = int(mouseX//200)
            if CROSS:
                update_board(clicked_row,clicked_col,True)
                CROSS = False
            else:
                update_board(clicked_row,clicked_col,False)
                CROSS = True
            
            if check_win(game):
                print("win")
                screen.fill(BACKGROUND)
                pygame.draw.line(screen, LINE_COLOR ,(0,300) ,(600,300), 200)
                if not CROSS:
                    screen.blit(CROSS_IMG,(25,225))
                else:
                    screen.blit(CIRCLE_IMG,(25,225))
                break
            elif check_tie(game):
                print("Tie")
                break
    
    pygame.display.update()

pygame.quit()