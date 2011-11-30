from tour_utils import *
from board_utils import *
import pdb
"""
Do a knights tour with an NxN board.
"""
def knights_tour( n, initial_move ):
    board = [ [0]*n for i in range(n) ]
    init_board( board, n )
    solution = []
    do_knights_tour( solution, initial_move, board, n )
    return solution

"""
solution: accumulated solution.
index: where the knight currently is.
board: an nXn board with correct values.
n: size of board.
"""
def do_knights_tour( solution, index, board, n ):
    # Choose the best move.
    best = best_move( index, board, n )
    if not best:
        return
    # Move there.
    make_move( best, board, n )
    pb(board, n)
    # Remember where we are.
    solution.append( best )
    # Recurse.
    do_knights_tour( solution, best, board, n )



if __name__ == "__main__":
    n = 4
    board = [ [0]*n for i in range(n) ]
    pb(init_board( board, n ),n)
    #print best_move( (1,2), board, n)
    print knights_tour(n, (0,0))

