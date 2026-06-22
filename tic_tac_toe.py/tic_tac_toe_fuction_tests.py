import unittest

from tic_tac_toe_functions import *

class TestTicTacToeFunctions(unittest.TestCase):

    def test_the_board_was_created_with_adequate_length(self):
        self.assertEqual(len(create_board()), 3)
        
#if __name__ ="__main__":
#    unittest.main()
