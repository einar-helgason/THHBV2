'''
Created on Mar 7, 2014

@author: Tryggvi
'''
import pygame 
from pygame.locals import *
import os
import card

main_dir = os.path.split(os.path.abspath(__file__))[0]
SCREENRECT = Rect(0, 0, 640, 480)

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'data', 'images', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()

def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs


def main():
    pygame.init()
    #win = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
    
    winstyle = 0 #|FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
    pygame.display.set_caption("Mouse Focus Workout")
    c = pygame.time.Clock()
    
    all = pygame.sprite.RenderUpdates()
    
   
    going = True
    #prufa
    myDeck = card.Deck()
    myCard = myDeck.cards[0]
    ###########
    while going :
        mx,my = pygame.mouse.get_pos()
        mouse_left_down = pygame.mouse.get_pressed()[0]
        
        print mouse_left_down
        for e in pygame.event.get():
            if e.type == QUIT:
                going = False
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    going = False
        if mouse_left_down : 
            myCard.x = mx
            myCard.y = my
        
        screen.blit(myCard.image,(myCard.x,myCard.y))
        
        pygame.display.update() # update the display
        c.tick(60) # only three images per second
        
        
   
 
if __name__ == '__main__': main()

    
