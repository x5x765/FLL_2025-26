import pygame
pygame.init()

class Piece:
    def __init__(self,x,y, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
    def draw(self,screen):
        pass
