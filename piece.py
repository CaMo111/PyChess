from abc import ABC, abstractmethod

class piece(ABC):

	@abstractmethod
	def __init__(self) -> None:
		pass
	
#
#RED 
#    
class r_queen(piece):
	def __init__(self):
			self.value = 9
			self.trans = 25
		
	def valid_movement(self):
		valid_movements=[]
    
class r_rook(piece):
    def __init__(self):
            self.value = 3
            self.trans = 24
        
    def valid_movement(self):
        valid_movements=[]
		
class r_king(piece):
	def __init__(self):
		self.value = 10
		self.trans = 26
	
	def valid_movement(self):
		valid_movements=[]

class r_pawn(piece):

	def __init__(self, pos:(int, int)):
		self.value = 1
		self.trans = 21
		#self.pos example is (1,0) for a7
		self.pos = pos 
		self.initial = True
	
	def valid_movement(self):
		if self.initial == True:
		    self.valid_movements=[(self.pos[0]+1, self.pos[1]), (self.pos[0]+2, self.pos[1])]
			
        
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
#
#BLUE 
#   

class b_queen(piece):
	def __init__(self):
			self.value = 9
			self.trans = 15
		
	def valid_movement(self):
		valid_movements=[]
    
class b_rook(piece):
    def __init__(self):
            self.value = 3
            self.trans = 14
        
    def valid_movement(self):
        valid_movements=[]
		
class b_king(piece):
	def __init__(self):
		self.value = 10
		self.trans = 16

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
	def __init__(self):
		self.value = 1
		self.trans = 11
		self.initial = True
	
	def valid_movement(self):
		valid_movements=[]