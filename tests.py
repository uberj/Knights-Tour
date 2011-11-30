import unittest
from tour_utils import *
from board_utils import *

class TestKnightsTour(unittest.TestCase):
    def setUp(self):
        n = 5
        self.b1 = board = [ [0]*n for i in range(n) ]
        self.b1 = [[],[],[]]

    def test_calc_valid_move( self ):
        return

    def test_valid_move( self ):
        return

    def test_best_move( self ):
        return

    def test_get_all_valid_moves( self ):
        n = 6
        moves = set(get_all_valid_moves((0,0),n))
        right_moves = set([(1,2),(2,1)])
        self.assertEqual( moves, right_moves)

        moves = set(get_all_valid_moves((1,1),n))
        right_moves = set([(0,3),(3,0),(2,3),(3,2)])
        self.assertEqual( moves, right_moves)

        moves = set(get_all_valid_moves((3,2),n))
        right_moves = set([(2,0),(4,0),(4,4),(2,4),(5,1),(5,3),(1,1),(1,3)])
        self.assertEqual( moves, right_moves)

        moves = set(get_all_valid_moves((5,5),n))
        right_moves = set([(4,3),(3,4)])
        self.assertEqual( moves, right_moves)

    def test_3_get_all_valid_moves( self ):
        n = 3
        moves = set(get_all_valid_moves((2,2),n))
        right_moves = set([(1,0),(0,1)])
        self.assertEqual( moves, right_moves)

    def test_make_move( self ):
        return

    def test_init_board( self ):
        return



if __name__ == "__main__":
    unittest.main()
