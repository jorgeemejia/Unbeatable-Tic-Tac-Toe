"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
rows = 3
cols = 3


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #counters for amounts of x's and o's
    num_of_x = 0
    num_of_o = 0
    #loop through board and count instances of each
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == X:
                num_of_x += 1
            if board[r][c] == O:
                num_of_o += 1
    #O is only returned in one instance, if num of O's is less than num of X's
    if num_of_o < num_of_x:
        return O
    #X is returned in two instances, 
    #num of x is less than num of o
    #num of x is same as num of o
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #moves will contain all possible actions
    moves = set()
    #loop through the board
    for r in range(rows):
        for c in range(cols):
            #if the space isn't occupied, then add it to the set
            if board[r][c] != X and board[r][c] != O:
                moves.add((r,c))
    
    return moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    #call actions function to get a set of all legal/possible moves
    moves = actions(board)
    #if the requested action isn't in moves(list of tuples), then raise the exception
    if action not in moves:
        raise Exception("Action is not a valid action for the board")
    #make a deep copy of the board
    boardCopy = copy.deepcopy(board)
    #get the current player using the player function
    currPlayer = player(board)

    #since action is a tuple 
    r = action[0]
    c = action[1]
    if currPlayer == X:
        boardCopy[r][c] == X
    else:
        boardCopy[r][c] == O

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #top row match and it's not a group of None's
    if board[0][0] == board[0][1] == board[0][2] and board[0][2] != None:
        return board[0][0]
    #middle row match
    elif board[1][0] == board[1][1] == board[1][2] and board[1][2] != None:
        return board[1][0]
    #bottom row match
    elif board[2][0] == board[2][1] == board[2][2] and board[2][2] != None:
        return board[2][0]
    #left col match
    elif board[0][0] == board[1][0] == board[2][0] and board[2][0] != None:
        return board[0][0]
    #mid col match
    elif board[0][1] == board[1][1] == board[2][1] and board[2][1] != None:
        return board[0][1]
    #right col match
    elif board[0][2] == board[1][2] == board[2][2] and board[2][2] != None:
        return board[0][2]
    #diag top left -> bottom right
    elif board[0][0] == board[1][1] == board[2][2] and board[2][2] != None:
        return board[0][0]
    #diag top right -> bottom left
    elif board[0][2] == board[1][1] == board[2][0] and board[2][0] != None:
        return board[0][2]
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #if all spaces are used or there isn't a winner, return None
    if board[0].count(None) + board[1].count(None) + board[2].count(None) == 0 or winner(board) != None:
        return True
    #else return False
    else:
        return False

def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def max_value(board):
    if terminal(board):
        return score(board)
    v = float("-inf")

    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v

def min_value(board):
    if terminal(board):
            return score(board)
    v = float('inf')

    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    else:
        #get set of possible moves
        moves = actions(board)
        
        #if player == X, then use max_value function
        if player(board) == X:
            #best value is set really low to accept first candidate
            best_value = float('-inf')
            #best move is set to None
            best_move = None
            #loop thru moves and if value obtained is more than current best, update current best
            #and update best move to that move
            for move in moves:
                value = max_value(result(board, move))
                if value > best_value:
                    best_move = move
                    best_value = value
            return best_move
            
        #if player == O, then use min_value
        else:
            #best value is set really high to accept first candidate
            best_value = float('inf')
            #best move is set to None
            best_move = None
            #loop thru moves and if value is less than current best, update current best
            #and update best move to that move
            for move in moves:
                value = min_value(result(board, move))
                if value < best_value:
                    best_move = move
                    best_value = value
            return best_move
            

#x win = 1
#o win = -1