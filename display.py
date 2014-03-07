'''
Created on Mar 7, 2014

@author: Tryggvi
'''
import pygame 
from pygame.locals import *
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]
SCREENRECT = Rect(0, 0, 640, 480)

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'data', file)
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
    
    winstyle = 0 |FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
    pygame.display.set_caption("Mouse Focus Workout")
    c = pygame.time.Clock()
   
    going = True
    while going :
        for e in pygame.event.get():
            if e.type == QUIT:
                going = False
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    going = False
                    
        screen.blit(load_image("01c.gif"),(0,0))
        pygame.display.flip() # update the display
        #c.tick(3) # only three images per second
        
        
   
 
if __name__ == '__main__': main()

    
