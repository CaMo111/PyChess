from piece import piece, r_pawn, r_queen, r_king, r_rook, b_pawn, r_knight, r_bishop, b_bishop, b_knight, b_king, b_queen, b_rook
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
	piece_board = [[r_rook(),r_knight(),r_bishop(),r_queen(),r_king(),r_bishop(),r_knight(),r_rook()], 
	[r_pawn(),r_pawn(),r_pawn(),r_pawn(),r_pawn(),r_pawn(),r_pawn(),r_pawn()], 
	[0,0,0,0,0,0,0,0], 
	[0,0,0,0,0,0,0,0], 
	[0,0,0,0,0,0,0,0], 
	[0,0,0,0,0,0,0,0], 
	[b_pawn(),b_pawn(),b_pawn(),b_pawn(),b_pawn(),b_pawn(),b_pawn(),b_pawn()], 
	[b_rook(),b_knight(),b_bishop(),b_queen(),b_king(),b_bishop(),b_knight(),b_rook()]]
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
			if isinstance(piece_board[i][j], piece):
			#check if the piece we are looking at is blue
				if piece_board[i][j].trans // 10 == 1:
					if board[i][j] == 0:
						final_board[i].append(white_space + blue_piece + piece_dictionary[piece_board[i][j].trans])
					else:
						final_board[i].append(black_space + blue_piece + piece_dictionary[piece_board[i][j].trans])
				#check if the piece we are looking at is red        
				elif piece_board[i][j].trans // 10 == 2:
					if board[i][j] == 0:
						final_board[i].append(white_space + red_piece + piece_dictionary[piece_board[i][j].trans])
					else:
						final_board[i].append(black_space + red_piece + piece_dictionary[piece_board[i][j].trans])
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

def make_movement(piece):
	pass

piece_dictionary = {
	0 : "   ",
	11 : " ♟︎ ",		
	12 : " ♞ ",
	13 : " ♝ ",
	14 : " ♜ ",
	15 : " ♛ ",
	16 : " ♚ ",
	
	21 : " ♟︎ ",
	22 : " ♞ ",
	23 : " ♝ ",
	24 : " ♜ ",
	25 : " ♛ ",
	26 : " ♚ "
}


#========================================================================================================================================================================
#
#                               PIECE CLASS CREATION
#
#========================================================================================================================================================================
#2 = red
#1 = blue

board = board_initilisation()
piece_board = board_initilisation2()
print_board(board, piece_board, piece_dictionary)

