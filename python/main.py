import time
import pygame as pg
from piece import Piece
from time import sleep
pg.init()

pg.mixer.init()
pg.mixer.music.load(r"sounds\background.mp3")
pg.mixer.music.set_volume(0.2)
pg.mixer.music.play(-1, 0.0)
clickSound = pg.mixer.Sound(r"sounds\click.mp3")
completionSound = pg.mixer.Sound(r"sounds\completion.mp3")

def performCompletion():
    isFalse = False
    global completionSound
    global pieces
    for piece in pieces:
        if not piece.isInPlace:
            isFalse = True
            break
    if not isFalse:
        completionSound.play()

screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.display.set_caption("Artifact Piece")
clock = pg.time.Clock()

piece1 = Piece(646, 134, r"images\piece (1).png")
piece2 = Piece(902, 132, r"images\piece (2).png")
piece3 = Piece(607, 239, r"images\piece (3).png")
piece4 = Piece(763, 188, r"images\piece (4).png")
piece5 = Piece(970, 236, r"images\piece (5).png")
piece6 = Piece(886, 256, r"images\piece (6).png")
piece7 = Piece(746, 274, r"images\piece (7).png")
piece8 = Piece(653, 370, r"images\piece (8).png")
piece9 = Piece(912, 389, r"images\piece (9).png")
piece10 = Piece(622, 504, r"images\piece (10).png")
piece11 = Piece(922, 487, r"images\piece (11).png")
piece12 = Piece(848, 505, r"images\piece (12).png")
piece13 = Piece(630, 645, r"images\piece (13).png")
piece14 = Piece(754, 616, r"images\piece (14).png")
piece15 = Piece(865, 642, r"images\piece (15).png")
base_pot = Piece(800, 425, r"images\base_pot_cracked.png")

pieces = [piece1, piece2, piece3, piece4, piece5, piece6, piece7, piece8, piece9, piece10, piece11, piece12, piece13, piece14, piece15]

running = True
while running:
    screen.fill((230, 230, 230))
    for piece in pieces:
        piece.update(screen)
        piece.draw(screen)
    # pg.draw.rect(screen, (0, 0, 0), [200, 200, 20, 20]) #for debug
    for event in pg.event.get():
        performCompletion()
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            clickSound.play()
            for piece in pieces:
                if piece.rect.collidepoint(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]):
                    piece.isSelected = not piece.isSelected
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            elif event.key == pg.K_s: # for debug
                save = open("coords.txt", "wt")
                for piece in pieces:
                    save.write(str(piece) + "\n")
                save.close()
                del save
    pg.display.flip()
    clock.tick(60)
