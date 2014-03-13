
'''
Created on Mar 6, 2014

@author: Tryggvi
'''
import os.path
import sys
import pygame
from pygame.locals import*
import random
from preloader import *

class Card(pygame.sprite.Sprite):
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]


    def __init__(self, suit, rank, front, x, y,parent):
        pygame.sprite.Sprite.__init__(self)
        self.suit = suit
        self.rank = rank
        self.front = front
        self.back = load_image('hidden.gif')
        self.image = self.back
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.hidden = True
        self.parent = parent
        self.isTop = False

        self.post_init()
        
    def post_init(self):
        self.rect.center = (self.x,self.y)
        
    def __str__(self):
        return '%s of %s' % (self.rank_names[self.rank], self.suit_names[self.suit])
    
    def __cmp__(self, other):
        # the first item of first tuple is compared to the first item of the second tuple.
        #If they are not equal, this is the result of the comparison, else the second item is considered.
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1,t2)
    
    def flip(self):
        self.image = self.front
        self.hidden = False
    
    def move_center_to(self,x,y):
        self.rect.center = (x,y)
        
    def update(self):
        if not self.hidden :
            if self.rect.collidepoint(pygame.mouse.get_pos()) and self.isTop:
                self.rect.center = pygame.mouse.get_pos()
        else :
            #self.flip()
            pass


def main():
   pass
if __name__ == '__main__': main()
