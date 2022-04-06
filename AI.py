import pygame
import random
import time

N = 6
EMPTY_SPACE = '_'
ICE_CREAM_TRUCK = 'A'
START_ROW = 2

# Game logic variables
global state_counter

# GUI constants
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
BOARD_SIZE = 1000
TILE_SIZE = 60
TOP_MARGIN = 10
LEFT_MARGIN = 175
# Colours
RED = (210, 43, 43)
PINK = (255, 207, 223)
GREEN = (198, 213, 126)
SKY_BLUE = (165, 222, 229)
BLUE = (5, 102, 118)
PURPLE = (114, 106, 149)
YELLOW = (250, 240, 175)
ORANGE = (254, 179, 119)
BROWN = (125, 90, 90)
TILE = (128,128,128)
BOARD = (100, 100, 100)
BLACK = (40, 40, 40)

# Car colour dictionary
CAR_COLOURS = {
  "A": RED,
  "B": BLUE,
  "c": GREEN,
  "D": PURPLE,
  "e": YELLOW,
  "f": BLACK,
  "g": ORANGE,
  "h": SKY_BLUE,
  "i": BROWN,
  "j": PINK,
}

def textElements(message, font):
  textBox = font.render(message, True, BLACK)
  return textBox, textBox.get_rect()

def create_button(message, color, hovered_color, pos_x, pos_y, width, height, surface, function, arguments):
  mouseX, mouseY = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()

  if (pos_x + width > mouseX > pos_x and pos_y + height > mouseY > pos_y):
    pygame.draw.rect(surface, hovered_color, (pos_x, pos_y, width, height))
    if (click[0] == 1 and function != None):
      if (arguments != None):
        function(arguments)
      else:
        function()
  else:
    pygame.draw.rect(surface, color, (pos_x, pos_y, width, height))
  textMsg, textBox = textElements(message, pygame.font.Font("freesansbold.ttf", 30))
  textBox.center = (int((pos_x + (width / 2))), int((pos_y + (height / 2))))
  surface.blit(textMsg, textBox)

def start_game():
  global state_counter
  pygame.init()
  surface = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
  state_counter = 0
  states_list = [[["_","f","h","_","g","_"], ["e","f","h","_","g","_"], ["e","A","A","_","_","_"], ["_","_","_","c","i","j"], ["_","B","B","c","i","j"], ["_","D","D","c","_","j"]], [["_","A","B","_","g","_"], ["e","f","h","_","g","_"], ["e","A","A","_","h","_"], ["_","_","_","c","i","j"], ["_","c","B","c","i","j"], ["_","D","D","c","_","j"]], [["_","f","h","_","g","_"], ["e","f","h","_","g","_"], ["e","A","A","_","_","_"], ["_","_","_","c","i","j"], ["_","B","B","c","i","j"], ["_","D","D","c","_","j"]]]
  state_qty = len(states_list) - 1

  while(True):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          quit()
    current_state = states_list[state_counter]

    draw_board(surface)
    draw_cars(surface, current_state)
    pygame.display.flip()
    create_button("Next", YELLOW, YELLOW, 800, 300, 150, 30, surface, get_next_state, state_qty)
    create_button("Previous", GREEN, GREEN, 0, 300, 150, 30, surface, get_previous_state, None)
    pygame.display.update()

def draw_board(surface):
  pygame.draw.rect(surface, BOARD, pygame.Rect(LEFT_MARGIN, TOP_MARGIN, 600, 600))
  for y in range(0, 6):
    for x in range(0, 6):
      pygame.draw.rect(surface, TILE, pygame.Rect(LEFT_MARGIN + 20 + x * 100, TOP_MARGIN + 20 + y * 100, 60, 60), 5)

def draw_cars(surface, board_state):
  for y in range(0, 6):
    for x in range(0, 6):
      if board_state[y][x] != '_':
        colour = CAR_COLOURS[board_state[y][x]]
        pygame.draw.rect(surface, colour, pygame.Rect(LEFT_MARGIN + x*100, TOP_MARGIN+y*100, 100, 100))


def get_next_state(state_qty):
  print("Next")
  global state_counter
  if state_counter < state_qty:
    state_counter += 1
  time.sleep(0.15)
  return

def get_previous_state():
  print("Previous")
  global state_counter
  if state_counter > 0:
    state_counter -= 1
  time.sleep(0.15)
  return

def get_board():
  # Uppercase is horizontal, lowercase is vertical.
  board = [[EMPTY_SPACE] * 6 for _ in range(N)]
  # Initialize the ice cream truck in a random column.
  start_col = random.randrange(N - 2)
  board[START_ROW][start_col] = board[START_ROW][start_col + 1] = ICE_CREAM_TRUCK

  # Add more cars.
  num_attempts = 0
  for i in range(random.randrange(6, 10)):
    car_len = random.randrange(2, 4)
    while True:
      vertical = random.randrange(2) == 0
      r = random.randrange(N - (car_len - 1) * int(vertical))
      c = random.randrange(N - (car_len - 1) * int(not vertical))
      is_clear = True
      for j in range(car_len):
        if board[r + j * int(vertical)][c + j * int(not vertical)] != EMPTY_SPACE:
          is_clear = False
          break

      if is_clear:
        car_char = chr(ord('b' if vertical else 'B') + i)
        for j in range(car_len):
          board[r + j * int(vertical)][c + j * int(not vertical)] = car_char
        break

      num_attempts += 1
      if num_attempts > 1000:
        # We have enough cars anyway.
        break

  return board


def board_str(board):
  return '\n'.join(''.join(_) for _ in board)


def copy_board(board):
  return [_[:] for _ in board]


def is_solved(board):
  # Find any obstacles between the ice cream truck and the right edge.
  for i in range(N - 1, -1, -1):
    char_i = board[START_ROW][i]
    if char_i == EMPTY_SPACE:
      continue
    elif char_i == ICE_CREAM_TRUCK:
      return True
    else:
      return False

  return True


def get_next_states(board):
  processed_chars_set = set([EMPTY_SPACE])
  next_states = []
  for r in range(N):
    for c in range(N):
      char = board[r][c]
      if char not in processed_chars_set:
        processed_chars_set.add(char)
        delta_r = 0
        delta_c = 0
        is_vertical = not char.isupper()
        if is_vertical:
          delta_r = 1
        else:
          delta_c = 1

        # Find the extrema
        min_r, max_r = r, r
        min_c, max_c = c, c
        while min_r - delta_r >= 0 and min_c - delta_c >= 0 and board[min_r - delta_r][min_c - delta_c] == char:
          min_r -= delta_r
          min_c -= delta_c

        while max_r + delta_r < N and max_c + delta_c < N and board[max_r + delta_r][max_c + delta_c] == char:
          max_r += delta_r
          max_c += delta_c

        if min_r - delta_r >= 0 and min_c - delta_c >= 0 and board[min_r - delta_r][min_c - delta_c] == EMPTY_SPACE:
          next_state = copy_board(board)
          next_state[min_r - delta_r][min_c - delta_c] = char
          next_state[max_r][max_c] = EMPTY_SPACE
          next_states.append(next_state)

        if max_r + delta_r < N and max_c + delta_c < N and board[max_r + delta_r][max_c + delta_c] == EMPTY_SPACE:
          next_state = copy_board(board)
          next_state[min_r][min_c] = EMPTY_SPACE
          next_state[max_r + delta_r][max_c + delta_c] = char
          next_states.append(next_state)

  return next_states


PLIES = {}
def search(board):
  queue = [(0, [board])]
  board_hash_set = set()

  while queue:
    ply, path = queue.pop(0)
    if ply not in PLIES:
      PLIES[ply] = 1
    else:
      PLIES[ply] += 1

    if is_solved(path[-1]):
      return path

    for next_state in get_next_states(path[-1]):
      if board_str(next_state) not in board_hash_set:
        board_hash_set.add(board_str(next_state))
        queue.append((ply + 1, path + [next_state]))

  return []

start_game()

"""while True:
  board = get_board()
  path = search(board)
  print('Solved length: {}'.format(len(path)))
  print(PLIES)
  if len(path) >= 15:
    print('\n\n'.join(board_str(_) for _ in path))
    break"""