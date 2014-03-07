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

def main():
    pygame.init()
    winstyle = 0 #|FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
    
    pygame.display.set_caption("Mouse Focus Workout")
    c = pygame.time.Clock()
    
    all = pygame.sprite.RenderUpdates() #ONOTAD
    
    deck.Deck.images = load_images('01c.gif','02c.gif','03c.gif','04c.gif','05c.gif','06c.gif','07c.gif','08c.gif','09c.gif','10c.gif','11c.gif','12c.gif','13c.gif',\
        '01d.gif','02d.gif','03d.gif','04d.gif','05d.gif','06d.gif','07d.gif','08d.gif','09d.gif','10d.gif','11d.gif','12d.gif','13d.gif',\
        '01h.gif','02h.gif','03h.gif','04h.gif','05h.gif','06h.gif','07h.gif','08h.gif','09h.gif','10h.gif','11h.gif','12h.gif','13h.gif',\
        '01s.gif','02s.gif','03s.gif','04s.gif','05s.gif','06s.gif','07s.gif','08s.gif','09s.gif','10s.gif','11s.gif','12s.gif','13s.gif')
    
    #prufa
    myDeck = deck.Deck()
    myCard = myDeck.cards[0]
    
    ###########
    
    going = True
    while going :
        mx,my = pygame.mouse.get_pos() #TAKA UT 
        mouse_left_down = pygame.mouse.get_pressed()[0] #TAKA UT UR MAIN
        
        for e in pygame.event.get():
            if e.type == QUIT:
                going = False
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    going = False
        if mouse_left_down : 
            myCard.x = mx
            myCard.y = my
            
        screen.blit(myCard.image,(myCard.x,myCard.y)) #TO-DO, LAGA OG HAFA UPDATE MANAGER
        
        updateManager.update(screen) #OVIRKUR
        pygame.display.update() # update the display
        c.tick(60) # only three images per second
        

        
        
if __name__ == '__main__': main()

    
