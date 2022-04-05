import pygame
import rect
import numpy as np
import random

TILESIZE = 44
BOARD_POS = (58, 185)
EMPTY_SPACE = '_'

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
    if 525 <= y <= 580:
        return 6
    else:
        return None

def draw_game_pieces(pieces, screen): #game screen draw function
    for i in pieces:
        x,y,typePiece,spaces,color = i

        rect = get_grapich_pos(x, y)
        if(typePiece=="h"):
            pygame.draw.rect(screen, color, pygame.Rect(rect.x, rect.y-3, 55+(55*spaces), 50))
        else:
            pygame.draw.rect(screen, color, pygame.Rect(rect.x, rect.y-7, 50, 55+(57*spaces)))

def get_grapich_pos(x,y):
    return rect.Rectangle(55+(y*57), 185+(x*57), 43, 45) #x, y, width, height

def get_pieces(matrix): #return (x,y,h/v,spaces)
    mControl = np.zeros((6, 6))
    pieces = []
    for y in range(6):
        for x in range(6):
            if mControl[y][x] == 0 and matrix[y][x].isalpha():
                mControl[y][x] = 1

                # Tipos de horizontales
                # 2 derecha (3 casillas)
                if (x + 1 <= 5 and x + 2 <= 5 and matrix[y][x + 1] == matrix[y][x] and matrix[y][x + 2] == matrix[y][
                    x]):
                    mControl[y][x + 1] = 1
                    mControl[y][x + 2] = 1
                    #print("horizontal: 2 derecha", matrix[y][x])
                    pieces.append((y, x, "h", 2,get_piece_color(matrix[y][x])))

                # 1 derecha (2 casillas)
                elif (x + 1 <= 5 and matrix[y][x + 1] == matrix[y][x]):
                    mControl[y][x + 1] = 1
                    #print("horizontal: 1 derecha", matrix[y][x])
                    pieces.append((y, x, "h", 1,get_piece_color(matrix[y][x])))

                # es vertical

                # Tipos de verticales
                # 2 abajo
                elif (y + 1 <= 5 and matrix[y + 1][x] == matrix[y][x] and y + 2 <= 5 and matrix[y + 2][x] == matrix[y][
                    x]):
                    mControl[y + 1][x] = 1
                    mControl[y + 2][x] = 1
                    #print("Vertical: 2 abajo ", matrix[y][x])
                    pieces.append((y, x, "v", 2, get_piece_color(matrix[y][x])))

                # 1 abajo
                elif (y + 1 <= 5 and matrix[y + 1][x] == matrix[y][x]):
                    mControl[y - 1][x] = 1
                    #print("Vertical: 1 abajo ", matrix[y][x])
                    pieces.append((y, x, "v", 1,get_piece_color(matrix[y][x])))
    return pieces

def get_piece_color(letter):
    if letter.upper() == 'A':
        return pygame.Color(173, 11, 9)
    if letter.upper() == 'B':
        return pygame.Color(72, 167, 201)
    if letter.upper() == 'C':
        return pygame.Color(122, 83, 167)
    if letter.upper() == 'D':
        return pygame.Color(252, 247, 102)
    if letter.upper() == 'E':
        return pygame.Color(240, 149, 51)
    if letter.upper() == 'F':
        return pygame.Color(1, 147, 116)
    if letter.upper() == 'G':
        return pygame.Color(38, 173, 97)
    if letter.upper() == 'H':
        return pygame.Color(170, 91, 212)
    if letter.upper() == 'I':
        return pygame.Color(0, 159, 172)
    if letter.upper() == 'J':
        return pygame.Color(8, 92, 68)
    if letter.upper() == 'K':
        return pygame.Color(255, 128, 249)
    if letter.upper() == 'L':
        return pygame.Color(255, 160, 128)
    if letter.upper() == 'M':
        return pygame.Color(79, 1, 32)
    if letter.upper() == 'N':
        return pygame.Color(76, 79, 1)
    if letter.upper() == 'Ñ':
        return pygame.Color(117, 255, 248)
    if letter.upper() == 'O':
        return pygame.Color(92, 35, 35)
    if letter.upper() == 'P':
        return pygame.Color(41, 35, 92)
    if letter.upper() == 'Q':
        return pygame.Color(92, 35, 83)
    if letter.upper() == 'R':
        return pygame.Color(131, 125, 181)
    if letter.upper() == 'S':
        return pygame.Color(50, 84, 76)
    if letter.upper() == 'T':
        return pygame.Color(119, 255, 0)

    return pygame.Color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

def draw_config_pieces(screen, pieces):
    for piece in pieces:
        piece.draw(screen)

def generateMatrix(configPieces):
    #matrix = np.empty((6, 6))
    matrix = [[EMPTY_SPACE] * 6 for _ in range(6)]

    for piece in configPieces:

        if piece.xMatrixPos != None and piece.yMatrixPos != None:
            #determine type (car or truck) and orientation (horizontal or vertical)

            #vertical car
            if piece.direction == "v" and piece.type == "c":
                matrix[piece.xMatrixPos][piece.yMatrixPos] = piece.letter
                matrix[piece.xMatrixPos+1][piece.yMatrixPos] = piece.letter

            # vertical truck
            elif piece.direction == "v" and piece.type == "t":
                matrix[piece.xMatrixPos][piece.yMatrixPos] = piece.letter
                matrix[piece.xMatrixPos + 1][piece.yMatrixPos] = piece.letter
                matrix[piece.xMatrixPos + 2][piece.yMatrixPos] = piece.letter

            #horizontal car
            elif piece.direction == "h" and piece.type == "c":
                matrix[piece.xMatrixPos][piece.yMatrixPos] = piece.letter
                matrix[piece.xMatrixPos][piece.yMatrixPos+1] = piece.letter

            #horizontal truck
            elif piece.direction == "h" and piece.type == "t":
                matrix[piece.xMatrixPos][piece.yMatrixPos] = piece.letter
                matrix[piece.xMatrixPos][piece.yMatrixPos+ 1] = piece.letter
                matrix[piece.xMatrixPos][piece.yMatrixPos+ 2] = piece.letter



    return matrix