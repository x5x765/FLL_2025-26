import pygame
from objects import *
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Artifact Piece")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.mouse.get_pressed():
            pos = pygame.mouse.get_pos()
            if :

