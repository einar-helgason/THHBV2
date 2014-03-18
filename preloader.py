'''
Created on Mar 7, 2014

@author: Tryggvi
'''
import pygame
from globals import *



def load_image(file):
    """loads an image, prepares it for play, returns a surface"""
    file = os.path.join(main_dir, 'data/images', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()

def load_images(*files):
    """loads images, returns a list of surfaces from images given in args"""
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs

def main():
    print load_image.__doc__
    
if __name__ == "__main__":
    main()