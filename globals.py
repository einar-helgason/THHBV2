'''
Created on Mar 7, 2014

@author: Tryggvi
'''
import os
import pygame
from pygame.locals import *

x_offset = 70
y_offset = 18

card_width= 57
card_height = 85

main_dir = os.path.split(os.path.abspath(__file__))[0]
SCREENRECT = Rect(0, 0, 800, 480)

#constants
WINSIZE = [800, 480]
WINCENTER = [400, 240]
NUMSTARS = 150

white = 255, 240, 200
black = 20, 20, 40
pink = 199, 21, 133

def main():
    """This module contains global variables shared with all other modules."""
    print main.__doc__

if __name__ == '__main__': 
    main()
