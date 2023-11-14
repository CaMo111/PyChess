import sys
import math
from abc import ABC, abstractmethod
import os 
import csv
from colorama import Fore, Back, Style
#========================================================================================================================================================================
#
#                               Board Initilisation
#
#========================================================================================================================================================================

final_board = [[],[],[],[],[],[],[],[]]

def board_initilisation():
	board = [[0,1,0,1,0,1,0,1],
	[1,0,1,0,1,0,1,0], 
	[0,1,0,1,0,1,0,1], 
	[1,0,1,0,1,0,1,0], 
	[0,1,0,1,0,1,0,1], 
	[1,0,1,0,1,0,1,0], 
	[0,1,0,1,0,1,0,1], 
	[1,0,1,0,1,0,1,0]]
	return board

def board_initilisation2():
	#let first decimal value 1 or 2 indicate player 1 or player 2 
	#let second decimal value eqaute to the piece, 1 for pawn, 2 for knight, 3 for bishop, 4 for rook, 5 for queen, 6 for king. 
	piece_board = [[24,22,23,25,26,23,22,24], 
	[21,21,21,21,21,21,21,21], 
	[0,0,0,0,0,0,0,0], 
	[0,0,0,0,0,0,0,0], 
	[0,0,0,0,0,0,0,0], 
	[0,0,0,0,0,0,0,0], 
	[11,11,11,11,11,11,11,11], 
	[14,12,13,15,16,13,12,14]]
	return piece_board

blue_pieces = [] 

def print_board(board, piece_board, piece_dictionary):
	black_space = Back.BLACK
	white_space = Back.WHITE
	blue_piece = Fore.BLUE
	red_piece = Fore.RED
	king_piece = Fore.YELLOW
	for i in range(0,8):
		for j in range(0,8):
			#check if the piece we are looking at is blue
			if piece_board[i][j] // 10 == 1:
				if board[i][j] == 0:
					final_board[i].append(white_space + blue_piece + piece_dictionary[piece_board[i][j]])
				else:
					final_board[i].append(black_space + blue_piece + piece_dictionary[piece_board[i][j]])
			#check if the piece we are looking at is red        
			elif piece_board[i][j] // 10 == 2:
				if board[i][j] == 0:
					final_board[i].append(white_space + red_piece + piece_dictionary[piece_board[i][j]])
				else:
					final_board[i].append(black_space + red_piece + piece_dictionary[piece_board[i][j]])
			#the only other option is for the piece to be empty                 
			else:
				if board[i][j] == 0:
					final_board[i].append(white_space + piece_dictionary[0])
				else:
					final_board[i].append(black_space + piece_dictionary[0])
	for row in range (0,8):
		row_number = [8,7,6,5,4,3,2,1]
		glue = ""
		finalrow = glue.join(final_board[row])
		print(Back.WHITE + Fore.BLACK + str(row_number[row]), finalrow)
	print(Fore.BLACK +"   a",Fore.BLACK +" b",Fore.BLACK +" c",Fore.BLACK +" d",Fore.BLACK +" e",Fore.BLACK +" f",Fore.BLACK +" g",Fore.BLACK +" h ")

piece_dictionary = {
	0 : "   ",
	11 : " P ",		
	12 : " K ",
	13 : " B ",
	14 : " R ",
	15 : " Q ",
	16 : " K ",
	
	21 : " P ",
	22 : " K ",
	23 : " B ",
	24 : " R ",
	25 : " Q ",
	26 : " K "
}


#========================================================================================================================================================================
#
#                               PIECE CLASS CREATION
#
#========================================================================================================================================================================


class piece(ABC):

    def initial_pos(self, starting_pos):
	    # getting x and y to put it into the board
	    for num in range(1, 9):
	        if num == starting_pos[1]:
                 y = (num-1) 
				 
		letters = ["a","b","c","d","e","f","g","h"]
			
	    for characters in letters:
		    if characters == starting_pos[0]:
		         x = characters.index()
        

    @abstractmethod
    
    def movement(self, departure, arrival):
	    pass
        
    @abstractmethod
    
    def valid_movements(self):
	    pass
    
    @abstractmethod
    
    def __str__(self) -> str:
        pass
        
class pawn(piece):
	
    def __init__(self, departure, arrival):
        self.value = 1

    def movement(self, departure, arrival):
	    pass

    def valid_movements(self):
        valid_movements = [] 

#========================================================================================================================================================================
#
#                               Game Navigation
#
#========================================================================================================================================================================


board = board_initilisation()
piece_board = board_initilisation2()
print_board(board, piece_board, piece_dictionary)
print(final_board[0][0])

