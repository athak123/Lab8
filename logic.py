# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    
    #Checking horizontal and vertical wins
    for i in range(3):
        temp1 = 0
        temp2 = 0
        for j in range(3):
            if board[i][j] == 'O':
                temp1 += 1
            elif board[i][j] == 'X':
                temp1 -= 1
            if board[j][i] == 'O':
                temp2 += 1
            elif board[j][i] == 'X':
                temp2 -= 1
        if temp1 == 3 or temp2 == 3:
            return 'O'
        if temp1 == -3 or temp2 == -3:
            return 'X'

    #Checking diagonal wins
    if board[1][1] == 'X':
        if (board[0][0] == 'X' and board[2][2] == 'X') or (board[0][2] == 'X' and board[2][0] == 'X'):
            return 'X'
    if board[1][1] == 'O':
        if (board[0][0] == 'O' and board[2][2] == 'O') or (board[0][2] == 'O' and board[2][0] == 'O'):
            return 'O'

    #returns nothing if there are no winners
    return None  


def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == 'X':
        return 'O'
    if player == 'O':
        return 'X'