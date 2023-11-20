#from piece import piece, r_pawn, r_queen, r_king, r_rook, b_pawn, r_knight, r_bishop, b_bishop, b_knight, b_king, b_queen, b_rook
import sys
import math
import copy
from abc import ABC, abstractmethod
import os 
import csv
from colorama import Fore, Back, Style
#SPECIAL CONSIDERATIONS:
#Special Move #1 Promotion
#Special Move #2 Passant - capturing pawn after moving twice
#Special Move #3 Castling
class piece(ABC):

	@abstractmethod
	def __init__(self) -> None:
		pass

	@abstractmethod
	def valid_movement(self) -> None:
		pass	

#
#test
#RED PIECES
#    
class r_queen(piece):
	def __init__(self, pos: (int,int)):
			self.pos = pos
			self.valid_movements=[]
			self.value = 9
			self.trans = 25
		
	def valid_movement(self):
		valid_movements=[]

		left_vals = []
		right_vals = []
		down_vals = []
		up_vals = []
		#ADD ROOK MOVEMENT
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
		#ADD DIAGONAL MOVEMENT
		y_co = self.pos[0]-1
		x_co = self.pos[1]-1
		#Diagonal Up-Left (y is decreasing, x is decreasing)
		for values in range(8):
			if y_co < 0 or x_co < 0 or y_co > 7 or x_co > 7:
				break
			#if we come across a piece
			if isinstance(piece_board[y_co][x_co], piece):
				if piece_board[y_co][x_co].trans // 10 == 2:
					break
				else:
					self.valid_movements.append((y_co,x_co))
					break
			else:
				self.valid_movements.append((y_co,x_co))
				y_co -=1 
				x_co -=1
		#Diagonal Up-Right (y is decreasing, x is increasing)
		#reset these
		y_co = self.pos[0]-1
		x_co = self.pos[1]+1
		for values in range(8):
			if y_co < 0 or x_co < 0 or y_co > 7 or x_co > 7:
				break
			#if we come across a piece
			if isinstance(piece_board[y_co][x_co], piece):
				if piece_board[y_co][x_co].trans // 10 == 2:
					break
				else:
					self.valid_movements.append((y_co,x_co))
					break
			else:
				self.valid_movements.append((y_co,x_co))
				y_co -=1 
				x_co +=1
		#Diagonal Down-Left (y is increasing, x is decreasing)
		y_co = self.pos[0]+1
		x_co = self.pos[1]-1
		for values in range(8):
			if y_co < 0 or x_co < 0 or y_co > 7 or x_co > 7:
				break
			#if we come across a piece
			if isinstance(piece_board[y_co][x_co], piece):
				if piece_board[y_co][x_co].trans // 10 == 2:
					break
				else:
					self.valid_movements.append((y_co,x_co))
					break
			else:
				self.valid_movements.append((y_co,x_co))
				y_co +=1 
				x_co -=1
		#Diagonal Down-Right (y is increasing, x is increasing)
		y_co = self.pos[0]+1
		x_co = self.pos[1]+1
		for values in range(8):
			if y_co < 0 or x_co < 0 or y_co > 7 or x_co > 7:
				break
			#if we come across a piece
			if isinstance(piece_board[y_co][x_co], piece):
				if piece_board[y_co][x_co].trans // 10 == 2:
					break
				else:
					self.valid_movements.append((y_co,x_co))
					break
			else:
				self.valid_movements.append((y_co,x_co))
				y_co +=1 
				x_co +=1
		

    
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
		self.valid_movements=[]
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
	def __init__(self, pos: (int,int)):
		self.value = 10
		self.pos = pos
		self.valid_movements = []
		self.trans = 26
		self.check = False
		self.check_mate = False
		self.future = False
	
	def valid_movement(self):
		self.check = False
		#can move in a sqaure anywhere around him. so append those values into a list. Then 
		#iterate over the piece board and for every enemey piece check their valid movements.
		#if there is overlap remove them from the kings valid movements
		#if valid_movement is none then game over
		#future boolean basically is false in any normal move but when true is if 
		#the check() function is predicting if a move will put the king in check
		self.invalid_moves = []
		self.valid_movements = []
		#get all invalid coordinates
		#adding every non good move
		for columns in range(8):
			for row_cells in range(8):
				if isinstance(piece_board[columns][row_cells], piece):
					if isinstance(piece_board[columns][row_cells], b_king):
						self.invalid_moves.append((columns, row_cells))
						self.invalid_moves.append((columns-1, row_cells))
						self.invalid_moves.append((columns+1, row_cells))
						self.invalid_moves.append((columns-1, row_cells-1))
						self.invalid_moves.append((columns-1, row_cells+1))
						self.invalid_moves.append((columns, row_cells-1))
						self.invalid_moves.append((columns, row_cells+1))
						self.invalid_moves.append((columns+1, row_cells-1))
						self.invalid_moves.append((columns+1, row_cells+1))

					elif isinstance(piece_board[columns][row_cells], b_pawn):
						self.invalid_moves.append((columns-1,row_cells-1))
						self.invalid_moves.append((columns-1,row_cells+1))
					else:
						if piece_board[columns][row_cells].trans // 10 != 2:
							piece_board[columns][row_cells].valid_movement()
							for coordinates in piece_board[columns][row_cells].valid_movements:
								self.invalid_moves.append(coordinates)

		for idx, i in enumerate(range(3)):
			#left around
			if idx == 1:
				y_cord = self.pos[0]-1
				x_cord = self.pos[1]-1
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 2:
						#taking a piece should only append if taking doesnt result in check
						#make check() function that returns true or false; by creating a 
						#deep copy of the board, taking the peice and seeing if check is true
						#if its true, do not append as a valid move
						#if moving doesn't result in check
						if self.future:
							if not check(piece_board, self, (y_cord,x_cord)):
								self.valid_movements.append((y_cord, x_cord))
								self.future = False
				else:
					self.valid_movements.append((y_cord, x_cord))
				#middle left one 
				y_cord = self.pos[0]
				x_cord = self.pos[1]-1
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 2:
						if self.future:
							if not check(piece_board, self, (y_cord,x_cord)):
								self.valid_movements.append((y_cord, x_cord))
								self.future = False
				else:
					self.valid_movements.append((y_cord, x_cord))
				#check 1 left down one
				y_cord = self.pos[0]+1
				x_cord = self.pos[1]-1
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 2:
						if self.future:
							if not check(piece_board, self, (y_cord,x_cord)):
								self.valid_movements.append((y_cord, x_cord))
								self.future = False
				else:
					self.valid_movements.append((y_cord, x_cord))
			#middle top bottom
			elif idx == 2:
				y_cord = self.pos[0]-1
				x_cord = self.pos[1]
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 2:
						if self.future:
							if not check(piece_board, self, (y_cord,x_cord)):
								self.valid_movements.append((y_cord, x_cord))
				else:
					self.valid_movements.append((y_cord, x_cord))
				#other
				y_cord = self.pos[0]+1
				x_cord = self.pos[1]
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 2:
						if self.future:
							if not check(piece_board, self, (y_cord,x_cord)):
								self.valid_movements.append((y_cord, x_cord))
								self.future = False
				else:
					self.valid_movements.append((y_cord, x_cord))
			#right; top middle and bottom.
			else:
				y_cord = self.pos[0]-1
				x_cord = self.pos[1]+1
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 2:
						if self.future:
							if not check(piece_board, self, (y_cord,x_cord)):
								self.valid_movements.append((y_cord, x_cord))
								self.future = False
				else:
					self.valid_movements.append((y_cord, x_cord))
				#middle left one 
				y_cord = self.pos[0]
				x_cord = self.pos[1]+1
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 2:
						if self.future:
							if not check(piece_board, self, (y_cord,x_cord)):
								self.valid_movements.append((y_cord, x_cord))
								self.future = False
				else:
					self.valid_movements.append((y_cord, x_cord))
				#check 1 left down one
				y_cord = self.pos[0]+1
				x_cord = self.pos[1]+1
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 2:
						if self.future:
							if not check(piece_board, self, (y_cord,x_cord)):
								self.valid_movements.append((y_cord, x_cord))
								self.future = False
				else:
					self.valid_movements.append((y_cord, x_cord))

		#get rid of kings movements that are invalid
		#eg cant move into a check position.
		for unchecked in self.invalid_moves:
			if unchecked == self.pos:
				self.check = True
			if unchecked in self.valid_movements:
				self.valid_movements.remove(unchecked)
		
		if len(self.valid_movements) == 0:
			if self.check == True:
				self.check_mate = True


        
class r_knight(piece):
	def __init__(self, pos: (int,int)):
		self.value = 5
		self.pos = pos
		self.trans = 22
		self.valid_movements=[]
	
	def valid_movement(self):
		valid_movements=[]
		for idx, values in enumerate(range(4)):
			if idx == 0:
				#check far left up 1 eg y-1, x-2
				if (self.pos[0]-1) < 0 or (self.pos[1]-2) < 0 or (self.pos[0]-1) >7 or (self.pos[1]-2) >7:
					pass
				elif isinstance(piece_board[self.pos[0]-1][self.pos[1]-2], piece):
					if piece_board[self.pos[0]-1][self.pos[1]-2].trans // 10 != 2:
						self.valid_movements.append((self.pos[0]-1, self.pos[1]-2))
				else:
					self.valid_movements.append((self.pos[0]-1, self.pos[1]-2))
				
				#check far left down 1; eg y+1 x-2
				if (self.pos[0]+1) < 0 or (self.pos[1]-2) < 0 or (self.pos[0]+1) >7 or (self.pos[1]-2) >7:
					pass
				elif isinstance(piece_board[self.pos[0]+1][self.pos[1]-2], piece):
					if piece_board[self.pos[0]+1][self.pos[1]-2].trans // 10 != 2:
						self.valid_movements.append((self.pos[0]+1, self.pos[1]-2))
				else:
					self.valid_movements.append((self.pos[0]+1, self.pos[1]-2))

			elif idx == 1:
				#check 1 left up two
				y_cord = self.pos[0]-2
				x_cord = self.pos[1]-1
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 2:
						self.valid_movements.append((y_cord, x_cord))
				else:
					self.valid_movements.append((y_cord, x_cord))
				#check 1 left down two
				y_cord = self.pos[0]+2
				x_cord = self.pos[1]-1
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 2:
						self.valid_movements.append((y_cord, x_cord))
				else:
					self.valid_movements.append((y_cord, x_cord))

			elif idx == 2:
				#check right up two
				y_cord = self.pos[0]-2
				x_cord = self.pos[1]+1
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 2:
						self.valid_movements.append((y_cord, x_cord))
				else:
					self.valid_movements.append((y_cord, x_cord))
				#check right down two
				y_cord = self.pos[0]+2
				x_cord = self.pos[1]+1
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 2:
						self.valid_movements.append((y_cord, x_cord))
				else:
					self.valid_movements.append((y_cord, x_cord))
			else:
				#check far right up 1 
				y_cord = self.pos[0]-1
				x_cord = self.pos[1]+2
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 2:
						self.valid_movements.append((y_cord, x_cord))
				else:
					self.valid_movements.append((y_cord, x_cord))
				#check far right down 1 
				y_cord = self.pos[0]+1
				x_cord = self.pos[1]+2
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 2:
						self.valid_movements.append((y_cord, x_cord))
				else:
					self.valid_movements.append((y_cord, x_cord))

class r_bishop(piece):
	def __init__(self, pos: (int,int)):
		self.pos = pos
		self.value = 3
		self.trans = 23
		self.valid_movements=[]
	
	def valid_movement(self):
		#create a function that ensures that depart isn't the same as to
		valid_movements=[]
		y_co = self.pos[0]-1
		x_co = self.pos[1]-1
		#Diagonal Up-Left (y is decreasing, x is decreasing)
		for values in range(8):
			if y_co < 0 or x_co < 0 or y_co > 7 or x_co > 7:
				break
			#if we come across a piece
			if isinstance(piece_board[y_co][x_co], piece):
				if piece_board[y_co][x_co].trans // 10 == 2:
					break
				else:
					self.valid_movements.append((y_co,x_co))
					break
			else:
				self.valid_movements.append((y_co,x_co))
				y_co -=1 
				x_co -=1
		#Diagonal Up-Right (y is decreasing, x is increasing)
		#reset these
		y_co = self.pos[0]-1
		x_co = self.pos[1]+1
		for values in range(8):
			if y_co < 0 or x_co < 0 or y_co > 7 or x_co > 7:
				break
			#if we come across a piece
			if isinstance(piece_board[y_co][x_co], piece):
				if piece_board[y_co][x_co].trans // 10 == 2:
					break
				else:
					self.valid_movements.append((y_co,x_co))
					break
			else:
				self.valid_movements.append((y_co,x_co))
				y_co -=1 
				x_co +=1
		#Diagonal Down-Left (y is increasing, x is decreasing)
		y_co = self.pos[0]+1
		x_co = self.pos[1]-1
		for values in range(8):
			if y_co < 0 or x_co < 0 or y_co > 7 or x_co > 7:
				break
			#if we come across a piece
			if isinstance(piece_board[y_co][x_co], piece):
				if piece_board[y_co][x_co].trans // 10 == 2:
					break
				else:
					self.valid_movements.append((y_co,x_co))
					break
			else:
				self.valid_movements.append((y_co,x_co))
				y_co +=1 
				x_co -=1
		#Diagonal Down-Right (y is increasing, x is increasing)
		y_co = self.pos[0]+1
		x_co = self.pos[1]+1
		for values in range(8):
			if y_co < 0 or x_co < 0 or y_co > 7 or x_co > 7:
				break
			#if we come across a piece
			if isinstance(piece_board[y_co][x_co], piece): 
				if piece_board[y_co][x_co].trans // 10 == 2:
					break
				else:
					self.valid_movements.append((y_co,x_co))
					break
			else:
				self.valid_movements.append((y_co,x_co))
				y_co +=1 
				x_co +=1


class r_pawn(piece):

	def __init__(self, pos:(int, int)):
		self.value = 1
		self.trans = 21
		#self.pos example is (1,0) for a7
		self.pos = pos 
		self.initial = True
		self.valid_movements=[]
		self.king_invalid = []

	def valid_movement(self):
		self.valid_movements=[]
		self.king_invalid = []
		if self.initial == True:
			#if pieceboard at self.pos[0]+1, self.pos[1] is empty then add, if not dont add
			if self.pos[0]+1 > 0 and self.pos[0]+1 < 8:
				if not(isinstance(piece_board[self.pos[0]+1][self.pos[1]],piece)):
					self.valid_movements.append((self.pos[0]+1, self.pos[1]))

			if self.pos[0]+2 > 0 and self.pos[0]+2 < 8:
				if not(isinstance(piece_board[self.pos[0]+2][self.pos[1]],piece)):
					self.valid_movements.append((self.pos[0]+2, self.pos[1]))

			self.initial = False
		else:
			if not(isinstance(piece_board[self.pos[0]+1][self.pos[1]],piece)):
				self.valid_movements=[(self.pos[0]+1, self.pos[1])]
		#If there is a piece diagonal down one RIGHT and its not same team

		#Append diagonals into possible moves
		if (self.pos[0]+1) < 0 or self.pos[1]+1 < 0 or (self.pos[0]+1) >7 or self.pos[1]+1 >7:
			pass
		elif isinstance(piece_board[self.pos[0]+1][self.pos[1]+1], piece):
			#not equal as we want to make sure its not red
			if piece_board[self.pos[0]+1][self.pos[1]+1].trans // 10 != 2:
				self.valid_movements.append((self.pos[0]+1,self.pos[1]+1))
				self.king_invalid.append((self.pos[0]+1,self.pos[1]+1))
		else:
			self.king_invalid.append((self.pos[0]+1,self.pos[1]+1))

		if (self.pos[0]+1) < 0 or self.pos[1]+1 < 0 or (self.pos[0]+1) >7 or self.pos[1]+1 >7:
			pass
		elif isinstance(piece_board[self.pos[0]+1][self.pos[1]-1], piece):
			#if its opposite team
			if piece_board[self.pos[0]+1][self.pos[1]+1].trans // 10 == 2:
				self.king_invalid.append((self.pos[0]-1,self.pos[1]-1))
				self.valid_movements.append((self.pos[0]+1,self.pos[1]-1))
		else:
			self.king_invalid.append((self.pos[0]+1,self.pos[1]+1))
#
#BLUE PIECES
#   

class b_queen(piece):
	def __init__(self, pos:(int,int)):
			self.value = 9
			self.pos = pos
			self.valid_movements = []
			self.trans = 15
		
	def valid_movement(self):
		self.valid_movements = []
		left_vals = []
		right_vals = []
		down_vals = []
		up_vals = []
		#ADD ROOK MOVEMENT
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
		#ADD DIAGONAL MOVEMENT
		#create a function that takes y_co and x_co and adds to a list
		y_co = self.pos[0]-1
		x_co = self.pos[1]-1
		#Diagonal Up-Left (y is decreasing, x is decreasing)
		for values in range(8):
			if y_co < 0 or x_co < 0 or y_co > 7 or x_co > 7:
				break
			#if we come across a piece
			if isinstance(piece_board[y_co][x_co], piece):
				if piece_board[y_co][x_co].trans // 10 == 1:
					break
				else:
					self.valid_movements.append((y_co,x_co))
					break
			else:
				self.valid_movements.append((y_co,x_co))
				y_co -=1 
				x_co -=1
		#Diagonal Up-Right (y is decreasing, x is increasing)
		#reset these
		y_co = self.pos[0]-1
		x_co = self.pos[1]+1
		for values in range(8):
			if y_co < 0 or x_co < 0 or y_co > 7 or x_co > 7:
				break
			#if we come across a piece
			if isinstance(piece_board[y_co][x_co], piece):
				if piece_board[y_co][x_co].trans // 10 == 1:
					break
				else:
					self.valid_movements.append((y_co,x_co))
					break
			else:
				self.valid_movements.append((y_co,x_co))
				y_co -=1 
				x_co +=1
		#Diagonal Down-Left (y is increasing, x is decreasing)
		y_co = self.pos[0]+1
		x_co = self.pos[1]-1
		for values in range(8):
			if y_co < 0 or x_co < 0 or y_co > 7 or x_co > 7:
				break
			#if we come across a piece
			if isinstance(piece_board[y_co][x_co], piece):
				if piece_board[y_co][x_co].trans // 10 == 1:
					break
				else:
					self.valid_movements.append((y_co,x_co))
					break
			else:
				self.valid_movements.append((y_co,x_co))
				y_co +=1 
				x_co -=1
		#Diagonal Down-Right (y is increasing, x is increasing)
		y_co = self.pos[0]+1
		x_co = self.pos[1]+1
		for values in range(8):
			if y_co < 0 or x_co < 0 or y_co > 7 or x_co > 7:
				break
			#if we come across a piece
			if isinstance(piece_board[y_co][x_co], piece):
				if piece_board[y_co][x_co].trans // 10 == 1:
					break
				else:
					self.valid_movements.append((y_co,x_co))
					break
			else:
				self.valid_movements.append((y_co,x_co))
				y_co +=1 
				x_co +=1
    
class b_rook(piece):

	def __init__(self, pos: (int,int)):
			self.pos = pos
			self.value = 3
			self.trans = 14
			self.valid_movements=[]
        
	def valid_movement(self):
		self.valid_movements=[]
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
	def __init__(self, pos:(int,int)):
		self.value = 10
		self.pos = pos
		self.valid_movements = []
		self.trans = 16
		self.check = False
		self.check_mate = False
		self.future = False

	def valid_movement(self):
		self.invalid_moves = []
		self.valid_movements = []
		#get all invalid coordinates
		#adding every non good move
		for columns in range(8):
			for row_cells in range(8):
				if isinstance(piece_board[columns][row_cells], piece):
					if isinstance(piece_board[columns][row_cells], r_king):
						self.invalid_moves.append((columns, row_cells))
						self.invalid_moves.append((columns-1, row_cells))
						self.invalid_moves.append((columns+1, row_cells))
						self.invalid_moves.append((columns-1, row_cells-1))
						self.invalid_moves.append((columns-1, row_cells+1))
						self.invalid_moves.append((columns, row_cells-1))
						self.invalid_moves.append((columns, row_cells+1))
						self.invalid_moves.append((columns+1, row_cells-1))
						self.invalid_moves.append((columns+1, row_cells+1))

					elif isinstance(piece_board[columns][row_cells], r_pawn):
						self.invalid_moves.append((columns-1,row_cells-1))
						self.invalid_moves.append((columns-1,row_cells+1))
					else:
						if piece_board[columns][row_cells].trans // 10 != 1:
							piece_board[columns][row_cells].valid_movement()
							for coordinates in piece_board[columns][row_cells].valid_movements:
								self.invalid_moves.append(coordinates)

		for idx, i in enumerate(range(3)):
			#left around
			if idx == 1:
				y_cord = self.pos[0]-1
				x_cord = self.pos[1]-1
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 1:
						#taking a piece should only append if taking doesnt result in check
						#make check() function that returns true or false; by creating a 
						#deep copy of the board, taking the peice and seeing if check is true
						#if its true, do not append as a valid move
						#if moving doesn't result in check
						if self.future:
							if not check(piece_board, self, (y_cord,x_cord)):
								self.valid_movements.append((y_cord, x_cord))
								self.future = False
				else:
					self.valid_movements.append((y_cord, x_cord))
				#middle left one 
				y_cord = self.pos[0]
				x_cord = self.pos[1]-1
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 1:
						if self.future:
							if not check(piece_board, self, (y_cord,x_cord)):
								self.valid_movements.append((y_cord, x_cord))
								self.future = False
				else:
					self.valid_movements.append((y_cord, x_cord))
				#check 1 left down one
				y_cord = self.pos[0]+1
				x_cord = self.pos[1]-1
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 1:
						if self.future:
							if not check(piece_board, self, (y_cord,x_cord)):
								self.valid_movements.append((y_cord, x_cord))
								self.future = False
				else:
					self.valid_movements.append((y_cord, x_cord))
			#middle top bottom
			elif idx == 2:
				y_cord = self.pos[0]-1
				x_cord = self.pos[1]
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 1:
						if self.future:
							if not check(piece_board, self, (y_cord,x_cord)):
								self.valid_movements.append((y_cord, x_cord))
				else:
					self.valid_movements.append((y_cord, x_cord))
				#other
				y_cord = self.pos[0]+1
				x_cord = self.pos[1]
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 1:
						if self.future:
							if not check(piece_board, self, (y_cord,x_cord)):
								self.valid_movements.append((y_cord, x_cord))
								self.future = False
				else:
					self.valid_movements.append((y_cord, x_cord))
			#right; top middle and bottom.
			else:
				y_cord = self.pos[0]-1
				x_cord = self.pos[1]+1
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 1:
						if self.future:
							if not check(piece_board, self, (y_cord,x_cord)):
								self.valid_movements.append((y_cord, x_cord))
								self.future = False
				else:
					self.valid_movements.append((y_cord, x_cord))
				#middle left one 
				y_cord = self.pos[0]
				x_cord = self.pos[1]+1
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 1:
						if self.future:
							if not check(piece_board, self, (y_cord,x_cord)):
								self.valid_movements.append((y_cord, x_cord))
								self.future = False
				else:
					self.valid_movements.append((y_cord, x_cord))
				#check 1 left down one
				y_cord = self.pos[0]+1
				x_cord = self.pos[1]+1
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 1:
						if self.future:
							if not check(piece_board, self, (y_cord,x_cord)):
								self.valid_movements.append((y_cord, x_cord))
								self.future = False
				else:
					self.valid_movements.append((y_cord, x_cord))

		#get rid of kings movements that are invalid
		#eg cant move into a check position.
		for unchecked in self.invalid_moves:
			if unchecked in self.valid_movements:
				self.valid_movements.remove(unchecked)
		
		if len(self.valid_movements) == 0:
			if self.check == True:
				self.check_mate = True

class b_knight(piece):
	def __init__(self, pos:(int,int)):
		self.value = 5
		self.pos = pos
		self.trans = 12
		self.valid_movements = []
	
	def valid_movement(self):
		self.valid_movements=[]
		for idx, values in enumerate(range(4)):
			#make this 1 function and put as a function of the knight function that passes which team 
			#and what coordinates to check. Pre define the coordinates as a tuple list and iterate through calling the function
			#each time.
			if idx == 0:
				#check far left up 1 eg y-1, x-2
				if (self.pos[0]-1) < 0 or (self.pos[1]-2) < 0 or (self.pos[0]-1) >7 or (self.pos[1]-2) >7:
					pass
				elif isinstance(piece_board[self.pos[0]-1][self.pos[1]-2], piece):
					if piece_board[self.pos[0]-1][self.pos[1]-2].trans // 10 != 1:
						self.valid_movements.append((self.pos[0]-1, self.pos[1]-2))
				else:
					self.valid_movements.append((self.pos[0]-1, self.pos[1]-2))
				
				#check far left down 1; eg y+1 x-2
				if (self.pos[0]+1) < 0 or (self.pos[1]-2) < 0 or (self.pos[0]+1) >7 or (self.pos[1]-2) >7:
					pass
				elif isinstance(piece_board[self.pos[0]+1][self.pos[1]-2], piece):
					if piece_board[self.pos[0]+1][self.pos[1]-2].trans // 10 != 1:
						self.valid_movements.append((self.pos[0]+1, self.pos[1]-2))
				else:
					self.valid_movements.append((self.pos[0]+1, self.pos[1]-2))

			elif idx == 1:
				#check 1 left up two
				y_cord = self.pos[0]-2
				x_cord = self.pos[1]-1
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 1:
						self.valid_movements.append((y_cord, x_cord))
				else:
					self.valid_movements.append((y_cord, x_cord))
				#check 1 left down two
				y_cord = self.pos[0]+2
				x_cord = self.pos[1]-1
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 1:
						self.valid_movements.append((y_cord, x_cord))
				else:
					self.valid_movements.append((y_cord, x_cord))

			elif idx == 2:
				#check right up two
				y_cord = self.pos[0]-2
				x_cord = self.pos[1]+1
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 1:
						self.valid_movements.append((y_cord, x_cord))
				else:
					self.valid_movements.append((y_cord, x_cord))
				#check right down two
				y_cord = self.pos[0]+2
				x_cord = self.pos[1]+1
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 1:
						self.valid_movements.append((y_cord, x_cord))
				else:
					self.valid_movements.append((y_cord, x_cord))
			else:
				#check far right up 1 
				y_cord = self.pos[0]-1
				x_cord = self.pos[1]+2
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 1:
						self.valid_movements.append((y_cord, x_cord))
				else:
					self.valid_movements.append((y_cord, x_cord))
				#check far right down 1 
				y_cord = self.pos[0]+1
				x_cord = self.pos[1]+2
				if (y_cord) < 0 or (x_cord) < 0 or (y_cord) >7 or (x_cord) >7:
					pass
				elif isinstance(piece_board[y_cord][x_cord], piece):
					if piece_board[y_cord][x_cord].trans // 10 != 1:
						self.valid_movements.append((y_cord, x_cord))
				else:
					self.valid_movements.append((y_cord, x_cord))

class b_bishop(piece):
	def __init__(self, pos: (int,int)):
		self.value = 5
		self.trans = 13
		self.valid_movements = []
		self.pos = pos
        
	def valid_movement(self):
		#create a function that ensures that depart isn't the same as to
		valid_movements=[]
		y_co = self.pos[0]-1
		x_co = self.pos[1]-1
		#Diagonal Up-Left (y is decreasing, x is decreasing)
		for values in range(8):
			if y_co < 0 or x_co < 0 or y_co > 7 or x_co > 7:
				break
			#if we come across a piece
			if isinstance(piece_board[y_co][x_co], piece):
				if piece_board[y_co][x_co].trans // 10 == 1:
					break
				else:
					self.valid_movements.append((y_co,x_co))
					break
			else:
				self.valid_movements.append((y_co,x_co))
				y_co -=1 
				x_co -=1
		#Diagonal Up-Right (y is decreasing, x is increasing)
		#reset these
		y_co = self.pos[0]-1
		x_co = self.pos[1]+1
		for values in range(8):
			if y_co < 0 or x_co < 0 or y_co > 7 or x_co > 7:
				break
			#if we come across a piece
			if isinstance(piece_board[y_co][x_co], piece):
				if piece_board[y_co][x_co].trans // 10 == 1:
					break
				else:
					self.valid_movements.append((y_co,x_co))
					break
			else:
				self.valid_movements.append((y_co,x_co))
				y_co -=1 
				x_co +=1
		#Diagonal Down-Left (y is increasing, x is decreasing)
		y_co = self.pos[0]+1
		x_co = self.pos[1]-1
		for values in range(8):
			if y_co < 0 or x_co < 0 or y_co > 7 or x_co > 7:
				break
			#if we come across a piece
			if isinstance(piece_board[y_co][x_co], piece):
				if piece_board[y_co][x_co].trans // 10 == 1:
					break
				else:
					self.valid_movements.append((y_co,x_co))
					break
			else:
				self.valid_movements.append((y_co,x_co))
				y_co +=1 
				x_co -=1
		#Diagonal Down-Right (y is increasing, x is increasing)
		y_co = self.pos[0]+1
		x_co = self.pos[1]+1
		for values in range(8):
			if y_co < 0 or x_co < 0 or y_co > 7 or x_co > 7:
				break
			#if we come across a piece
			if isinstance(piece_board[y_co][x_co], piece):
				if piece_board[y_co][x_co].trans // 10 == 1:
					break
				else:
					self.valid_movements.append((y_co,x_co))
					break
			else:
				self.valid_movements.append((y_co,x_co))
				y_co +=1 
				x_co +=1

class b_pawn(piece):

	def __init__(self, pos:(int, int)):
		self.value = 1
		self.trans = 11
		self.initial = True
		valid_movements=[]
		self.king_invalid = []
		self.pos = pos
	
	def valid_movement(self):
		self.valid_movements=[]
		self.king_invalid =[]
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

		if (self.pos[0]-1) < 0 or self.pos[1]+1 < 0 or (self.pos[0]-1) >7 or self.pos[1]+1 >7:
			pass
		elif isinstance(piece_board[self.pos[0]-1][self.pos[1]+1], piece):
			#if its opposite team
			if piece_board[self.pos[0]-1][self.pos[1]+1].trans // 10 == 2:
				self.valid_movements.append((self.pos[0]-1,self.pos[1]+1))
				self.king_invalid.append((self.pos[0]+1,self.pos[1]+1))
		else:
			self.king_invalid.append((self.pos[0]+1,self.pos[1]+1))

		if (self.pos[0]-1) < 0 or self.pos[1]-1 < 0 or (self.pos[0]-1) >7 or self.pos[1]-1 >7:
			pass
		elif isinstance(piece_board[self.pos[0]-1][self.pos[1]-1], piece):
			#if its opposite team
			if piece_board[self.pos[0]-1][self.pos[1]-1].trans // 10 == 2:
				self.king_invalid.append((self.pos[0]-1,self.pos[1]-1))
				self.valid_movements.append((self.pos[0]-1,self.pos[1]-1))
		else:
			self.king_invalid.append((self.pos[0]+1,self.pos[1]+1))

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

def check_if_king_needs_to_move() -> bool:
	for column in range(8):
		for row_cell in range(8):
			if isinstance(piece_board[column][row_cell], r_king):
				piece_board[column][row_cell].valid_movement()
				if piece_board[column][row_cell].check == True:
					return True
				else:
					return False


def check(a_piece_board, king, to: (int,int)) -> bool:
	#taking a piece should only append if taking doesnt result in check
	#make check() function that returns true or false; by creating a 
	#copy of the board, taking the peice and seeing if check is true
	#if its true, do not append as a valid move
	'''copy_for_checking = copy.deepcopy(a_piece_board)
	print(copy_for_checking)
	copy_for_checking[to[0]][to[1]] = 0
	king.valid_movement()
	if to in king.valid_movements:
		return False
	else:
		return True'''
	copy_for_checking = [row[:] for row in a_piece_board]
	king.future = True
	copy_for_checking[to[0]][to[1]] = 0
	king.valid_movement()
	if to in king.valid_movements:
		return False
	else:
		return True
	
def piece_saving_check(a_piece_board, king, fro:(int,int), to:(int,int)) -> bool:
	'''
	This function checks if moving a piece will save the king 
	from being in check
	#returns false if the move is not allowed
	#returns True if the move saves the king
	'''
	copy_for_checking = [row[:] for row in a_piece_board]
	moving_piece = piece_board[fro[0]][fro[1]]
	print(moving_piece)
	piece_board[moving_piece.pos[0]][moving_piece.pos[1]] = 0

	piece_board[to[0]][to[1]] = moving_piece
	king.valid_movement()

	if king.check == True:
		return False
	else:
		return True




piece_board = [[r_rook((0,0)),r_knight((0,1)),r_bishop((0,2)),r_queen((0,3)),0,r_bishop((0,5)),r_knight((0,6)),r_rook((0,7))], 
[r_pawn((1,0)),r_pawn((1,1)),r_pawn((1,2)),r_pawn((1,3)),r_pawn((1,4)),r_pawn((1,5)),r_pawn((1,6)),r_pawn((1,7))], 
[0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0], 
[r_king((4,0)),0,0,b_pawn((4,3)),0,0,0,0], 
[b_pawn((5,0)),0,0,0,b_knight((5,4)),0,0,0], 
[0,b_pawn((6,1)),b_pawn((6,2)),b_pawn((6,3)),0,b_pawn((6,5)),b_pawn((6,6)),b_pawn((6,7))], 
[b_rook((7,0)),b_knight((7,1)),b_bishop((7,2)),b_queen((7,3)),b_king((7,4)),b_bishop((7,5)),0,b_rook((7,7))]]

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
	#This needs rewriting
	game_over=False
	while not game_over:
		print_board(board, piece_board, piece_dictionary)
		fro, to = str(input("where from")), str(input("where to"))

		if check_if_king_needs_to_move() == True:
			while check_if_king_needs_to_move() == True:
				print("king is in check, you must move the king")
				fro, to = str(input("where from")), str(input("where to"))
				for columns in range(8):
					for cells in range(8):
						if isinstance(piece_board[columns][cells], r_king):
							kingpos = piece_board[columns][cells]

				fro_pos, to_pos = pos_system[fro], pos_system[to]
				if piece_saving_check(piece_board, kingpos, fro_pos, to_pos) == True:
					make_movement(fro, to)
					#print_board(board, piece_board, piece_dictionary)
				else:
					print("movement does not save the king, try again ")
		else:
			try:
				make_movement(fro, to)
				print_board(board, piece_board, piece_dictionary)
			except:
				print("invalid move, try again")
			
#instead of making the movement for us, we could make make_movement return the coordinate that is changing, and therefore when in gen_game is called if king is 
#in check, seew if make_movement != False and if king.check != True; then follow through
def make_movement(dep, to):
	#This needs rewriting
	try:
		test = piece_board[pos_system[dep][0]][pos_system[dep][1]]
		pass

	except:
		print("Keyed a position that doesn't exist; enter to a position that you can move to")
		test = piece_board[pos_system[dep][-10]][pos_system[to][-10]]
	if dep == to:
		print("You cannot move to the same sqaure")
		test = piece_board[pos_system[dep][-10]][pos_system[to][-10]]

	#if there is a piece at the dep position
	if isinstance(piece_board[pos_system[dep][0]][pos_system[dep][1]], piece):
		moving_piece = piece_board[pos_system[dep][0]][pos_system[dep][1]]
		#update the valid coordinate to move onto
		moving_piece.valid_movement()
		#check must come after valid_movement

		#if where we are moving to is valid
		if pos_system[to] in moving_piece.valid_movements:
			#if there is nothing where we are going
			if not(isinstance(piece_board[pos_system[to][0]][pos_system[to][1]], piece)):
				moving_piece.pos = (pos_system[to][0], pos_system[to][1])
				#make old pieceboard piece nothing
				piece_board[pos_system[dep][0]][pos_system[dep][1]] = 0
				#make new pieceboard position new piece
				piece_board[pos_system[to][0]][pos_system[to][1]] = moving_piece
			else:
				#There is something where we are moving and have to replace it
				piece_board[pos_system[to][0]][pos_system[to][1]] = 0
				moving_piece.pos = (pos_system[to][0], pos_system[to][1])
				#make old pieceboard piece nothing
				piece_board[pos_system[dep][0]][pos_system[dep][1]] = 0
				#make new pieceboard position new piece
				piece_board[pos_system[to][0]][pos_system[to][1]] = moving_piece
		else:
			print("Moving to a position that you cant move to")
			test = piece_board[pos_system[dep][-10]][pos_system[to][-10]]
	else:
		print("There is no piece selected")
		test = piece_board[pos_system[dep][-10]][pos_system[to][-10]]

#========================================================================================================================================================================
#
#                               PIECE CLASS CREATION
#
#========================================================================================================================================================================
#2 = red
#1 = blue
gen_game()

#have to update the piece board each time to print