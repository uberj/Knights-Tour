import pdb

def calc_valid_moves( index, n ):
    return len(get_all_valid_moves( index, n))

"""
Given an (i,j) index, return
the value of board at that index.
"""
def val( index, board ):
    return board[index[0]][index[1]]

"""
Given an (i,j) index, choose the lowest
degree move.
@return the (i,j) index of that val
"""
def best_move( index, board, n ):
    best = None
    for possible in get_all_valid_moves( index, n ):
        if val(possible, board) <= 0:
            # We already made a move here.
            continue
        elif best is None:
            best = possible
        elif val(possible, board) < best:
            best = possible
        else:
            continue

    return best



"""
Given a board and a (i,j) touple, calculate
all the valid moves taken from (i,j).
There should be 8 possible moves.
"""
def get_all_valid_moves( index, n ):
    moves, valid_moves = [], []
    moves.append((index[0]-2,index[1]+1))
    moves.append((index[0]-2,index[1]-1))
    moves.append((index[0]+2,index[1]+1))
    moves.append((index[0]+2,index[1]-1))

    moves.append((index[0]-1,index[1]+2))
    moves.append((index[0]-1,index[1]-2))
    moves.append((index[0]+1,index[1]+2))
    moves.append((index[0]+1,index[1]-2))
    for move in moves:
        if move[0] >= n or move[0] < 0 or \
           move[1] >= n or move[1] < 0:
            continue
        else:
            valid_moves.append(move)

    return valid_moves

def make_move( index, board, n ):
    if val( index, board) <= 0:
        print "SANITY CHECK FAILURE"
    else:
        board[index[0]][index[1]] = 0
    # Decrement all other moves that were counting this sqaure.
    for possible in get_all_valid_moves( index, n ):
        board[possible[0]][possible[1]] -= 1



def init_board( board, n ):
    for i in range(n):
        for j in range(n):
            board[i][j] = calc_valid_moves( (i,j), n )
    return board

