"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    # it's basically 3 lists of 3
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    flat_board = [cell for row in board for cell in row]
    if flat_board.count(X) > flat_board.count(O):
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell is EMPTY:
                action_set.add((i, j))
    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception # if action not valid

    # copy the board
    board_copy = copy.deepcopy(board)

    board_copy[action[0]][action[1]] = player(board_copy)

    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # all possible win combinations

    win_combinations = [[(0, 0), (0, 1), (0, 2)],
                        [(1, 0), (1, 1), (1, 2)],
                        [(2, 0), (2, 1), (2, 2)],
                        [(0, 0), (1, 0), (2, 0)],
                        [(0, 1), (1, 1), (2, 1)],
                        [(0, 2), (1, 2), (2, 2)],
                        [(0, 0), (1, 1), (2, 2)],
                        [(0, 2), (1, 1), (2, 0)]]
    
    for combination in win_combinations:
        x = 0
        o = 0
        for i, j in combination:
            if board[i][j] == X:
                x += 1
            if board[i][j] == O:
                o += 1
            # get winner
            if x == 3:
                return X
            if o == 3:
                return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def max_val(board):
    if terminal(board):
        return utility(board)
    m = float("-inf")
    for action in actions(board):
        m = max(m, min_val(result(board, action)))
    return m

def min_val(board):
    if terminal(board):
        return utility(board)
    m = float("-inf")
    for action in actions(board):
        m = min(m, max_val(result(board, action)))
    return m

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # if board is empty
    if board == initial_state():
        return (0,0)
    
    if player(board) == X:
        m = float("-inf")
        player_do = None
        for action in actions(board):
            min_result = min_val(result(board, action))
            if min_result > m:
                m = min_result
                player_do = action
    
    elif player(board) == O:
        m = float("inf")
        player_do = None
        for action in actions(board):
            max_result = max_val(result(board, action))
            if max_result < m:
                m = max_result
                player_do = action   
    
    return player_do
        
