# Импортируем библиотеку pygame
import pygame
from pygame.locals import *

class cage:
    def __init__(self):
        self.parrams = {'image': 'Object\Cage\cage.bmp'}

    def load_image(self):
        return pygame.image.load(self.parrams['image'])
