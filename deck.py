'''
Created on Mar 7, 2014

@author: Tryggvi
'''

import random
from card import Card
from pygame.locals import *
from preloader import *
x_offset = 20

def initDeckImg():
    Deck.images = load_images('01c.gif','02c.gif','03c.gif','04c.gif','05c.gif','06c.gif','07c.gif','08c.gif','09c.gif','10c.gif','11c.gif','12c.gif','13c.gif',\
        '01d.gif','02d.gif','03d.gif','04d.gif','05d.gif','06d.gif','07d.gif','08d.gif','09d.gif','10d.gif','11d.gif','12d.gif','13d.gif',\
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
        strDeck = []
        for card in self.cards:
            strDeck.append(str(card))
        return '\n'.join(strDeck)
    
    def __len__(self):
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
        self.cards[-1].flip()

#the deck that is dealt from
class dealDeck(Deck):
    def __init__(self,n,parent,x,y):
        self.cards = []
        self.x = x
        self.y = y
        for i in range(n):
            self.cards.append(parent.pop_card())
            self.cards[i].move_center_to(self.x,self.y)
            self.cards[i].parent = 'dealDeck'
        self.cards[-1].isTop = True

    def add_card(self, card):
        """Adds a card to the deck."""
        try :
            self.cards[-1].isTop = False
            self.cards.append(card)
            card.move_center_to(self.x,self.y)
            card.isTop = True
        except:
            pass
    

#the rows where cards lay                
class rowDeck(Deck):
    def __init__(self,n,parent,x,y):
        self.cards = []
        self.x = x
        self.y = y
        self.offset = 20
        for i in range(n):
            self.cards.append(parent.pop_card()) 
            self.cards[i].move_center_to(self.x,self.y+i*self.offset)
            self.cards[i].parent = 'rowDeck%d' % i
        self.cards[-1].isTop = True

    def canAdd(self, card):
        """True if you can add your selected card to the row."""
        isBlack  = self.suitOf_cardOnTop % 2 == 0
        isRed = self.suitOf_cardOnTop % 2 == 1
        hasOneLessRank = self.rankOf_cardOnTop == card.rank+1
        if isBlack and card.suit % 2 == 1 and hasOneLessRank:
            return True
        if isRed and card.suit % 2 == 0 and hasOneLessRank:
            return True
        else:
            return False
        
        def add_card(self, card):
            """Adds a card to the deck."""
            try :
                self.cards[-1].isTop = False
                self.cards.append(card)
                card.move_center_to(self.x,self.y)
                card.isTop = True
            except:
                pass
    

                        
class colDeck(Deck):
    #image = load_image('shade.gif')
    def __init__(self,n,parent,x,y):
        self.cards = []
        self.x = x
        self.y = y
        for i in range(n): #fer aldrei inni thvi n er 0 i byrjun
            self.cards.append(parent.pop_card())
            self.cards[i].move_center_to(self.x,self.y)
            self.cards[i].parent = 'colDeck%d' % i
            print self.cards[i].parent
    
    def canAdd(self, card):
        """cecks for availability."""
        if card.rank == 0 and not self.cards:
            return True
        sameSuit = self.suitOf_cardOnTop == card.suit
        nextRank = self.rankOf_cardOnTop == card.rank-1
        if sameSuit and nextRank:
            return True
        else:
            return False
    
            
            
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
            pass
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
    Master.sort()
    
    row_decks = []
    rd_offset = 70
    for i in range(7):
        row_decks.append(rowDeck(i+1,Master, 150+i*rd_offset, 100))
        
    col_decks = []
    for i in range(4):
        col_decks.append(colDeck(0,Master, 150+i*rd_offset, 100))  
    
    hand = handDeck(50,50)
    
    deal = dealDeck(len(Master),Master, 0, 0)
    #deal.flip_card()
    
        
    
    
if  __name__ == "__main__":
    main()

