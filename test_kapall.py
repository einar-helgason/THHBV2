'''
Created on Mar 19, 2014

@author: Tryggvi
'''
import pygame
from pygame.locals import *
from globals import *

import unittest
import card
import deck
import preloader

class test_card(unittest.TestCase):
    
    def setUp(self):
        self.picture = preloader.load_image('01s.gif')
        self.tester = card.Card('Spades','Ace', self.picture, 0, 0, 'test-parent')

    def test_card_creation(self):
        pass
        
    def test_card_str(self):
        self.assertEqual('Ace of Spades', str(self.tester))
        self.assertNotEqual('2 of Hearts', str(self.tester))
        self.assertNotEqual('foobar', str(self.tester))
        
    def test_card_flip(self):
        self.tester.flip()
        self.assertEqual(self.tester.image, self.tester.front)
        self.assertFalse(self.tester.hidden)
        
    def test_card_move_center_to(self):
        self.tester.move_center_to(50, 50)
        self.assertEqual(self.tester.rect.center, (50,50))
        

class test_deck(unittest.TestCase):
    
    def setUp(self):
        self.tester = deck.Deck()
        
    def test_deck_creation(self):
        pass
    
    def test_deck_len(self):
        self.assertEqual(len(self.tester), 52)
    
    def test_deck_str(self):
        self.assertIsInstance(str(self.tester), list)
        
    def test_deck_add_card(self):
        picture = preloader.load_image('01s.gif')
        testCard = card.Card('Spades','Ace', picture, 0, 0, 'test-parent')
        testDeck = deck.Deck()
        testDeck.add_card(testCard)
        self.assertEqual(len(testDeck), 53)
        
    
        
        
    





if __name__ == '__main__':
    pygame.init()
    winstyle = 0 #|FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
    
    unittest.main(exit=False)