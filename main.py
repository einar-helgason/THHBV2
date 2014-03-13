'''
Created on Mar 7, 2014

@author: Tryggvi
'''
import pygame
from pygame.locals import *
from globals import *
from preloader import *
import card
import updateManager
import deck
import sys
from handleMouse import *

def main():
    pygame.init()
    winstyle = 0 #|FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
    pygame.display.set_caption("Kapall!")
    c = pygame.time.Clock()
    
    all = pygame.sprite.RenderUpdates() #ONOTAD
    
    #INIT BACKGROUND
    background = load_image('background.png')
    screen.blit(background, (0, 0))
    
    deck.initDeckImg()

    #init decks.
    master = deck.Deck()
    master.shuffle()
    
    row_decks = []
    offset = 70
    for i in range(7):
        row_decks.append(deck.rowDeck(i+1,master, 150+i*offset, 180))
    col_decks = []
    for i in range(4):
        col_decks.append(deck.colDeck(0,master, 250+i*offset, 50))  
    
    hand = deck.handDeck(50+offset,50)
    
    deal = deck.dealDeck(len(master),master, 50, 50)
    #deal.flip_card()
    
    cardSprites = pygame.sprite.LayeredUpdates()
    cardPos = []
    ########## Add To cardSprites and cardlist
    for i in range(len(row_decks)):
        cardSprites.add(row_decks[i].cards)
        for card in row_decks[i].cards: cardPos.append(card)
    for i in range(len(col_decks)):
        cardSprites.add(col_decks[i].cards)
        for card in col_decks[i].cards: cardPos.append(card)
    cardSprites.add(hand.cards)
    for card in hand.cards : cardPos.append(card)
    cardSprites.add(deal.cards)
    for card in deal.cards : cardPos.append(card)
    ###########
    
    
    going = True
    while going :
        
        is_left_mouse_down = pygame.mouse.get_pressed()[0]
        is_mouse_moving = False
        
        for e in pygame.event.get():
            if e.type == QUIT:
                going = False
                break
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    going = False
                    break
            if e.type == MOUSEMOTION :
                is_mouse_moving = True
            else : is_mouse_moving = False
            
            if e.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for card in cardPos :
                    if card.rect.collidepoint(pos) and card.hidden :
                        if card.parent == 'dealDeck' :
                            if deal.cards[-1] == card :
                                hand.add_card(deal.pop_card())
                                cardSprites.move_to_front(card) # laetur spilid teiknast fremst
                                card.flip()
                        if card.isTop : card.flip()


        #Check if move card
        if is_left_mouse_down and is_mouse_moving :
            cardSprites.update()
            
        cardSprites.clear(screen, background)
        cardSprites.draw(screen) #notar image og rect af sprite til ad teikna.
        
            
        pygame.display.update() # update the display
        c.tick(60) #60fps
    
    pygame.quit()
    sys.exit()

        
        
if __name__ == '__main__': 
    main()

    
