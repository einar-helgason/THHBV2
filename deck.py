'''
Created on Mar 7, 2014

@author: Tryggvi
'''

import random
from card import Card

class Deck(object):
    images = []
    
    image_count = 0
    def __init__(self):
        self.cards = []
        
        for suit in range(0,4):
            for rank in range(0,13):
                card = Card(suit,rank, self.images[self.image_count],0,0)
                self.cards.append(card)
                self.image_count +=1
                
    def __str__(self):
        strDeck = []
        for card in self.cards:
            strDeck.append(str(card))
        return '\n'.join(strDeck)
    
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
    

