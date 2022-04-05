# Rush Hour Game


# Imports
import pygame
import button
import board
import pieces
import AI

# Constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
BOARD_POS = (58, 185)
TILESIZE = 44
SPACE = 13
EMPTY_SPACE = '.'
N = 6
board_matrix = [[EMPTY_SPACE] * N for _ in range(N)]

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Rush Hour Game")

# images
image = pygame.image.load(r'./images/Home.PNG')
start_img = pygame.image.load(r'./images/start_btn.png').convert_alpha()
exit_img = pygame.image.load(r'./images/exit_btn.png').convert_alpha()
play_img = pygame.image.load(r'./images/play_btn.png').convert_alpha()
board_img = pygame.image.load(r'./images/board.png').convert_alpha()
header_img = pygame.image.load(r'./images/header.png').convert_alpha()
next_img = pygame.image.load(r'./images/next_btn.png').convert_alpha()
prev_img = pygame.image.load(r'./images/previus_btn.png').convert_alpha()
ver_car_img = pygame.image.load(r'./images/vertical_car_img.png').convert_alpha()
hor_car_img = pygame.image.load(r'./images/horizontal_car_img.png').convert_alpha()
ver_truck_img = pygame.image.load(r'./images/vertical_truck_img.png').convert_alpha()
hor_truck_img = pygame.image.load(r'./images/horizontal_truck_img.png').convert_alpha()
trash_can_img = pygame.image.load(r'./images/trash_can.png').convert_alpha()

# create button instances
start_btn = button.Button(250, 350, start_img, 1)
play_btn = button.Button(480, 515, play_img, 1)
exit_btn = button.Button(250, 450, exit_img, 1)
next_btn = button.Button(480, 270, next_img, 1)
prev_btn = button.Button(480, 350, prev_img, 1)
hor_truck_btn = button.Button(485, 270, hor_truck_img, 1)
ver_truck_btn = button.Button(485, 330, ver_truck_img, 1)
ver_car_btn = button.Button(485, 390, ver_car_img, 1)
hor_car_btn = button.Button(485, 450, hor_car_img, 1)

# create config pieces array
configPieces = []
letter = 'A'
valid = True  # quick fix bug: create multiple config pieces

font = pygame.font.SysFont("Times New Roman", 30)

# !!!!!!!!!!!!!!!!!!!
# Scenes details
# sceneIndex = 0 -> menu
# sceneIndex = 1 -> initial config
# sceneIndex = 2 -> game

sceneIndex = 0
game_board = board.create_board()
board_surf = board.create_board_surf()

matrix = [[['.', 'B', 'B', 'B', '.', '.'], ['G', 'G', 'G', 'c', 'h', '.'], ['.', 'A', 'A', 'c', 'h', '.'],
           ['e', '.', '.', 'c', 'h', '.'], ['e', '.', 'f', '.', 'D', 'D'], ['e', '.', 'f', '.', '.', '.']],
          [['.', '.', 'B', 'B', 'B', '.'], ['G', 'G', 'G', 'c', 'h', '.'], ['.', 'A', 'A', 'c', 'h', '.'],
           ['e', '.', '.', 'c', 'h', '.'], ['e', '.', 'f', '.', 'D', 'D'], ['e', '.', 'f', '.', '.', '.']],
          [['.', '.', '.', 'B', 'B', 'B'], ['G', 'G', 'G', 'c', 'h', '.'], ['.', 'A', 'A', 'c', 'h', '.'],
           ['e', '.', '.', 'c', 'h', '.'], ['e', '.', 'f', '.', 'D', 'D'], ['e', '.', 'f', '.', '.', '.']],
          [['.', '.', '.', 'B', 'B', 'B'], ['G', 'G', 'G', 'c', 'h', '.'], ['A', 'A', '.', 'c', 'h', '.'],
           ['e', '.', '.', 'c', 'h', '.'], ['e', '.', 'f', '.', 'D', 'D'], ['e', '.', 'f', '.', '.', '.']],
          [['.', '.', '.', 'B', 'B', 'B'], ['G', 'G', 'G', 'c', 'h', '.'], ['A', 'A', '.', 'c', 'h', '.'],
           ['e', '.', 'f', 'c', 'h', '.'], ['e', '.', 'f', '.', 'D', 'D'], ['e', '.', '.', '.', '.', '.']],
          [['.', '.', '.', 'B', 'B', 'B'], ['G', 'G', 'G', 'c', 'h', '.'], ['A', 'A', 'f', 'c', 'h', '.'],
           ['e', '.', 'f', 'c', 'h', '.'], ['e', '.', '.', '.', 'D', 'D'], ['e', '.', '.', '.', '.', '.']],
          [['.', '.', '.', 'B', 'B', 'B'], ['G', 'G', 'G', 'c', 'h', '.'], ['A', 'A', 'f', 'c', 'h', '.'],
           ['e', '.', 'f', 'c', 'h', '.'], ['e', '.', '.', 'D', 'D', '.'], ['e', '.', '.', '.', '.', '.']],
          [['.', '.', '.', 'B', 'B', 'B'], ['G', 'G', 'G', 'c', 'h', '.'], ['A', 'A', 'f', 'c', 'h', '.'],
           ['e', '.', 'f', 'c', 'h', '.'], ['e', '.', 'D', 'D', '.', '.'], ['e', '.', '.', '.', '.', '.']],
          [['.', '.', '.', 'B', 'B', 'B'], ['G', 'G', 'G', 'c', '.', '.'], ['A', 'A', 'f', 'c', 'h', '.'],
           ['e', '.', 'f', 'c', 'h', '.'], ['e', '.', 'D', 'D', 'h', '.'], ['e', '.', '.', '.', '.', '.']],
          [['.', '.', '.', 'B', 'B', 'B'], ['G', 'G', 'G', 'c', '.', '.'], ['A', 'A', 'f', 'c', '.', '.'],
           ['e', '.', 'f', 'c', 'h', '.'], ['e', '.', 'D', 'D', 'h', '.'], ['e', '.', '.', '.', 'h', '.']],
          [['.', '.', '.', 'B', 'B', 'B'], ['G', 'G', 'G', 'c', '.', '.'], ['A', 'A', 'f', 'c', '.', '.'],
           ['e', '.', 'f', 'c', 'h', '.'], ['e', 'D', 'D', '.', 'h', '.'], ['e', '.', '.', '.', 'h', '.']],
          [['.', '.', '.', 'B', 'B', 'B'], ['G', 'G', 'G', '.', '.', '.'], ['A', 'A', 'f', 'c', '.', '.'],
           ['e', '.', 'f', 'c', 'h', '.'], ['e', 'D', 'D', 'c', 'h', '.'], ['e', '.', '.', '.', 'h', '.']],
          [['.', '.', '.', 'B', 'B', 'B'], ['.', 'G', 'G', 'G', '.', '.'], ['A', 'A', 'f', 'c', '.', '.'],
           ['e', '.', 'f', 'c', 'h', '.'], ['e', 'D', 'D', 'c', 'h', '.'], ['e', '.', '.', '.', 'h', '.']],
          [['.', '.', '.', 'B', 'B', 'B'], ['.', '.', 'G', 'G', 'G', '.'], ['A', 'A', 'f', 'c', '.', '.'],
           ['e', '.', 'f', 'c', 'h', '.'], ['e', 'D', 'D', 'c', 'h', '.'], ['e', '.', '.', '.', 'h', '.']],
          [['.', '.', '.', 'B', 'B', 'B'], ['.', '.', '.', 'G', 'G', 'G'], ['A', 'A', 'f', 'c', '.', '.'],
           ['e', '.', 'f', 'c', 'h', '.'], ['e', 'D', 'D', 'c', 'h', '.'], ['e', '.', '.', '.', 'h', '.']],
          [['.', '.', '.', 'B', 'B', 'B'], ['.', '.', 'f', 'G', 'G', 'G'], ['A', 'A', 'f', 'c', '.', '.'],
           ['e', '.', '.', 'c', 'h', '.'], ['e', 'D', 'D', 'c', 'h', '.'], ['e', '.', '.', '.', 'h', '.']],
          [['.', '.', 'f', 'B', 'B', 'B'], ['.', '.', 'f', 'G', 'G', 'G'], ['A', 'A', '.', 'c', '.', '.'],
           ['e', '.', '.', 'c', 'h', '.'], ['e', 'D', 'D', 'c', 'h', '.'], ['e', '.', '.', '.', 'h', '.']],
          [['.', '.', 'f', 'B', 'B', 'B'], ['.', '.', 'f', 'G', 'G', 'G'], ['A', 'A', '.', '.', '.', '.'],
           ['e', '.', '.', 'c', 'h', '.'], ['e', 'D', 'D', 'c', 'h', '.'], ['e', '.', '.', 'c', 'h', '.']]]
step = 0


# Menu Scene
def drawMenuScene(screen):
    global sceneIndex, running
    screen.fill((255, 255, 255))
    # image
    screen.blit(image, (15, 100))
    # buttons (Start and Exit)
    if start_btn.draw(screen) == True:
        sceneIndex = 1  # going to initial config scene

    if exit_btn.draw(screen) == True:
        running = False  # quit


# Inital Config Scene
def drawConfigScene(screen):
    global running, sceneIndex, configPieces, letter, matrix
    screen.fill((255, 255, 255))

    screen.blit(header_img, (180, 10))
    screen.blit(board_surf, (44, 172))
    screen.blit(board_img, (10, 120))
    screen.blit(trash_can_img, (338, 527))
    # ---
    # -------
    piece, x, y = board.get_square_under_mouse(game_board)
    if x != None:
        rect = (BOARD_POS[0] + (x * TILESIZE) + (x * SPACE), BOARD_POS[1] + (y * TILESIZE) + (y * SPACE), TILESIZE,
                TILESIZE)
        pygame.draw.rect(screen, (245, 152, 33, 50), rect, 2)

    if ver_car_btn.draw(screen) == True and valid == True:
        newPiece = pieces.Piece(540, 142, 50, 105, letter, "v", "c", ver_car_img);
        letter = chr(ord(letter) + 1)
        configPieces.append(newPiece)

    elif ver_truck_btn.draw(screen) == True and valid == True:
        newPiece = pieces.Piece(540, 80, 50, 162, letter, "v", "t", ver_car_img);
        letter = chr(ord(letter) + 1)
        configPieces.append(newPiece)

    elif hor_car_btn.draw(screen) == True and valid == True:
        newPiece = pieces.Piece(515, 182, 105, 50, letter, "h", "c", ver_car_img);
        letter = chr(ord(letter) + 1)
        configPieces.append(newPiece)

    elif hor_truck_btn.draw(screen) == True and valid == True:
        newPiece = pieces.Piece(486, 182, 163, 50, letter, "h", "t", ver_car_img);
        letter = chr(ord(letter) + 1)
        configPieces.append(newPiece)

    board.draw_config_pieces(screen, configPieces)

    if play_btn.draw(screen) == True:
        configMatrix = board.generateMatrix(configPieces)  # => generate config matrix <=
        print("Config Matrix:\n", configMatrix)
        #print('\n'.join(''.join(_) for _ in configMatrix))
        matrix = AI.solve(configMatrix)
        sceneIndex = 2  # going to game scene


# Game scene
def drawGameScene(screen):
    global step
    screen.fill((255, 255, 255))
    screen.blit(board_img, (10, 120))
    screen.blit(header_img, (180, 10))

    if len(matrix) > 0 :

        pieces = board.get_pieces(matrix[step])
        board.draw_game_pieces(pieces, screen)

        if next_btn.draw(screen) == True and step < len(matrix) - 1:
            step = step + 1

        if prev_btn.draw(screen) == True and step > 0:
            step = step - 1
    else:
        text = font.render('Impossible', True, (255,255,255), (0,0,0))
        textRect = text.get_rect()
        textRect.center = (540, 315)
        screen.blit(text,textRect)

# Select which scene draw according to scene index
def drawScene(screen):
    global sceneIndex
    # start
    if sceneIndex == 0:
        drawMenuScene(screen)

    elif sceneIndex == 1:
        drawConfigScene(screen)

    elif sceneIndex == 2:
        drawGameScene(screen)


def placePieceOnMatrix(piece, y, x):
    global board_matrix
    cont = 0
    if piece.type == 't':
        length = 3
    if piece.type == 'c':
        length = 2
    clearCarFromMatrix(piece.letter, length, board_matrix)
    if piece.direction == 'h':
        while cont < length:
            board_matrix[y][x+cont] = piece.letter
            cont += 1
    if piece.direction == 'v':
        while cont < length:
            board_matrix[y+cont][x] = piece.letter
            cont += 1

def clearCarFromMatrix(letter, length, board):
    cont = 0
    x = 0
    y = 0
    while y < 6:
        x = 0
        while x < 6:
            if board[y][x] == letter:
                board[y][x] = EMPTY_SPACE
                cont += 1
            x += 1
        if cont == length:
            break
        y += 1

def delete_piece(piece):
    global valid
    if piece.type == 't':
        length = 3
    if piece.type == 'c':
        length = 2
    clearCarFromMatrix(piece.letter, length, board_matrix)
    piece.delete()
    valid = True


# Run until the user asks to quit
running = True
# selected_piece = None
while running:
    clock = pygame.time.Clock()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Did the user click the window close button?
            running = False
        elif event.type == pygame.KEYDOWN and sceneIndex != 0:
            if event.key == pygame.K_ESCAPE:
                configPieces = []
                letter = 'A'
                step = 0
                sceneIndex = sceneIndex - 1  # going back

        elif event.type == pygame.MOUSEBUTTONDOWN and sceneIndex == 1:
            pos = pygame.mouse.get_pos()
            for piece in configPieces:
                if piece.rect.collidepoint(event.pos):
                    piece.clicked = True
                    print("piece letter: ", piece.letter)
                    valid = False

        elif event.type == pygame.MOUSEMOTION and sceneIndex == 1:
            pos = pygame.mouse.get_pos()
            for piece in configPieces:
                if piece.clicked:
                    piece.rect.x = piece.rect.x + (pos[0] - piece.rect.x)
                    piece.rect.y = piece.rect.y + (pos[1] - piece.rect.y)
        elif event.type == pygame.MOUSEBUTTONUP and sceneIndex == 1:
            piece, y, x = board.get_square_under_mouse(game_board)
            print(x, y)
            pos = pygame.mouse.get_pos()
            if 335 <= pos[0] <= 385 and 525 <= pos[1] <= 580:
                for piece in configPieces:
                    if piece.clicked:
                        delete_piece(piece)
                        print(board_matrix)
                        print('delete piece')
            if x is not None:
                for piece in configPieces:
                    if piece.clicked:
                        piece.rect.x = board.get_grapich_pos(x, y).x
                        piece.rect.y = board.get_grapich_pos(x, y).y - 1
                        piece.xMatrixPos = x
                        piece.yMatrixPos = y
                        placePieceOnMatrix(piece, x, y)
                        piece.clicked = False
                        valid = True

    # Fill the background with white
    screen.fill((255, 255, 255))
    drawScene(screen)

    # Flip the display
    pygame.display.flip()
    clock.tick(30)

# Done! Time to quit.
pygame.quit()
