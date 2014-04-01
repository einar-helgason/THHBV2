'''
Created on Mar 7, 2014

@author: Tryggvi update
'''
import pygame
from pygame.locals import *
from globals import *
from preloader import load_image
import card
import deck
import sys

def main():
    pygame.init()
    winstyle = 0 #|FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
    pygame.display.set_caption("Kapall!")
    c = pygame.time.Clock()
    
    curr_card = None
    
    background = load_image('background2.jpg') #INIT BACKGROUND
    background = pygame.transform.scale(background, SCREENRECT.size)
    screen.blit(background, (0, 0))

    no_card_img = load_image('shade_night.png')
    
    deck.initDeckImg()

    #init decks.
    master = deck.Deck()
    master.shuffle()
    
    row_decks = []
    for i in range(7):
        row_decks.append(deck.rowDeck(i+1,master, 150+i*x_offset, 180))
    col_decks = []
    for i in range(4):
        col_decks.append(deck.colDeck(0,master, 360+i*x_offset, 53))  
    
    hand = deck.handDeck(50+x_offset,50)
    
    deal = deck.dealDeck(len(master),master, 50, 50)
    

    cardSprites = pygame.sprite.LayeredUpdates() #Layered sprite group. Used to draw and update the card sprites.
    cardPos = [] #list to iter all cards to check for "collision" with mouse
    """ Add all cards to cardSprites and cardPos """
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
        """Draw the bottom of all the collection decks, if they are empty this shows."""
        for i in range(4):
            screen.blit(no_card_img, (col_decks[i].x-card_width/2, col_decks[i].y-card_height/2))
        
        for e in pygame.event.get():
            """EVENT QUIT"""
            if e.type == QUIT:
                going = False
                break
            """EVENT KEYDOWN - ESCAPE KEY"""
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    going = False
                    break
            """EVENT MOUSE IS STILL"""    
            if e.type != MOUSEMOTION:
                """EVENT MOUSE BUTTON DOWN"""
                if e.type == MOUSEBUTTONDOWN:
                    down_pos = pygame.mouse.get_pos() #save pos of down-click
                    card_old_x = 0 #so card can jump back to old pos
                    card_old_y = 0
                    """finna hvada spil eg held a og hvad er foreldri thess"""
                    
                    """SEARCH FOR CURR_CARD IN ROW DECKS"""
                    for i in range(len(row_decks)):
                        for card in row_decks[i].cards:
                            if card.rect.collidepoint(down_pos) and card.isTop and not card.hidden:
                                card_old_x = card.rect.center[0] #sma hax, tekur x og y gildin ur midju spilsinns.
                                card_old_y = card.rect.center[1]
                                curr_card = card
                                curr_card_parent = row_decks[i]
                    """SEARCH FOR CURR_CARD IN COLLECTION DECKS"""            
                    for i in range(len(col_decks)):
                        for card in col_decks[i].cards:
                            if card.rect.collidepoint(down_pos) and card.isTop and not card.hidden:
                                card_old_x = card.rect.center[0] #sma hax, tekur x og y gildin ur midju spilsinns.
                                card_old_y = card.rect.center[1]
                                curr_card = card
                                curr_card_parent = col_decks[i]
                    """SEARCH FOR CURR_CARD IN HAND DECK"""
                    for card in hand.cards:
                            if card.rect.collidepoint(down_pos) and card.isTop and not card.hidden:
                                card_old_x = card.rect.center[0] #sma hax, tekur x og y gildin ur midju spilsinns.
                                card_old_y = card.rect.center[1]
                                curr_card = card
                                curr_card_parent = hand
                    
                """EVENT MOUSE BUTTON UP"""  #this is inside event mouse is still.  
                if e.type == MOUSEBUTTONUP:
                    up_pos = pygame.mouse.get_pos()
                    
                    "TRY TO APPEND CURR_CARD TO ROW DECKS"  
                    try:                                    
                        for i in range(len(row_decks)):
                            "IF EMPTY ROW, CHECK FOR KING CARD"
                            if(len(row_decks[i].cards) == 0):
                                if(row_decks[i].rect.collidepoint(up_pos)):
                                    if row_decks[i].canAdd(curr_card):
                                        row_decks[i].add_card(curr_card_parent.pop_card())
                                        try: curr_card_parent.cards[-1].isTop = True
                                        except: pass
                                        curr_card = None
                                        
                            for card in row_decks[i].cards:
                                if card.rect.collidepoint(up_pos) and card.isTop and not card.hidden:
                                    if row_decks[i].canAdd(curr_card) :
                                        row_decks[i].add_card(curr_card_parent.pop_card())
                                        try: curr_card_parent.cards[-1].isTop = True #Laetir spilid undir verda TOP
                                        except: print " --> vandamal i row_drcks ad lata card verda TOP"
                                        curr_card = None 
                    except Exception, error:  
                        print error
                        print " --> vandamal i row_decks" 
                                  
                    "TRY TO APPEND CURR_CARD TO COL DECKS"  
                    try:
                        for i in range(len(col_decks)):
                            if col_decks[i].rect.collidepoint(up_pos):
                                if col_decks[i].canAdd(curr_card) :
                                    col_decks[i].add_card(curr_card_parent.pop_card()) #var med curr_card inni i pop_card
                                    try: curr_card_parent.cards[-1].isTop = True #Laetir spilid undir verda TOP
                                    except: print " --> vandamal i col_drcks ad lata card verda TOP"
                                    curr_card = None 
                    except Exception, error:  
                        print error
                        print " --> vandamal i col_decks"
                        
                    "TRY TO MOVE CURR_CARD TO OLD POSITION"  
                    try: curr_card.move_center_to(card_old_x, card_old_y)
                    except Exception, error:  
                        pass #ekkert curr_card
                              
                    curr_card = None #last thing to do after a mouse up event is to release the curr_card.
            
            """EVENT MOUSE IS MOVING"""        
            if e.type == MOUSEMOTION :
                try: 
                    curr_card.update()
                    cardSprites.move_to_front(curr_card)
                except: pass #ekkert curr_card
            
            
            """EVENT MOUSEUP""" #this is the rest of the mouseup event AFTER curr_card stuff has been executed.
            if e.type == MOUSEBUTTONUP:
                up_pos = pygame.mouse.get_pos()
                for card in cardPos :
                    """CLICK IS ON A HIDDEN TOP CARD"""
                    if card.rect.collidepoint(up_pos) and card.hidden :
                        if card.isTop : 
                            card.flip()
                """CLICK IS ON DEALDECK"""
                if deal.rect.collidepoint(up_pos):
                    if len(deal.cards) == 0:
                        for i in range(len(hand.cards)):
                            hand.cards[-1].isTop = False #til oryggis
                            deal.add_card(hand.pop_card())
                            try: deal.cards[-1].flip_back()
                            except: " --> vandamal i flippa spili i dealDeck, lyklegast thvi hann er tomur"
                        deal.cards[-1].isTop = True
                    else: 
                        hand.add_card(deal.pop_card())
                        cardSprites.move_to_front(hand.cards[-1]) # laetur spilid teiknast fremst
                        hand.cards[-1].flip()


        
        cardSprites.clear(screen, background)
        cardSprites.draw(screen) #notar image og rect af sprite til ad teikna.
        
            
        pygame.display.update() # update the display
        c.tick(60) #60fps
    
    pygame.quit()
    sys.exit()

        
        
if __name__ == '__main__': 
    main()

    
