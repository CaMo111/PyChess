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
	[r_pawn((1,0)),r_pawn((1,1)),r_pawn((1,2)),r_pawn((1,3)),r_pawn((1,4)),r_pawn((1,5)),r_pawn((1,6)),r_pawn((1,7))], 
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
	print("\n \n \n")
	final_board = [[],[],[],[],[],[],[],[]]
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

def make_movement(dep, to):
	#if there is a piece at the dep position
	if isinstance(piece_board[pos_system[dep][0]][pos_system[dep][1]], piece):
		moving_piece = piece_board[pos_system[dep][0]][pos_system[dep][1]]
		if pos_system[to] in moving_piece.valid_movements:
			moving_piece.pos = (pos_system[to][0], pos_system[to][1])
			#make old pieceboard piece nothing
			piece_board[pos_system[dep][0]][pos_system[dep][1]] = 0
			#make new pieceboard position new piece
			piece_board[pos_system[to][0]][pos_system[to][1]] = moving_piece

			print(moving_piece.pos)
		else:
			raise ValueError
	else:
		raise ValueError


pos_system = {
	"a8" : (0,0),
	"b8" : (0,1),
	"c8" : (0,2),
	"d8" : (0,3),
	"e8" : (0,4),
	"f8" : (0,5),
	"g8" : (0,6),
	"h8" : (0,7),

	"a7" : (1,0),
	"b7" : (1,1),
	"c7" : (1,2),
	"d7" : (1,3),
	"e7" : (1,4),
	"f7" : (1,5),
	"g7" : (1,6),
	"h7" : (1,7),

	"a6" : (2,0),
	"b6" : (2,1),
	"c6" : (2,2),
	"d6" : (2,3),
	"e6" : (2,4),
	"f6" : (2,5),
	"g6" : (2,6),
	"h6" : (2,7),

	"a5" : (3,0),
	"b5" : (3,1),
	"c5" : (3,2),
	"d5" : (3,3),
	"e5" : (3,4),
	"f5" : (3,5),
	"g5" : (3,6),
	"h5" : (3,7),

	"a4" : (4,0),
	"b4" : (4,1),
	"c4" : (4,2),
	"d4" : (4,3),
	"e4" : (4,4),
	"f4" : (4,5),
	"g4" : (4,6),
	"h4" : (4,7),

	"a3" : (5,0),
	"b3" : (5,1),
	"c3" : (5,2),
	"d3" : (5,3),
	"e3" : (5,4),
	"f3" : (5,5),
	"g3" : (5,6),
	"h3" : (5,7),

	"a2" : (6,0),
	"b2" : (6,1),
	"c2" : (6,2),
	"d2" : (6,3),
	"e2" : (6,4),
	"f2" : (6,5),
	"g2" : (6,6),
	"h2" : (6,7),

	"a1" : (7,0),
	"b1" : (7,1),
	"c1" : (7,2),
	"d1" : (7,3),
	"e1" : (7,4),
	"f1" : (7,5),
	"g1" : (7,6),
	"h1" : (7,7)
}

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
make_movement("a7", "a6")
print_board(board, piece_board, piece_dictionary)
#have to update the piece board each time to print