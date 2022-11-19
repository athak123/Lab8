import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

        board = [
            ['O', None, 'X'],
            [None, 'O', None],
            [None, 'X', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')

        board = [
            ['O', None, 'X'],
            [None, 'X', 'X'],
            [None, 'X', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), None)

        board = [
            ['O', 'X', 'X'],
            [None, 'X', 'X'],
            [None, 'X', None],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    
    def test_other_player(self):
        self.assertEqual(logic.other_player('X'), 'O')
        self.assertEqual(logic.other_player('O'), 'X')

    # TODO: Test all functions from logic.py!


if __name__ == '__main__':
    unittest.main()