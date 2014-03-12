'''
Created on Mar 10, 2014

@author: Tryggvi
'''
import pygame
from pygame.locals import *

def is_mouse_moving():
    for e in pygame.event.get():
        if e.type == MOUSEMOTION :
            return True
        else : return False
        
def is_left_mouse_down():
    if pygame.mouse.get_pressed()[0] :
        return True 
    else : return False