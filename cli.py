# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

# from logic import make_empty_board

#Using other functions from logic file, hence importing the entire file
import logic


if __name__ == "__main__":
    board = logic.make_empty_board()
    winner = None
    count = 9

    #Asking the user for starting character 
    ans =  input('Enter the first players characher(X or O)')
    flag = 1
    while flag == 1 :
        if ans == 'X' or ans == 'O':
            flag = 0                #Sanity check: Taking X or O only as input
        else:
            ans =  input('Please enter X or O')
    #Not considering x or o, only considering the X or O

    while winner == None:
        # TODO: Show the board to the user.
        # TODO: Input a move from the player.
        # TODO: Update the board.
        # TODO: Update who's turn it is.

        #Printing the board
        print('********************************')
        for i in range(3):
            for j in range(3):
                print(board[i][j], end=" ")
            print()
        print('Current turn: ' + ans)


        #Taking input indexes from user
        index_i = int(input("Enter x axis on board"))
        index_j = int(input("Enter y axis on board"))

        #Sanity checks on indexes
        #Making sure not to rewrite used indexes
        if index_i < 0 or index_j < 0 or index_i > 2 or index_j > 2:
            print("Enter valid index")
            continue
        elif board[index_i][index_j] == None:
            board[index_i][index_j] = ans
        elif board[index_i][index_j] != None:
            print("Select an index not already chosen")
            continue

        #Updating index and checking winner
        winner = logic.get_winner(board)
        if winner != None:
            for i in range(3):
                for j in range(3):
                    print(board[i][j], end=" ")
                print()
            print("And the winner is " + winner)
            quit()

        #Calling the next player
        ans = logic.other_player(ans)

        #If the board is full with no clear winner, it's a draw
        count  -= 1
        if count == 0:
            print("Its a draw")
            break
