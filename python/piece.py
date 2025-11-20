from random import randint
import pygame
pygame.init()

class Piece:
    def __init__(self, xGoal, yGoal, image_path):
        self.x = randint(50, 1500)
        self.y = randint(50, 800)
        self.xGoal = xGoal
        self.yGoal = yGoal
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))
        self.isSelected = False
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, screen):
        if self.isSelected:
            screen.blit(self.image, self.rect)
            self.rect.center = pygame.mouse.get_pos()
        if self.rect.centerx in range(self.xGoal-10, self.xGoal+10):
            self.rect.center = (self.xGoal, self.yGoal)
