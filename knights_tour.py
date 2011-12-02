from tour_utils import *
from board_utils import *
import sys
import pdb
"""
Do a knights tour with an NxN board.
"""
def knights_tour( n, initial_move ):
    board = [ [0]*n for i in range(n) ]
    init_board( board, n )
    board[initial_move[0]][initial_move[1]] = 0
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
    # Remember where we are.
    solution.append( best )
    # Recurse.
    do_knights_tour( solution, best, board, n )



if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "Usage: python knights_tour.py n i j"
        print "n = board size (n by n)"
        print "i j = Initial move in the ith jth index"
        sys.exit(0)
    n = int(sys.argv[1])
    initial_move = (int(sys.argv[2]),int(sys.argv[3]))
    board = [ [0]*n for i in range(n) ]
    #print best_move( (1,2), board, n)
    sol = [initial_move]+knights_tour(n,initial_move )
    #pdb.set_trace()
    print "Board solution"
    solution_to_board(sol, board, n)
    mark_last_move( board, n, sol[-1])
    pb(board , n)
    if len(sol) == (n*n - 1):
        sys.exit(0)
    else:
        sys.exit(1)

