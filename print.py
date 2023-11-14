#from piece import piece, r_pawn, r_queen, r_king, r_rook, b_pawn, r_knight, r_bishop, b_bishop, b_knight, b_king, b_queen, b_rook
import sys
import math
from abc import ABC, abstractmethod
import os 
import csv
from colorama import Fore, Back, Style
class piece(ABC):

	@abstractmethod
	def __init__(self) -> None:
		pass

	@abstractmethod
	def valid_movement(self) -> None:
		pass	

#
#RED PIECES
#    
class r_queen(piece):
	def __init__(self):
			self.value = 9
			self.trans = 25
		
	def valid_movement(self):
		valid_movements=[]
    
class r_rook(piece):
	def __init__(self, pos):
		self.pos = pos
		self.value = 3
		self.trans = 24
		self.valid_movements=[]
        
	def valid_movement(self):
		'''
		For left_squares and up_squares the list is regenerated when seeing same team as there would be more empty positions to check
		for right_squares and down_squares function calls break to stop for loop as seeing same team would mean no more positions to traverse
		'''
		left_vals = []
		right_vals = []
		down_vals = []
		up_vals = []
		#moving leftwards into rook appending valid movements

		for left_squares in range(self.pos[1]):
			if isinstance(piece_board[self.pos[0]][left_squares], piece):
				#if its same team destroy all current
				if piece_board[self.pos[0]][left_squares].trans // 10 == 2:
					left_vals = []
				else:
					#still reset as can't move through the piece but reset and add everything else
					left_vals = []
					left_vals.append((self.pos[0],left_squares))
			#empty position means add
			else:
				left_vals.append((self.pos[0],left_squares))

		for right_squares in range(self.pos[1]+1, 8):
			if isinstance(piece_board[self.pos[0]][right_squares], piece):
				if piece_board[self.pos[0]][right_squares].trans // 10 == 2:
					break
				else:
					right_vals.append((self.pos[0],right_squares))
					break
			else:
				right_vals.append((self.pos[0],right_squares))
				#right_vals.append(piece_board[self.pos[0]][right_squares])

		#for all squares starting downwards 1 beneath the rook
		for down_squares in range(((self.pos[0]+1)), 8):
			#if we come across a piece
			if isinstance(piece_board[down_squares][self.pos[1]], piece):
				if piece_board[down_squares][self.pos[1]].trans // 10 == 2:
					break
				else:
					down_vals.append((down_squares, self.pos[1]))
					break
			else:
				down_vals.append((down_squares, self.pos[1]))
		#moving from top to where rook is 
		for up_squares in range(0, self.pos[0]):
			if isinstance(piece_board[up_squares][self.pos[1]], piece):
				if piece_board[up_squares][self.pos[1]].trans // 10 == 2:
					up_vals = []
				else:
					up_vals = []
					up_vals.append((up_squares, self.pos[1]))
			else:
				up_vals.append((up_squares, self.pos[1]))

		self.valid_movements = left_vals + right_vals + down_vals + up_vals
		
class r_king(piece):
	def __init__(self):
		self.value = 10
		self.trans = 26
	
	def valid_movement(self):
		valid_movements=[]
        
class r_knight(piece):
	def __init__(self):
		self.value = 5
		self.trans = 22
	
	def valid_movement(self):
		valid_movements=[]

class r_bishop(piece):
	def __init__(self):
		self.value = 5
		self.trans = 23
	
	def valid_movement(self):
		valid_movements=[]

class r_pawn(piece):

	def __init__(self, pos:(int, int)):
		self.value = 1
		self.trans = 21
		#self.pos example is (1,0) for a7
		self.pos = pos 
		self.initial = True
		self.valid_movements=[]

	def valid_movement(self):
		self.valid_movements=[]
		if self.initial == True:
			#if pieceboard at self.pos[0]+1, self.pos[1] is empty then add, if not dont add
			if not(isinstance(piece_board[self.pos[0]+1][self.pos[1]],piece)):
				self.valid_movements.append((self.pos[0]+1, self.pos[1]))
			if not(isinstance(piece_board[self.pos[0]+2][self.pos[1]],piece)):
				self.valid_movements.append((self.pos[0]+2, self.pos[1]))
			self.initial = False
		else:
			if not(isinstance(piece_board[self.pos[0]+1][self.pos[1]],piece)):
				self.valid_movements=[(self.pos[0]+1, self.pos[1])]
		#If there is a piece diagonal down one RIGHT and its not same team

		if isinstance(piece_board[self.pos[0]+1][self.pos[1]+1], piece):
			#not equal as we want to make sure its not red
			if piece_board[self.pos[0]+1][self.pos[1]+1].trans // 10 != 2:
				self.valid_movements.append((self.pos[0]+1,self.pos[1]+1))
		# if 
		if isinstance(piece_board[self.pos[0]+1][self.pos[1]-1], piece):
			#if its opposite team
			if piece_board[self.pos[0]+1][self.pos[1]+1].trans // 10 == 2:
				self.valid_movements.append((self.pos[0]+1,self.pos[1]-1))
#
#BLUE PIECES
#   

class b_queen(piece):
	def __init__(self):
			self.value = 9
			self.trans = 15
		
	def valid_movement(self):
		valid_movements=[]
    
class b_rook(piece):

	def __init__(self, pos: (int,int)):
			self.pos = pos
			self.value = 3
			self.trans = 14
			self.valid_movements=[]
        
	def valid_movement(self):
		left_vals = []
		right_vals = []
		down_vals = []
		up_vals = []
		#moving leftwards into rook appending valid movements

		for left_squares in range(self.pos[1]):
			if isinstance(piece_board[self.pos[0]][left_squares], piece):
				#if its same team destroy all current
				if piece_board[self.pos[0]][left_squares].trans // 10 == 1:
					left_vals = []
				else:
					#still reset as can't move through the piece but reset and add everything else
					left_vals = []
					left_vals.append((self.pos[0],left_squares))
			#empty position means add
			else:
				left_vals.append((self.pos[0],left_squares))

		for right_squares in range(self.pos[1]+1, 8):
			if isinstance(piece_board[self.pos[0]][right_squares], piece):
				if piece_board[self.pos[0]][right_squares].trans // 10 == 1:
					break
				else:
					right_vals.append((self.pos[0],right_squares))
					break
			else:
				right_vals.append((self.pos[0],right_squares))
				#right_vals.append(piece_board[self.pos[0]][right_squares])

		#for all squares starting downwards 1 beneath the rook
		for down_squares in range(((self.pos[0]+1)), 8):
			#if we come across a piece
			if isinstance(piece_board[down_squares][self.pos[1]], piece):
				if piece_board[down_squares][self.pos[1]].trans // 10 == 1:
					break
				else:
					down_vals.append((down_squares, self.pos[1]))
					break
			else:
				down_vals.append((down_squares, self.pos[1]))
		#moving from top to where rook is 
		for up_squares in range(0, self.pos[0]):
			if isinstance(piece_board[up_squares][self.pos[1]], piece):
				if piece_board[up_squares][self.pos[1]].trans // 10 == 1:
					up_vals = []
				else:
					up_vals = []
					up_vals.append((up_squares, self.pos[1]))
			else:
				up_vals.append((up_squares, self.pos[1]))

		self.valid_movements = left_vals + right_vals + down_vals + up_vals
		
class b_king(piece):
	def __init__(self):
		self.value = 10
		self.trans = 16

	def valid_movement(self):
		valid_movements=[]

class b_knight(piece):
	def __init__(self):
		self.value = 5
		self.trans = 12
	
	def valid_movement(self):
		valid_movements=[]

class b_bishop(piece):
    def __init__(self):
            self.value = 5
            self.trans = 13
        
    def valid_movement(self):
        valid_movements=[]

class b_pawn(piece):

	def __init__(self, pos:(int, int)):
		self.value = 1
		self.trans = 11
		self.initial = True
		valid_movements=[]
		self.pos = pos
	
	def valid_movement(self):
		self.valid_movements=[]
		if self.initial == True:
			#if pieceboard at self.pos[0]+1, self.pos[1] is empty then add, if not dont add
			if not(isinstance(piece_board[self.pos[0]-1][self.pos[1]],piece)):
				self.valid_movements.append((self.pos[0]-1, self.pos[1]))
			if not(isinstance(piece_board[self.pos[0]-2][self.pos[1]],piece)):
				self.valid_movements.append((self.pos[0]-2, self.pos[1]))
			self.initial = False
		else:
			if not(isinstance(piece_board[self.pos[0]-1][self.pos[1]],piece)):
				self.valid_movements=[(self.pos[0]-1, self.pos[1])]
		#If there is a piece diagonal down one RIGHT and its not same team

		if isinstance(piece_board[self.pos[0]-1][self.pos[1]+1], piece):
			#if its opposite team
			if piece_board[self.pos[0]-1][self.pos[1]+1].trans // 10 == 2:
				self.valid_movements.append((self.pos[0]-1,self.pos[1]+1))
		# if 
		if isinstance(piece_board[self.pos[0]-1][self.pos[1]-1], piece):
			#if its opposite team
			if piece_board[self.pos[0]-1][self.pos[1]-1].trans // 10 == 2:
				self.valid_movements.append((self.pos[0]-1,self.pos[1]-1))

#========================================================================================================================================================================
#
#                               Board Initilisation
#
#========================================================================================================================================================================

final_board = [[],[],[],[],[],[],[],[]]

	#def board_initilisation():
board = [[0,1,0,1,0,1,0,1],
[1,0,1,0,1,0,1,0], 
[0,1,0,1,0,1,0,1], 
[1,0,1,0,1,0,1,0], 
[0,1,0,1,0,1,0,1], 
[1,0,1,0,1,0,1,0], 
[0,1,0,1,0,1,0,1], 
[1,0,1,0,1,0,1,0]]

piece_board = [[r_rook((0,0)),r_knight(),r_bishop(),r_queen(),r_king(),r_bishop(),r_knight(),r_rook((0,7))], 
[r_pawn((1,0)),r_pawn((1,1)),r_pawn((1,2)),r_pawn((1,3)),r_pawn((1,4)),r_pawn((1,5)),r_pawn((1,6)),r_pawn((1,7))], 
[0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0], 
[b_pawn((6,0)),b_pawn((6,1)),b_pawn((6,2)),b_pawn((6,3)),b_pawn((6,4)),b_pawn((6,5)),b_pawn((6,6)),b_pawn((6,7))], 
[b_rook((7,0)),b_knight(),b_bishop(),b_queen(),b_king(),b_bishop(),b_knight(),b_rook((7,7))]]

def print_board(board, piece_board, piece_dictionary):
	#os.system('cls')
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
		#update the valid coordinate to move onto
		moving_piece.valid_movement()
		#if where we are moving to is valid
		if pos_system[to] in moving_piece.valid_movements:
			#if there is nothing where we are going
			if not(isinstance(piece_board[pos_system[to][0]][pos_system[to][1]], piece)):
				print("called1")
				moving_piece.pos = (pos_system[to][0], pos_system[to][1])
				#make old pieceboard piece nothing
				piece_board[pos_system[dep][0]][pos_system[dep][1]] = 0
				#make new pieceboard position new piece
				piece_board[pos_system[to][0]][pos_system[to][1]] = moving_piece
			else:
				print("called2")
				#There is something where we are moving and have to replace it
				piece_board[pos_system[to][0]][pos_system[to][1]] = 0
				moving_piece.pos = (pos_system[to][0], pos_system[to][1])
				#make old pieceboard piece nothing
				piece_board[pos_system[dep][0]][pos_system[dep][1]] = 0
				#make new pieceboard position new piece
				piece_board[pos_system[to][0]][pos_system[to][1]] = moving_piece
		else:
			print("Moving to a position that you cant move to")
			raise ValueError
	else:
		print("There is no piece selected")
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

def gen_game():
	game_over=False
	while not game_over:
		print_board(board, piece_board, piece_dictionary)
		fro, to = str(input("where from")), str(input("where to"))
		make_movement(fro, to)


	


#========================================================================================================================================================================
#
#                               PIECE CLASS CREATION
#
#========================================================================================================================================================================
#2 = red
#1 = blue
gen_game()

#have to update the piece board each time to print