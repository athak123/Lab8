from flask import Flask
import cli3
app = Flask(__name__)
@app.route('/')
def tic_tac_toe():
    # This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

# from logic import make_empty_board
#alabhya is the coolest oye yaaawr

#Using other functions from logic file, hence importing the entire file
import logic
import random
import csv
import shutil
from tempfile import NamedTemporaryFile
import os
import numpy as np
import pandas as pd

class modules:
    def print_board(self, board, ans):
        self.board = board
        self.ans = ans
        print('********************************')
        for i in range(3):
            for j in range(3):
                print(board[i][j], end=" ")
            print()
                
    def input_indexes(self,ans,bot):
        self.ans = ans
        self.bot = bot
        if(ans != bot):
            index_i = int(input("Enter x axis on board"))
            index_j = int(input("Enter y axis on board"))
        else:
            index_i = random.randint(0,2)
            index_j = random.randint(0,2)
        return index_i, index_j

    def checking_validity(self, index_i, index_j, ans, bot):
        self.index_i = index_i
        self.index_j = index_j
        self.ans = ans
        self.bot = bot
        if index_i < 0 or index_j < 0 or index_i > 2 or index_j > 2:
                print("Enter valid index")
                return False
        elif board[index_i][index_j] != None:
                if (ans != bot):
                    print("Select an index not already chosen")
                return False
        elif board[index_i][index_j] == None:
            return True
        return False


    @staticmethod
    def read_data(Player_Name):
        filename = "data.csv"
        with open(filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            items = []
            unknown_player_name = None
            for row in reader:
                if Player_Name is not None:
                    if Player_Name == row.get("Player_Name"):
                        return True
                    else:
                        unknown_player_name = Player_Name
            if unknown_player_name is not None:
                return False
        return None

    @staticmethod
    def append_data(file_path, Player_Name, Wins, Losses, Draws):
        fieldnames = ['Player_Name', 'Wins', 'Losses', 'Draws']
        #the number of rows?
        #next_id = modules.get_length(file_path)
        with open(file_path, "a") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            #*********Run only first time**********
            if int(os.stat(file_path).st_size) == 0:
                writer.writeheader()
            writer.writerow({
                    "Player_Name": Player_Name,
                    "Wins": Wins,
                    "Losses": Losses,
                    "Draws": Draws,
                })


    @staticmethod
    def ret_bytes(file_path):
        with open(file_path, "a") as csvfile:
            if int(os.stat(file_path).st_size) == 0:
                return True
            else:
                return False
        return None


#append_data("data.csv", "Justin", "hello@teamcfe.com", 123.22)

    @staticmethod
    def edit_data(Player_Name=None, Wins=None, Losses=None, Draws=None):
        myList = []
        filename = "data.csv"
        with open(filename, 'r') as file:
            myFile = csv.reader(file)
            for row in myFile:
                myList.append(row)

        myList = [[int(x) if x.isdigit() else x for x in lst] for lst in myList]
        A = np.array(myList)
        result = list(zip(*np.where(A == Player_Name)))
        
        if Wins == 1:
            myList[result[0][0]][1] = myList[result[0][0]][1] + 1 
        if Losses == 1:
            myList[result[0][0]][2] = myList[result[0][0]][2] + 1
        if Draws == 1:
            myList[result[0][0]][3] = myList[result[0][0]][3] + 1

        with open(filename, 'w+') as file:
            myFile = csv.writer(file)
            for i in range(len(myList)):
                myFile.writerow(myList[i])


    @staticmethod
    def print_stats(file_path):
        with open(file_path) as trfp, open("test.csv", "w+") as twfp:
            reader = csv.reader(trfp)
            writer = csv.writer(twfp)
            for row in reader:
                writer.writerow(row)
        df = pd.read_csv("test.csv")
        df.index.name = 'Index'
        df.to_csv("test.csv")
        with open("test.csv") as fp:
            reader = csv.reader(fp, delimiter=",")
            data_read = [row for row in reader]
            print(data_read)
            print()

if __name__ == "__main__":
    instance_class = modules()
    board = logic.make_empty_board()
    winner = None
    count = 9
    
    #Asking the user for starting character 
    player_count = int(input("Please enter number of players (1 or 2)"))
    flag_count = -1
    while flag_count == -1:
        if player_count == 1 or player_count == 2:
            flag_count = 0
        else:
            player_count = int(input("Please enter 1 or 2"))

    name1 = input("Enter name of player 1")
    if(player_count == 2):
        name2 = input("Enter name of player 2")
    else:
        name2 = "Bot"


    ans =  input('Enter the first players characher(X or O)')
    
    flag = 1
    while flag == 1 :
        if ans == 'X' or ans == 'O':
            flag = 0                #Sanity check: Taking X or O only as input
        else:
            ans =  input('Please enter X or O')

    first_player = ans
    #Not considering x or o, only considering the X or O

    if(player_count == 1):
        bot = logic.other_player(ans)
    else:
        bot = None

    instance_class.print_board(board, ans)

    #*******Run this the first time only***********
    if instance_class.ret_bytes("data.csv")== True:
        instance_class.append_data("data.csv", "Bot", 0, 0, 0)


    while winner == None:
        # TODO: Show the board to the user.
        # TODO: Input a move from the player.
        # TODO: Update the board.
        # TODO: Update who's turn it is.

        #Printing the board

        #Taking input indexes from user
        result = instance_class.input_indexes(ans, bot)
        
        #Sanity checks on indexes
        #Making sure not to rewrite used indexes

        index_i, index_j = result
        ans_check = instance_class.checking_validity(index_i, index_j, ans, bot)
        if(ans_check == False):
            continue
        board[index_i][index_j] = ans

        instance_class.print_board(board, ans)
        
        #Updating index and checking winner
        winner = logic.get_winner(board)
        if winner != None:
            if winner == first_player:
                if instance_class.read_data(name1) == True:
                    instance_class.edit_data(name1, 1, 0, 0)
                elif instance_class.read_data(name1) == False:
                    instance_class.append_data("data.csv", name1, 1, 0, 0)
                if instance_class.read_data(name2) == True:
                    instance_class.edit_data(name2, 0, 1, 0)
                elif instance_class.read_data(name2) == False:
                    instance_class.append_data("data.csv", name2, 0, 1, 0)
            else:
                if instance_class.read_data(name2) == True:
                    instance_class.edit_data(name2, 1, 0, 0)
                elif instance_class.read_data(name2) == False:
                    instance_class.append_data("data.csv", name2, 1, 0, 0)
                if instance_class.read_data(name1) == True:
                    instance_class.edit_data(name1, 0, 1, 0)
                elif instance_class.read_data(name1) == False:
                    instance_class.append_data("data.csv", name1, 0, 1, 0)
            instance_class.print_board(board, ans)
            print("And the winner is " + winner)
            instance_class.print_stats("data.csv")
            quit()

        #Calling the next player
        ans = logic.other_player(ans)
        print('Current turn: ' + ans)
        

        #If the board is full with no clear winner, it's a draw
        count  -= 1
        if count == 0:
            if instance_class.read_data(name1) == True:
                instance_class.edit_data(name1, 0, 0, 1)
            elif instance_class.read_data(name1) == False:
                instance_class.append_data("data.csv", name1, 0, 0, 1)
            if instance_class.read_data(name2) == True:
                instance_class.edit_data(name2, 0, 0, 1)
            elif instance_class.read_data(name2) == False:
                instance_class.append_data("data.csv", name1, 0, 0, 1)
            instance_class.print_board(board, ans)
            print("Its a draw")
            instance_class.print_stats("data.csv")
            break

    
            return 'Tic-Tac-Toe game goes here'

