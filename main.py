'''
Created on Mar 7, 2014

@author: Tryggvi update
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
    curr_card = None
    
    #INIT BACKGROUND
    background = load_image('background.png')
    screen.blit(background, (0, 0))

    no_card_img = load_image('shade.gif')
    no_card_img_halfwidth = no_card_img.get_width()/2 
    no_card_img_halfheight = no_card_img.get_height()/2
    
    deck.initDeckImg()

    #init decks.
    master = deck.Deck()
    master.shuffle()
    
    row_decks = []
    for i in range(7):
        row_decks.append(deck.rowDeck(i+1,master, 150+i*y_offset, 180))
    col_decks = []
    for i in range(4):
        col_decks.append(deck.colDeck(0,master, 250+i*y_offset, 50))  
    
    hand = deck.handDeck(50+y_offset,50)
    
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
            screen.blit(no_card_img, (col_decks[i].x-no_card_img_halfwidth, col_decks[i].y-no_card_img_halfheight))
            
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
                
            if e.type != MOUSEMOTION:
                if e.type == MOUSEBUTTONDOWN:
                    down_pos = pygame.mouse.get_pos() #save pos of down-click
                    card_old_x = 0#so card can jump back
                    card_old_y = 0
                    card_parent_obj = None
                    for card in cardPos:
                        if card.rect.collidepoint(down_pos) and card.isTop and not card.hidden: #LAGA MED TOP
                            card_old_x = card.rect.center[0] #sma hax, tekur x og y gildin ur midju spilsinns.
                            card_old_y = card.rect.center[1]
                            curr_card = card
                            if card in hand.cards: card_parent_obj = hand #!!!!!!!!!!
                            print curr_card
                    print down_pos
                if e.type == MOUSEBUTTONUP:
                    up_pos = pygame.mouse.get_pos()
                    for card in cardPos:
                        if card.rect.collidepoint(up_pos):
                            #TO-DO tjekka hvort curr_card ma fara thangad
                            for i in range(len(col_decks)):
                                if card.parent == 'rowDeck%d' %i:
                                    if row_decks[i].canAdd(curr_card) :
                                        row_decks[0].add(curr_card)
                                    
                            else: 
                                try: curr_card.move_center_to(card_old_x, card_old_y)
                                except: "ekkert curr_card"
                        
                    curr_card = None 
                    print up_pos
                    
            if e.type == MOUSEMOTION :
                is_mouse_moving = True
                """LAGA THETTA"""
                try: 
                    curr_card.update()
                    cardSprites.move_to_front(curr_card)
                except: pass #print "ekkert curr_card"
                """****************"""
            else : is_mouse_moving = False
            
            """MOUSEDOWN""" #laga, finna ut hvernig ma save-a klikk. Get kanski latid spil halda utan um original pos.
            if is_left_mouse_down:
                 pass
            """MOUSEUP"""
            if e.type == MOUSEBUTTONUP:
                up_pos = pygame.mouse.get_pos()
                for card in cardPos :
                    """CLICK IS ON A HIDDEN TOP CARD"""
                    if card.rect.collidepoint(up_pos) and card.hidden :
                        if card.isTop : 
                            card.flip()
                        """CLICK IS ON DEALDECK"""
                        if card.parent == 'dealDeck' :
                            if deal.cards[-1] == card :
                                hand.add_card(deal.pop_card())
                                cardSprites.move_to_front(card) # laetur spilid teiknast fremst
                                card.flip()
                        

        
        cardSprites.clear(screen, background)
        #cardSprites.update()
        cardSprites.draw(screen) #notar image og rect af sprite til ad teikna.
        
            
        pygame.display.update() # update the display
        c.tick(60) #60fps
    
    pygame.quit()
    sys.exit()

        
        
if __name__ == '__main__': 
    main()

    
