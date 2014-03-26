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

class test_preloads(unittest.TestCase):
    def test_load_image(self):
        tester = preloader.load_image('01s.gif')
        self.assertIsInstance(tester, pygame.Surface)
        
    def test_load_images(self):
        tester = preloader.load_images('01c.gif','02c.gif','03c.gif','04c.gif','05c.gif','06c.gif','07c.gif','08c.gif','09c.gif','10c.gif')
        self.assertIsInstance(tester, list)
        for i in tester:
            self.assertIsInstance(i, pygame.Surface)

class test_card(unittest.TestCase):
    
    def setUp(self): 
        self.picture = preloader.load_image('01s.gif')
        self.tester = card.Card(3,0, self.picture, 0, 0, 'test-parent')
        
    def test_card_creation(self):
        self.assertEqual(self.tester.suit, 3)
        self.assertEqual(self.tester.rank, 0)
        self.assertEqual(self.tester.front, self.picture)
        self.assertEqual(self.tester.back, self.tester.image)
        self.assertIsInstance(self.tester.rect, pygame.Rect)
        self.assertEqual(self.tester.x, 0)
        self.assertEqual(self.tester.y, 0)
        self.assertTrue(self.tester.hidden)
        self.assertEqual(self.tester.parent, 'test-parent')
        self.assertFalse(self.tester.isTop)
        self.assertTupleEqual(self.tester.rect.center, (self.tester.x, self.tester.y))
        
    def test_card_str(self):
        self.assertEqual( 'Ace of Spades', str(self.tester) )
        self.tester2 = card.Card(2, 1, self.picture, 0, 0, 'test-parent')
        self.assertNotEqual(str(self.tester2), str(self.tester))
        self.assertNotEqual( 'foobar', str(self.tester))
        
    def test_card_flip(self):
        self.tester.flip()
        self.assertEqual(self.tester.image, self.tester.front)
        self.assertFalse(self.tester.hidden)
        
    def test_card_move_center_to(self):
        #two floats input
        self.tester.move_center_to(50, 50)
        self.assertTupleEqual(self.tester.rect.center, (50,50))
        #tuple input
        self.tester.move_center_to((40, 40))
        self.assertTupleEqual(self.tester.rect.center, (40,40))
        

class test_deck(unittest.TestCase):
    
    def setUp(self):
        deck.initDeckImg()
        self.tester = deck.Deck()
        picture = preloader.load_image('01s.gif')
        self.testCard = card.Card(3, 0, picture, 0, 0, 'test-parent')
        
    def test_deck_creation(self):
        self.assertEqual(self.tester.image_count, 52)
        self.assertEqual(len(self.tester.cards), 52)
        self.assertIsInstance(self.tester.cards[0], card.Card)
    
    def test_deck_len(self):
        self.assertEqual(len(self.tester), 52)
    
    def test_deck_str(self):
        self.assertIsInstance(str(self.tester), str)
        
    def test_deck_add_card(self):
        picture = preloader.load_image('01s.gif')
        testCard = card.Card(3, 0, picture, 0, 0, 'test-parent')
        self.assertEqual(len(self.tester), 52)
        self.tester.add_card(testCard)
        self.assertEqual(len(self.tester), 53)
        
    def test_deck_remove_card(self):
        self.assertEqual(len(self.tester), 52)
        self.tester.add_card(self.testCard)
        self.tester.remove_card(self.testCard)
        self.assertEqual(len(self.tester), 52)
        
    def test_deck_pop_card(self):
        self.tester.pop_card()
        self.assertEqual(len(self.tester), 51)

    def test_deck_shuffle(self):
        temp = self.tester.cards[0]
        self.tester.shuffle()
        self.assertNotEqual(self.tester.cards[0], temp, "1/52 likur a a thetta klikki!")
        
    def test_deck_sort(self):
        self.tester.sort()
        self.assertEqual(str(self.tester.cards[0]), 'Ace of Clubs')
        self.assertEqual(str(self.tester.cards[1]), '2 of Clubs')
        #...
        self.assertEqual(str(self.tester.cards[-1]), 'King of Spades')
    
    def test_deck_flip_card(self):
        self.tester.flip_card()
        self.assertEqual(self.tester.cards[-1].image, self.tester.cards[-1].front)
        self.assertFalse(self.tester.cards[-1].hidden)
        

class test_dealDeck(unittest.TestCase):
    def setUp(self):
        deck.initDeckImg()
        self.master = deck.Deck()
        self.tester = deck.dealDeck(10, self.master, 30, 30)
        picture = preloader.load_image('01s.gif')
        self.testCard = card.Card(3, 0, picture, 0, 0, 'test-parent')
    
    def test_dealDeck_creation(self):
        for i in range(len(self.tester.cards)):
            self.assertEqual(self.tester.x, 30)
            self.assertEqual(self.tester.y, 30)
            self.assertEqual(self.tester.cards[i].parent, 'dealDeck')
        self.assertTrue(self.tester.cards[-1].isTop)
        
    def test_dealDeck_add_card(self):
        self.tester.add_card(self.testCard)
        self.assertFalse(self.tester.cards[-2].isTop)
        self.assertTrue(self.tester.cards[-1].isTop)
        self.assertEqual(len(self.tester.cards) , 11)
        self.assertIsInstance(self.tester.cards[-1], card.Card)
        self.assertTupleEqual((self.tester.x, self.tester.y), self.testCard.rect.center)
        self.assertTrue(self.testCard.isTop)
        
class test_rowDeck(unittest.TestCase):
    def setUp(self):
        deck.initDeckImg()
        self.master = deck.Deck()
        self.tester = deck.rowDeck(4, self.master, 30, 30)
        picture = preloader.load_image('01s.gif')
        self.testCard = card.Card(3, 0, picture, 0, 0, 'test-parent')
        
    def test_rowDeck_creation(self):
        self.assertEqual(len(self.master.cards), 52-4)
        self.assertEqual(len(self.tester.cards), 4)
        for i in range(4):
            self.assertTupleEqual(self.tester.cards[i].rect.center, (self.tester.x,self.tester.y+i*self.tester.offset))
            self.assertEqual(self.tester.cards[i].parent, 'rowDeck%d' % i)
            
    def test_rowDeck_canAdd(self):
        """virkar thetta fall einar?"""
        pass
    
    def test_rowDeck_can_add(self):
        """a eftir ad utfaera"""
        pass

class test_colDeck(unittest.TestCase):
    def setUp(self):
        deck.initDeckImg()
        self.master = deck.Deck()
        self.tester = deck.colDeck(4, self.master, 30, 30)
        picture = preloader.load_image('01s.gif')
        self.testCard = card.Card(3, 0, picture, 0, 0, 'test-parent')
        
    def test_colDeck_creation(self):
        self.assertEqual(len(self.tester.cards), 4)
        for i in range(4):
            self.assertTupleEqual(self.tester.cards[i].rect.center, (self.tester.x,self.tester.y))
            self.assertEqual(self.tester.cards[i].parent, 'colDeck%d' % i)
    
    def test_colDeck_addCard(self):
        """virkar thetta falll einar?"""
        pass
    
    
class test_handDeck(unittest.TestCase):
    def setUp(self):
        self.tester = deck.handDeck(30, 30)
        picture = preloader.load_image('01s.gif')
        self.testCard = card.Card(3, 0, picture, 0, 0, 'test-parent')
    
    def test_handDeck_creation(self):
        self.assertEqual(self.tester.x, 30)
        self.assertEqual(self.tester.y, 30)
        self.assertEqual(len(self.tester.cards), 0)
        
    def test_handDeck_add_card(self):
        self.tester.add_card(self.testCard)
        self.assertEqual(len(self.tester.cards), 1)
        self.assertListEqual(self.tester.cards, [self.testCard])
        self.assertTupleEqual(self.tester.cards[-1].rect.center, (self.tester.x,self.tester.y))
        self.assertTrue(self.testCard.isTop)
        self.assertEqual(self.testCard.parent, 'handDeck')
        
            
        
        
def main():
    pygame.init()
    winstyle = 0 #|FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
    unittest.main(exit=False)    
    pygame.quit()
    

if __name__ == '__main__':
    main()
