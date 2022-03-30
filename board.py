import pygame

TILESIZE = 44

def create_board_surf():
    board_surf = pygame.Surface((TILESIZE*9, TILESIZE*9))
    board_surf.set_colorkey((0, 0, 0))  #transparent mode
    SPACE = 13
    xSpace = SPACE
    ySpace = SPACE
    dark = False
    for y in range(6):
        for x in range(6):
            rect = pygame.Rect((x*TILESIZE)+xSpace, (y*TILESIZE)+ySpace, TILESIZE, TILESIZE)
            pygame.draw.rect(board_surf, pygame.Color('indianred1' if dark else 'indianred1'), rect)
            dark = not dark
            xSpace = xSpace + SPACE
        dark = not dark
        ySpace = ySpace + SPACE
        xSpace = SPACE
    return board_surf

def create_board():
    board = []
    for y in range(6):
        board.append([])
        for x in range(6):
            board[y].append(None)

    return board