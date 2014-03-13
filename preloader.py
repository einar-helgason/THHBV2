'''
Created on Mar 7, 2014

@author: Tryggvi
'''
import pygame
from globals import *



def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'data/images', file)
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
