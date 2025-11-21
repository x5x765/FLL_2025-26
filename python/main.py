import pygame as pg
from piece import Piece
pg.init()

pg.mixer.init()
pg.mixer.music.load(r"sounds\background.mp3")
pg.mixer.music.play(-1, 0.0)

screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.display.set_caption("Artifact Piece")
clock = pg.time.Clock()
piece1 = Piece(666, 150, r"images\piece (1).png")
piece2 = Piece(922, 151, r"images\piece (2).png")
piece3 = Piece(631, 258, r"images\piece (3).png")
piece4 = Piece(778, 202, r"images\piece (4).png")
piece5 = Piece(989, 253, r"images\piece (5).png")
piece6 = Piece(902, 277, r"images\piece (6).png")
piece7 = Piece(763, 294, r"images\piece (7).png")
piece8 = Piece(676, 392, r"images\piece (8).png")
piece9 = Piece(932, 414, r"images\piece (9).png")
piece10 = Piece(646, 537, r"images\piece (10).png")
piece11 = Piece(943, 513, r"images\piece (11).png")
piece12 = Piece(868, 534, r"images\piece (12).png")
piece13 = Piece(656, 674, r"images\piece (13).png")
piece14 = Piece(780, 648, r"images\piece (14).png")
piece15 = Piece(895, 674, r"images\piece (15).png")
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
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
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
