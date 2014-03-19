'''
Created on Mar 7, 2014

@author: Tryggvi
'''
import os
from pygame.locals import *
import pygame


is_left_mouse_down = False
is_mouse_moving = False
y_offset = 70


main_dir = os.path.split(os.path.abspath(__file__))[0]
SCREENRECT = Rect(0, 0, 640, 480)
