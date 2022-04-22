import random

N = 6
EMPTY_SPACE = '_'
ICE_CREAM_TRUCK = 'A'
START_ROW = 2
EXIT_ROW = 2


def board_str(board):
    return '\n'.join(''.join(_) for _ in board)


def copy_board(board):
    return [_[:] for _ in board]


def is_solved(board):
    # Find any obstacles between the main cart and the right edge.
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

                if min_r - delta_r >= 0 and min_c - delta_c >= 0 and board[min_r - delta_r][
                    min_c - delta_c] == EMPTY_SPACE:
                    next_state = copy_board(board)
                    next_state[min_r - delta_r][min_c - delta_c] = char
                    next_state[max_r][max_c] = EMPTY_SPACE
                    next_states.append(next_state)

                if max_r + delta_r < N and max_c + delta_c < N and board[max_r + delta_r][
                    max_c + delta_c] == EMPTY_SPACE:
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

        sorted_states = sort_heuristics(get_next_states(path[-1]))
        for next_state in sorted_states:
            if board_str(next_state) not in board_hash_set:
                board_hash_set.add(board_str(next_state))
                queue.append((ply + 1, path + [next_state]))
    return []


def solve(board):
    calc_heuristic(board)
    path = search(board)
    return path


# ***************************
#   HEURISTIC CALCULATION
# ***************************
def sort_heuristics(possible_next_states):
    sorted_states = []
    heuristics_states = []
    for state in possible_next_states:
        heuristics_states.append([calc_heuristic(state), state])
    heuristics_states.sort(key=lambda x: x[0])
    for state in heuristics_states:
        sorted_states.append(state[1])
    return sorted_states


def calc_heuristic(board):
    result = 0
    blockers = get_blocking_cars(board[EXIT_ROW])
    min_sub_blockers = get_min_subblocking_cars(board, blockers)
    for sub in min_sub_blockers:
        result += len(sub)
    result += len(blockers)
    return result


def get_blocking_cars(exit_row):
    result = []
    unique_cars = remove_repeated(exit_row)
    red_car_pos = unique_cars.index('A')
    for i in range(red_car_pos + 1, len(unique_cars)):
        if unique_cars[i] != "_":
            result.append(unique_cars[i])
    return result


def get_board_column(board, column):
    result = []
    for line in board:
        result.append(line[column])
    return result


def get_blocking_columns(board, blocking_cars):
    blocking_cars_positions = []
    result = []
    for car in blocking_cars:
        blocking_cars_positions.append(board[EXIT_ROW].index(car))
    for pos in blocking_cars_positions:
        result.append(remove_repeated(get_board_column(board, pos)))
    return result


def get_min_subblocking_cars(board, blocking_cars):
    result = []
    blocking_columns = get_blocking_columns(board, blocking_cars)
    for i in range(len(blocking_columns)):
        top, bottom = get_top_bot_blockers(blocking_columns[i], blocking_cars[i])
        result.append(remove_blanks(top)) if len(top) < len(bottom) else result.append(remove_blanks(bottom))
    return result


def get_top_bot_blockers(column, separator):
    index = column.index(separator)
    top = column[:index]
    column.reverse()
    index = column.index(separator)
    bottom = column[:index]
    bottom.reverse()
    return top, bottom


def remove_blanks(row):
    result = []
    for elem in row:
        if elem != '_': result.append(elem)
    return result


def remove_repeated(row):
    result = []
    found = []
    for elem in row:
        if elem not in found:
            result.append(elem)
            found.append(elem)
    return result
