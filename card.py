
'''
Created on Mar 6, 2014

@author: Tryggvi
'''
import pygame
from globals import *
from preloader import load_image

class Card(pygame.sprite.Sprite):
    """
    The Card class represents a playing-card in the game. 
    In it, all card logic and card images are stored.
    """
    
    suit_names = ["Diamonds", "Clubs", "Hearts", "Spades"]
    rank_names = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit, rank, front, x, y,parent):
        pygame.sprite.Sprite.__init__(self)
        self.suit = suit
        self.rank = rank
        self.front = front
        self.back = load_image('hidden_owl.png')
        self.image = self.back
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)      
        self.hidden = True
        self.isTop = False
        
    def __str__(self):
        return '%s of %s' % (self.rank_names[self.rank], self.suit_names[self.suit])
    
    def __cmp__(self, other):
        """ The first item of first tuple is compared to the first item of the second tuple.
        If they are not equal, this is the result of the comparison, else the second item is considered.
        """
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1,t2)
    
    def flip(self):
        self.image = self.front
        self.hidden = False

    def flip_back(self):
        self.image = self.back
        self.hidden = True
    
    def move_center_to(self, *args):
        if len(args) == 1 :
            assert isinstance(args[0], tuple), 'Argument should be a tuple!'
            self.rect.center = args[0]
        else :
            try:
                self.rect.center = (args[0],args[1])
            except (AttributeError, TypeError):
                raise AssertionError('Input variables should be x and y coordinates')
        
    def update(self):
            if not self.hidden :
                self.rect.center = pygame.mouse.get_pos()

def main():
    print Card.__doc__

if __name__ == '__main__': main()
