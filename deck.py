'''
Created on Mar 7, 2014

@author: Tryggvi
'''

import random
from card import Card
import pygame
from pygame.locals import *
from preloader import load_images
from globals import *

#Eftir: buid er ad hlada inn i deck.images listann, pygame surfaces fyrir gefnar myndir.
def initDeckImg():
    Deck.images = load_images('01d.gif','02d.gif','03d.gif','04d.gif','05d.gif','06d.gif','07d.gif','08d.gif','09d.gif','10d.gif','11d.gif','12d.gif','13d.gif',\
        '01c.gif','02c.gif','03c.gif','04c.gif','05c.gif','06c.gif','07c.gif','08c.gif','09c.gif','10c.gif','11c.gif','12c.gif','13c.gif',\
        '01h.gif','02h.gif','03h.gif','04h.gif','05h.gif','06h.gif','07h.gif','08h.gif','09h.gif','10h.gif','11h.gif','12h.gif','13h.gif',\
        '01s.gif','02s.gif','03s.gif','04s.gif','05s.gif','06s.gif','07s.gif','08s.gif','09s.gif','10s.gif','11s.gif','12s.gif','13s.gif')
    
class Deck(object):
    images = []
    image_count = 0
    def __init__(self):
        self.cards = []
        for suit in range(0,4):
            for rank in range(0,13):
                card = Card(suit,rank, self.images[self.image_count],0,0, type(self)) #init card pos @0,0
                self.add_card(card)
                self.image_count +=1
                
    def __str__(self):
        """Returns the string format for the deck."""
        strDeck = []
        for card in self.cards:
            strDeck.append(str(card))
        return '\n'.join(strDeck)
    
    def __len__(self):
        """Returns the number of cards in the deck."""
        return len(self.cards)
    
    def add_card(self, card):
        """Adds a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card):
        """Removes a card from the deck."""
        self.cards.remove(card)

    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.
        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()
        
    def flip_card(self):
        """Calls the flip function of the top card in the deck."""
        assert len(self.cards) != 0
        self.cards[-1].flip()

#the deck that is dealt from
class dealDeck(Deck):
    def __init__(self,n,parent,x,y):
        self.cards = []
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x-card_width/2 ,self.y-card_height/2, card_width, card_height)
        for i in range(n):
            self.cards.append(parent.pop_card())
            self.cards[i].move_center_to(self.x,self.y)
        self.cards[-1].isTop = True

    def add_card(self, card):
        """Adds a card to the deck."""
        try :
            self.cards[-1].isTop = False
        except:
            print " --> vandamal i ad gera spili TOP i dealDeck"
        self.cards.append(card)
        card.move_center_to(self.x,self.y)
        card.isTop = True
    

#the rows where cards lay                
class rowDeck(Deck):
    def __init__(self,n,parent,x,y):
        self.cards = []
        self.x = x
        self.y = y
        for i in range(n):
            self.cards.append(parent.pop_card()) 
            self.cards[i].move_center_to(self.x,self.y+i*y_offset)
        self.cards[-1].isTop = True

    def canAdd(self, card):
        """True if you can add your selected card to the row."""
        if card.rank == 12 and len(self.cards) == 0 :
            return True
        
        top_suit_fix = self.cards[-1].suit+1
        other_suit_fix = card.suit+1
        top_card_color = top_suit_fix % 2
        other_card_color = other_suit_fix % 2
        
        if (top_card_color != other_card_color) : diffColor = True
        else: diffColor = False
        
        hasOneLessRank = self.cards[-1].rank-1 == card.rank
        
        if diffColor and hasOneLessRank:
            return True
        else:
            return False
        
    def add_card(self, card):
        """Adds a card to the deck."""
        try :
            self.cards[-1].isTop = False
        except:
            pass 
        finally:
            self.cards.append(card)
            card.isTop = True
            card.move_center_to(self.x, (self.y+len(self.cards)*y_offset)-20) #self.y-card.image.get_width()/2+len(self.cards)*(y_offset+10))
    

                        
class colDeck(Deck):
    #image = load_image('shade.gif')
    def __init__(self,n,parent,x,y):
        self.cards = []
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x-card_width/2 ,self.y-card_height/2, card_width, card_height)
        for i in range(n):
            self.cards.append(parent.pop_card())
            self.cards[i].move_center_to(self.x,self.y)
    
    def canAdd(self, card):
        """checks for availability."""
        if card.rank == 0 and len(self.cards) == 0:
            return True
        
        sameSuit = self.cards[-1].suit == card.suit
        nextRank = self.cards[-1].rank+1 == card.rank
        if sameSuit and nextRank:
            return True
        else:
            return False

    def add_card(self, card):
        """Adds a card to the deck."""
        try :
            self.cards[-1].isTop = False
        except:
            print " --> vandamal i ad baeta vid spili i col_cards"
        finally:
            self.cards.append(card)
            card.isTop = True
            card.move_center_to(self.rect.center)
            
            
class handDeck(Deck):
    def __init__(self,x,y):
        self.cards = []
        self.x = x
        self.y = y   
        
    def add_card(self, card):
        """Adds a card to the deck."""
        try:
            self.cards[-1].isTop = False
        except : 
            print " --> vandamal ad gera TOP i hand"
        finally:
            self.cards.append(card)
            card.move_center_to(self.x,self.y)
            card.isTop = True
            card.parent = 'handDeck'
        
def main():
    pygame.init()
    winstyle = 0 #|FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
    initDeckImg()
    
    Master = Deck()
    Master.shuffle()
    
    row_decks = []
    rd_offset = 70
    for i in range(7):
        row_decks.append(rowDeck(i+1,Master, 150+i*rd_offset, 100))
    print row_decks[0].cards[0].parent
        
    col_decks = []
    for i in range(4):
        col_decks.append(colDeck(0,Master, 150+i*rd_offset, 100))  
    
    hand = handDeck(50,50)
    
    deal = dealDeck(len(Master),Master, 0, 0)
         
if  __name__ == "__main__":
    main()

