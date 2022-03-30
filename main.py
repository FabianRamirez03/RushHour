# Rush Hour Game

# Imports
import pygame
import button
import board

# Constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
BOARD_POS = (58, 185)
TILESIZE = 44
SPACE = 13

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

# create button instances
start_btn = button.Button(250, 350, start_img, 1)
play_btn = button.Button(480, 515, play_img, 1)
exit_btn = button.Button(250, 450, exit_img, 1)

font = pygame.font.SysFont("Times New Roman", 30)

# !!!!!!!!!!!!!!!!!!!
# Scenes details
# sceneIndex = 0 -> menu
# sceneIndex = 1 -> initial config
# sceneIndex = 2 -> game

sceneIndex = 0
game_board = board.create_board()
board_surf = board.create_board_surf()
# Graphic Constants


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
    global running, sceneIndex
    screen.fill((255, 255, 255))
    screen.blit(board_img, (10, 120))
    screen.blit(header_img, (180, 10))
    screen.blit(board_surf, (44, 172))

    if play_btn.draw(screen) == True:
        sceneIndex = 2  # going to game scene


# Game scene
def drawGameScene(screen):
    screen.fill((0, 0, 0))
    text = font.render("Game", True, (255, 255, 255))
    screen.blit(text, (300, 220, 500, 200))


# Select which scene draw acording to scene index
def drawScene(screen):
    global sceneIndex
    # start
    if sceneIndex == 0:
        drawMenuScene(screen)

    elif sceneIndex == 1:
        drawConfigScene(screen)

    elif sceneIndex == 2:
        drawGameScene(screen)


# Run until the user asks to quit
running = True
while running:
    clock = pygame.time.Clock()
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and sceneIndex != 0:
            if event.key == pygame.K_ESCAPE:
                sceneIndex = 0  # going back to menu

    # Fill the background with white
    screen.fill((255, 255, 255))
    drawScene(screen)
    # Flip the display
    if sceneIndex == 1:
        piece, x, y = board.get_square_under_mouse(game_board)
        if x != None:
            rect = (BOARD_POS[0] + (x * TILESIZE) + (x*SPACE), BOARD_POS[1] + (y * TILESIZE) + (y*SPACE) , TILESIZE, TILESIZE)
            pygame.draw.rect(screen, (0, 0, 255, 50), rect, 2)
    pygame.display.flip()
    clock.tick(30)
# Done! Time to quit.
pygame.quit()
