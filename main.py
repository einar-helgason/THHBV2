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
    pygame.display.set_caption("Mouse Focus Workout")
    c = pygame.time.Clock()
    
    all = pygame.sprite.RenderUpdates() #ONOTAD
    
    #INIT BACKGROUND
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    deck.initDeckImg()
    
    #prufa
    masterDeck = deck.Deck()
    myCard = masterDeck.cards[0]
    
    cardSprite = pygame.sprite.Group(myCard)
    screen.blit(myCard.image,(myCard.x,myCard.y)) #TO-DO, LAGA OG HAFA UPDATE MANAGER
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
        #globals.checkEvents()


        cardSprite.clear(screen, background)
        cardSprite.draw(screen)
        
        #Check if move card
        if is_left_mouse_down and is_mouse_moving :
            cardSprite.update()
            
        #updateManager.update(screen) #OVIRKUR
        pygame.display.update() # update the display
        c.tick(60) #60fps
    
    pygame.quit()
    sys.exit()

        
        
if __name__ == '__main__': 
    main()

    
