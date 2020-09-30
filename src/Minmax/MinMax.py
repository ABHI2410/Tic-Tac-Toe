class Board():

	####################################################################
	#                  Defining all important variables                #
	####################################################################
	def __init__(self):

		self.board = [
				['','',''],
				['','',''],
				['','',''],
			]								# tic-tac-toe board
		self.winner = None					# tic-tac-toe winner
		self.currentPlayer = 'AIPlayer'		# Player who is playing
		self.scores = {						# Score of each outcome 
			'X':1,
			'O':-1,
			'tie':0,
		}

		self.ai = 'X'						# AI player Initial
		self.human = 'O'					# Human player Initial


	####################################################################
	#                  Checking if board is full or not                #
	####################################################################
	def isBoardNotFull(self):
		for i in range (len(self.board)):
				for j in range (len(self.board[i])):
					if self.board[i][j] == '':
						Ans = True
						break
					else:
						Ans = False
		return Ans


	####################################################################
	#           Checking if board position is full or not              #
	####################################################################
	def checkSpaceOnBoard(self,place):
		if place == '':
			return True
		else:
			return False


	####################################################################
	#              Checking if any player has won yet                  #
	####################################################################
	def checkWinner(self):
		self.winner = None
		#Diagonal win condition check
		if self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2]:
			self.winner = self.board[2][0]
		elif self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
	  		self.winner = self.board[0][0]
		else:

			for i in range(len(self.board)):
				if self.winner in ["", None]:
					#horizontal win condition check
					if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
						self.winner = self.board[i][0]
					#vertical win condition check
					elif self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
						self.winner = self.board[0][i]


		if self.winner == None and self.isBoardNotFull() == False:
			return 'tie'						# Return Tie if Board is full and no winner was found
		elif self.winner == None:
			return ""							# Return null if no winner is found
		else:
			return self.winner 					# Return winner if found


	####################################################################
	#                Recursive MinMax Algorithm                        #
	####################################################################
	def minmax(self,depth,isMaxinizig):
		result = self.checkWinner()

		# winner found return score
		if result != '':
			return self.scores[result]

		# AI Player's turn 
		if isMaxinizig:
			bestscore = -1
			for i in range (len(self.board)):
				for j in range (len(self.board[i])):
					if self.checkSpaceOnBoard(self.board[i][j]):
						self.board[i][j] = self.ai 				# AI Initial Assigning
						score = self.minmax(depth+1,False)		# Recursive Call for minmax
						self.board[i][j] = '';
						bestscore = max(score,bestscore)		# Check if move was optimal or not
		# Human Player's turn
		else:
			bestscore = 1
			for i in range (len(self.board)):
				for j in range (len(self.board[i])):
					if self.checkSpaceOnBoard(self.board[i][j]):
						self.board[i][j] = self.human 			# Human Initial Assigning
						score = self.minmax(depth+1,True)		# Recursive Call for minmax
						self.board[i][j] = '';
						bestscore = min(score,bestscore) 		# Check if move was optimal or not
		return bestscore


	####################################################################
	#                Finding Best Move for AI                          #
	####################################################################
	def bestMove(self):
		bestscore = -1000000
		for i in range (len(self.board)):
				for j in range (len(self.board[i])):
					if self.checkSpaceOnBoard(self.board[i][j]):
						self.board[i][j] = self.ai 				# Human Initial Assigning
						score = self.minmax(0,False)			# Function call for minmax
						self.board[i][j] = ''
						if  score > bestscore:					# Check if move is best move or not
							bestscore = score
							Move = [i,j]					
		return Move


	####################################################################
	#            Representation of Tic-Tac-Toe board                   #
	####################################################################
	def __repr__(self):
		out = ""
		for i in self.board:
			char = " "
			for j in i:
				out = out + char +j
				char = "|"
			out = out + "\n"
		return out


