
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

class Card(object):
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit, rank, image, x, y):
        self.suit = suit
        self.rank = rank
        self.image = image
        self.x = x
        self.y = y
        
    def __str__(self):
        return '%s of %s' % (self.rank_names[self.rank], self.suit_names[self.suit])
    
    def __cmp__(self, other):
        # the first item of first tuple is compared to the first item of the second tuple.
        #If they are not equal, this is the result of the comparison, else the second item is considered.
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1,t2)

SCREENRECT     = Rect(0, 0, 640, 480)

def main(winstyle = 0):
    # Initialize pygame
    pygame.init()
    pygame.event.get()
    #define screen
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    
    #decorate window
    #icon = pygame.transform.scale(Deck.images[0], (32, 32))
    #pygame.display.set_icon(icon)
    
    pygame.display.set_caption('Pygame Aliens')
    pygame.mouse.set_visible(0)
    
    
if __name__ == '__main__': main()
