
'''
Created on Mar 6, 2014

@author: Tryggvi
'''
import os.path
import sys
import pygame
from pygame.locals import*
main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'data/images', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()

def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs

class Card(object):
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit, rank, image):
        self.suit = suit
        self.rank = rank
        self.image = image
        
    def __str__(self):
        return '%s of %s' % (self.rank_names[self.rank], self.suit_names[self.suit])
    
    def __cmp__(self, other):
        # the first item of first tuple is compared to the first item of the second tuple.
        #If they are not equal, this is the result of the comparison, else the second item is considered.
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1,t2)

class Deck(object):
    images = []
    image_count = 0
    def __init__(self):
        self.cards = []
        for suit in range(0,4):
            for rank in range(0,13):
                card = Card(suit,rank,images[image_count])
                image_count +=1
                self.cards.append(card)
                
    def __str__(self):
        strDeck = []
        for card in self.cards:
            strDeck.append(str(card))
        return '\n'.join(strDeck)
    
SCREENRECT     = Rect(0, 0, 640, 480)

def main(winstyle = 0):
    # Initialize pygame
    pygame.init()
    pygame.event.get()
    #define screen
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
    #preload Images
    Deck.images = load_images('01c.gif','02c.gif','03c.gif','04c.gif','05c.gif','06c.gif','07c.gif','08c.gif','09c.gif','10c.gif','11c.gif','12c.gif','13c.gif',\
        '01d.gif','02d.gif','03d.gif','04d.gif','05d.gif','06d.gif','07d.gif','08d.gif','09d.gif','10d.gif','11d.gif','12d.gif','13d.gif',\
        '01h.gif','02h.gif','03h.gif','04h.gif','05h.gif','06h.gif','07h.gif','08h.gif','09h.gif','10h.gif','11h.gif','12h.gif','13h.gif',\
        '01s.gif','02s.gif','03s.gif','04s.gif','05s.gif','06s.gif','07s.gif','08s.gif','09s.gif','10s.gif','11s.gif','12s.gif','13s.gif')
    #decorate window
    icon = pygame.transform.scale(Deck.images[0], (32, 32))
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Pygame Aliens')
    pygame.mouse.set_visible(0)
    

    
    
if __name__ == '__main__': main()
