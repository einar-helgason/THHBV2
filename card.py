
'''
Created on Mar 6, 2014

@author: Tryggvi
'''
class Card(object):
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return '%s of %s' % (self.rank_names[self.rank], self.suit_names[self.suit])
    
    def __cmp__(self, other):
        # the first item of first tuple is compared to the first item of the second tuple.
        #If they are not equal, this is the result of the comparison, else the second item is considered.
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1,t2)

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(0,4):
            for rank in range(0,13):
                card = Card(suit,rank)
                self.cards.append(card)
                
    def __str__(self):
        strDeck = []
        for card in self.cards:
            strDeck.append(str(card))
        return '\n'.join(strDeck)
    
a = Deck()
print a
                