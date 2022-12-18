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


import logic
import random
import csv
import shutil
from tempfile import NamedTemporaryFile
import os
import numpy as np
import pandas as pd


def print_board(board, ans):
    #self.board = board
    #self.ans = ans
    print('********************************')
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()

#@staticmethod    
def input_indexes(ans,bot):
    #self.ans = ans
    #self.bot = bot
    if(ans != bot):
        index_i = int(input("Enter x axis on board"))
        index_j = int(input("Enter y axis on board"))
    else:
        index_i = random.randint(0,2)
        index_j = random.randint(0,2)
    return index_i, index_j


#@staticmethod
def checking_validity(board, index_i, index_j, ans, bot):
    #self.index_i = index_i
    #self.index_j = index_j
    #self.ans = ans
    #self.bot = bot
    if index_i < 0 or index_j < 0 or index_i > 2 or index_j > 2:
            print("Enter valid index")
            return False
    elif board[index_i][index_j] != None:
            if (ans != bot):
                print("Select an index not already chosen")
            return False
    elif board[index_i][index_j] == None:
        #board[index_i][index_j] = ans
        return True
    return False


#@staticmethod
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

#@staticmethod
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


#@staticmethod
def ret_bytes(file_path):
    with open(file_path, "a") as csvfile:
        if int(os.stat(file_path).st_size) == 0:
            return True
        else:
            return False
    return None


#append_data("data.csv", "Justin", "hello@teamcfe.com", 123.22)

#staticmethod
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


#@staticmethod
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



