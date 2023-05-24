from .constants import WHITE,BLACK,SQUARE_SIZE,GOLD
import pygame


class Piece:
    def __init__(self,row,col,color):
        self.row=row
        self.col=col
        self.color=color
        self.king=False

        if self.color == WHITE:
            self.OPcolor=BLACK
            self.direction=-1
        else:
            self.OPcolor=WHITE
            self.direction=1

        self.x=0
        self.y=0
        self.calc_pos()

    def calc_pos(self):
        self.x=SQUARE_SIZE*self.col+SQUARE_SIZE//2
        self.y=SQUARE_SIZE*self.row+SQUARE_SIZE//2

    def make_king(self):
        self.king=True
    
    def draw(self,win):
        pygame.draw.circle(win,BLACK,(self.x,self.y),30)
        pygame.draw.circle(win,self.color,(self.x,self.y),28)
        if self.king:
            pygame.draw.circle(win,GOLD,(self.x,self.y),7)
        else:
            pygame.draw.circle(win,self.OPcolor,(self.x,self.y),7)

        


    def __repr__(self):
        return str(self.color)
        




