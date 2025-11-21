from random import randint
import pygame
pygame.init()

class Piece:
    def __init__(self, xGoal, yGoal, image_path):
        self.xGoal = xGoal
        self.yGoal = yGoal
        self.image = pygame.image.load(image_path).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.isSelected = False
        self.rect.center = (randint(50, 1500), randint(50, 800))
        self.isInPlace = False
        self.imagePath = image_path

    def __str__(self):
        return f"{str(self.rect.centerx)}, {str(self.rect.centery)}, {self.imagePath}"

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, screen):
        if self.isSelected and not self.isInPlace:
            self.rect.center = pygame.mouse.get_pos()
        if self.rect.centerx in range(self.xGoal-10, self.xGoal+10) and self.rect.centery in range(self.yGoal-10, self.yGoal+10) and not self.isInPlace:
            self.rect.center = (self.xGoal, self.yGoal)
            self.isInPlace = True
