import pygame as pg
from objects import *
pg.init()

pg.mixer.init()
pg.mixer.music.load(r"sounds\background.mp3")
pg.mixer.music.play(-1, 0.0)

screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.display.set_caption("Artifact Piece")
clock = pg.time.Clock()
piece = Piece(200, 200, r"images\piece1.png")
running = True
while running:
    piece.update(screen)
    screen.fill((230, 230, 230))
    piece.draw(screen)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if piece.rect.collidepoint(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]):
                piece.isSelected = not piece.isSelected
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
    pg.display.flip()
    clock.tick(60)
