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
            continue
        elif val(possible, board) == val(best, board):
            # Tie breaker
            if abs(possible[0] - possible[1]) < abs(best[0] - best[1]):
                best = possible
            continue
        elif val(possible, board) < val(best, board):
            best = possible
        else:
            continue

    return best

"""
HACK HACK HACK.
If there is only one sqaure left that is still a zero.
1) Find it
2) Get the last known move
3) See if you can move into the last square from the last known move.
4 a) If you can mark it.
  b) If you can't don't mark it.
"""
def mark_last_move( board, n, last_known ):
    zeros = 0
    zero_location = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                zeros += 1
                zero_location = (i,j)
    if zeros != 1:
        return
    else:
        if abs( zero_location[0] - last_known[0] ) == 1 and abs( zero_location[1] - last_known[1] ) == 2:
            board[zero_location[0]][zero_location[1]] = n*n
        elif abs( zero_location[0] - last_known[0] ) == 2 and abs( zero_location[1] - last_known[1] ) == 1:
            board[zero_location[0]][zero_location[1]] = n*n
        else:
            return





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
        if board[possible[0]][possible[1]] > 0:
            board[possible[0]][possible[1]] -= 1



def init_board( board, n ):
    for i in range(n):
        for j in range(n):
            board[i][j] = calc_valid_moves( (i,j), n )
    return board

