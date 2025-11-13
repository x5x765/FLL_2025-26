import pygame
pygame.init()

class Piece:
    def __init__(self, x : int, y : int, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))
        self.isSelected = False

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, screen):
        if self.isSelected:
            screen.blit(self.image, self.rect)
            self.rect.center = pygame.mouse.get_pos()

