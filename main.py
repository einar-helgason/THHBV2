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
from sounds import *
from textonscreen import*

def main():
    pygame.init()
    winstyle = 0 #|FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
    pygame.display.set_caption("Kapall!")
    c = pygame.time.Clock()
    
    curr_cards_list = []
    
    background = load_image('background2.jpg') #INIT BACKGROUND
    background = pygame.transform.scale(background, SCREENRECT.size)
    screen.blit(background, (0, 0))

    no_card_img = load_image('shade_night.png')
    
    deck.initDeckImg()
    #draw on screen
    drawText(screen,"ESC to exit!",400,400)
    drawScore(screen,10)
    
    #load sound effects
    mute_sound = False
    mouseClick_sound = load_sound('Lamb.wav')
    colDeck_sound = load_sound('1-up.wav')
    flip_sound = load_sound('page-flip-02.wav')
    winning_sound = load_sound('tribWin.wav')
    if pygame.mixer:
        music = os.path.join(main_dir, 'data/sounds', 'naturesounds.ogg')
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)
    
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
            """Event Keydown - m to mute"""
            if e.type == KEYDOWN:
                if e.key == K_m:
                    mute_sound = not mute_sound
                    if mute_sound:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                
            """EVENT MOUSE IS STILL"""    
            if e.type != MOUSEMOTION:
                """EVENT MOUSE BUTTON DOWN"""
                if e.type == MOUSEBUTTONDOWN:
                    #if (not mute_sound):
                        #mouseClick_sound.play()
                    down_pos = pygame.mouse.get_pos() #save pos of down-click
                    card_old_x = 0 #so card can jump back to old pos
                    card_old_y = 0
                    """finna hvada spil eg held a og hvad er foreldri thess"""
                    
                    """SEARCH FOR curr_cards IN ROW DECKS"""
                    for i in range(len(row_decks)):
                        for card in row_decks[i].cards:
                            #"ATH: HER ERU MORG SPIL TEKIN UPP!"
                            if card.AOE.collidepoint(down_pos) and not card.hidden:
                                card_old_x = card.rect.center[0] 
                                card_old_y = card.rect.center[1]
                                curr_cards_parent = row_decks[i]
                                
                                index = row_decks[i].cards.index(card)
                                #index - efstu spil i rodinni eru sett i curr_cards_list
                                curr_cards_list = row_decks[i].cards[index:]
                                

                            #"EITT SPIL TEKId UPP."
                            elif card.rect.collidepoint(down_pos) and card.isTop and not card.hidden:
                                card_old_x = card.rect.center[0] 
                                card_old_y = card.rect.center[1]
                                curr_cards_list.append(card)
                                curr_cards_parent = row_decks[i]

                    """SEARCH FOR curr_cards IN COLLECTION DECKS"""            
                    for i in range(len(col_decks)):
                        for card in col_decks[i].cards:
                            if card.rect.collidepoint(down_pos) and card.isTop and not card.hidden:
                                card_old_x = card.rect.center[0] #sma hax, tekur x og y gildin ur midju spilsinns.
                                card_old_y = card.rect.center[1]
                                curr_cards_list.append(card)
                                curr_cards_parent = col_decks[i]
                    """SEARCH FOR curr_cards IN HAND DECK"""
                    for card in hand.cards:
                            if card.rect.collidepoint(down_pos) and card.isTop and not card.hidden:
                                card_old_x = card.rect.center[0] #sma hax, tekur x og y gildin ur midju spilsinns.
                                card_old_y = card.rect.center[1]
                                curr_cards_list.append(card)
                                curr_cards_parent = hand
                    
                """EVENT MOUSE BUTTON UP"""  #this is inside event mouse is still.  
                if e.type == MOUSEBUTTONUP:
                    up_pos = pygame.mouse.get_pos()
                    
                    "TRY TO APPEND curr_cards TO ROW DECKS"  
                    try:                                    
                        for i in range(len(row_decks)):
                            "IF EMPTY ROW, CHECK FOR KING CARD"
                            if(len(row_decks[i].cards) == 0):
                                if(row_decks[i].rect.collidepoint(up_pos)):
                                    if row_decks[i].canAdd(curr_cards_list[0]):
                                        temp = []
                                        n = len(curr_cards_list) 
                                        for a in range(n):
                                            temp.append(curr_cards_parent.pop_card())  
                                        try: 
                                            curr_cards_parent.cards[-1].isTop = True
                                            row_decks[i].cards[-1].isTop = False
                                        except Exception, error: print " --> BUG!!"
                                        
                                        for b in range(n):
                                            row_decks[i].add_card(temp.pop())
                                        curr_cards_list = []
                            
                            for card in row_decks[i].cards:
                                "Click is on top card"
                                if card.rect.collidepoint(up_pos) and card.isTop and not card.hidden:
                                    if row_decks[i].canAdd(curr_cards_list[0]) :
                                        temp = []
                                        n = len(curr_cards_list) 
                                        for a in range(n):
                                            temp.append(curr_cards_parent.pop_card())  
                                        try: 
                                            curr_cards_parent.cards[-1].isTop = True
                                            row_decks[i].cards[-1].isTop = False
                                        except Exception, error: print " --> BUG!!"
                                        
                                        for b in range(n):
                                            row_decks[i].add_card(temp.pop())
                                        curr_cards_list = []

                    except IndexError:  pass
                                  
                    "TRY TO APPEND curr_cards TO COL DECKS"  
                    try:
                        col_deck_sum = 0
                        for i in range(len(col_decks)):
                            if col_decks[i].rect.collidepoint(up_pos):
                                if col_decks[i].canAdd(curr_cards_list[0]) :
                                    col_decks[i].add_card(curr_cards_parent.pop_card()) #var med curr_cards inni i pop_card
                                    try: curr_cards_parent.cards[-1].isTop = True #Laetir spilid undir verda TOP
                                    except IndexError: pass
                                    curr_cards_list = []
                                    if (not mute_sound):
                                        colDeck_sound.play()
                            col_deck_sum = col_deck_sum + len(col_decks[i])
                        """WINNER IF HAPPENDS"""
                        if col_deck_sum == 52:
                            winning_sound.play()

                    except IndexError: pass
                        
                    "MOVE curr_cards TO OLD POSITION"  
                    for i in range(len(curr_cards_list)): 
                        curr_cards_list[i].move_center_to(card_old_x, card_old_y+i*y_offset)

                              
                    curr_cards_list = [] #last thing to do after a mouse up event is to release the curr_cards.
            
            """EVENT MOUSE IS MOVING"""        
            if e.type == MOUSEMOTION :
                for i in range(len(curr_cards_list)):
                    curr_cards_list[i].update(i)
                    cardSprites.move_to_front(curr_cards_list[i])
                            
            
            
            """EVENT MOUSEUP""" #this is the rest of the mouseup event AFTER curr_cards stuff has been executed.
            if e.type == MOUSEBUTTONUP:
                up_pos = pygame.mouse.get_pos()
                for card in cardPos :
                    """CLICK IS ON A HIDDEN TOP CARD"""
                    if card.rect.collidepoint(up_pos) and card.hidden :
                        if card.isTop : 
                            card.flip()
                            if not mute_sound:
                                flip_sound.play()
                """CLICK IS ON DEALDECK"""
                if deal.rect.collidepoint(up_pos):
                    if len(deal.cards) == 0:
                        for i in range(len(hand.cards)):
                            hand.cards[-1].isTop = False #til oryggis
                            deal.add_card(hand.pop_card())
                            try: deal.cards[-1].flip_back()
                            except IndexError: pass
                        try: deal.cards[-1].isTop = True
                        except IndexError: pass
                    else: 
                        hand.add_card(deal.pop_card())
                        cardSprites.move_to_front(hand.cards[-1]) # laetur spilid teiknast fremst
                        hand.cards[-1].flip()
                        if not mute_sound:
                            flip_sound.play()


        
        cardSprites.clear(screen, background)
        cardSprites.draw(screen) #notar image og rect af sprite til ad teikna.
        
            
        pygame.display.update() # update the display
        c.tick(60) #60fps
    
    pygame.quit()
    sys.exit()

        
        
if __name__ == '__main__': 
    main()

    
