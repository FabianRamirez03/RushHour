import pygame

TILESIZE = 44
BOARD_POS = (58, 185)


def get_square_under_mouse(board):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    x = get_X_Under_Mouse(int(mouse_pos[0]))
    y = get_Y_Under_Mouse(int(mouse_pos[1]))
    try:
        if x != None and y != None:
            if x >= 0 and y >= 0: return board[y][x], x, y
    except IndexError:
        pass
    return None, None, None


def create_board_surf() -> object:
    board_surf = pygame.Surface((TILESIZE * 9, TILESIZE * 9))
    board_surf.set_colorkey((0, 0, 0))  # transparent mode
    SPACE = 13
    xSpace = SPACE
    ySpace = SPACE
    dark = False
    for y in range(6):
        for x in range(6):
            rect = pygame.Rect((x * TILESIZE) + xSpace, (y * TILESIZE) + ySpace, TILESIZE, TILESIZE)
            pygame.draw.rect(board_surf, pygame.Color('indianred1' if dark else 'red'), rect)
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


def get_X_Under_Mouse(x):
    if 56 <= x <= 100:
        return 0
    if 113 <= x <= 157:
        return 1
    if 160 <= x <= 214:
        return 2
    if 227 <= x <= 271:
        return 3
    if 284 <= x <= 328:
        return 4
    if 341 <= x <= 385:
        return 5
    else:
        return None

def get_Y_Under_Mouse(y):
    if 185 <= y <= 229:
        return 0
    if 242 <= y <= 286:
        return 1
    if 299 <= y <= 343:
        return 2
    if 356 <= y <= 400:
        return 3
    if 413 <= y <= 457:
        return 4
    if 470 <= y <= 514:
        return 5
    else:
        return None