import pygame, sys
import numpy as np

pygame.init()

BACKGROUND = (4,22,35)
WIDTH = 600
HEIGHT = 600
LINE_COLOR = (20,175,229)
LINE_WIDTH = 13
BOARD_ROWS = 3
BOARD_COL = 3

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BACKGROUND)

game = np.zeros((BOARD_ROWS,BOARD_COL))

def draw_board():
    pygame.draw.line(screen, LINE_COLOR ,(0,200) ,(600,200),LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR ,(0,400) ,(600,400),LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR ,(200,0) ,(200,600),LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR ,(400,0) ,(400,600),LINE_WIDTH)

draw_board()

#MAINLOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()