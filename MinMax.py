class Board():


	def __init__(self):

		self.board = [
				['','',''],
				['','',''],
				['','',''],
			]								
		self.winner = None					
		self.currentPlayer = 'AIPlayer'		
		self.scores = {						 
			'X':1,
			'O':-1,
			'tie':0,
		}

		self.ai = 'X'						
		self.human = 'O'					


	
	def isBoardNotFull(self):
		for i in range (len(self.board)):
				for j in range (len(self.board[i])):
					if self.board[i][j] == '':
						Ans = True
						break
					else:
						Ans = False
		return Ans



	def checkSpaceOnBoard(self,place):
		if place == '':
			return True
		else:
			return False


	def checkWinner(self):
		self.winner = None
		
		if self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2]:
			self.winner = self.board[2][0]
		elif self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
	  		self.winner = self.board[0][0]
		else:

			for i in range(len(self.board)):
				if self.winner in ["", None]:
					
					if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
						self.winner = self.board[i][0]
					
					elif self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
						self.winner = self.board[0][i]


		if self.winner == None and self.isBoardNotFull() == False:
			return 'tie'						
		elif self.winner == None:
			return ""							
		else:
			return self.winner 					


	
	def minmax(self,depth,isMaxinizig):
		result = self.checkWinner()

		
		if result != '':
			return self.scores[result]

		 
		if isMaxinizig:
			bestscore = -1
			for i in range (len(self.board)):
				for j in range (len(self.board[i])):
					if self.checkSpaceOnBoard(self.board[i][j]):
						self.board[i][j] = self.ai 				
						score = self.minmax(depth+1,False)		
						self.board[i][j] = '';
						bestscore = max(score,bestscore)		
		
		else:
			bestscore = 1
			for i in range (len(self.board)):
				for j in range (len(self.board[i])):
					if self.checkSpaceOnBoard(self.board[i][j]):
						self.board[i][j] = self.human 			
						score = self.minmax(depth+1,True)		
						self.board[i][j] = '';
						bestscore = min(score,bestscore) 		
		return bestscore


	def bestMove(self):
		bestscore = -1000000
		for i in range (len(self.board)):
				for j in range (len(self.board[i])):
					if self.checkSpaceOnBoard(self.board[i][j]):
						self.board[i][j] = self.ai 				
						score = self.minmax(0,False)			
						self.board[i][j] = ''
						if  score > bestscore:					
							bestscore = score
							bestMove = [i,j]
		a = bestMove[0]
		b = bestMove[1]
		self.board[a][b] = self.ai 								 
		self.currentPlayer = 'HumanPlayer'						



	def __repr__(self):
		out = ""
		for i in self.board:
			char = " "
			for j in i:
				out = out + char +j
				char = "|"
			out = out + "\n"
		return out



if __name__ == '__main__':
	print("Let the Game Begin")
	board = Board()													
	while board.isBoardNotFull():									
		if board.currentPlayer == 'AIPlayer':						
			board.bestMove()
			
		else:														
			currentwinner=board.checkWinner()						 
			if board.isBoardNotFull() and currentwinner != None:	
				row = int(input("Enter row of next move"))			
				column = int(input("Enter column of next move"))	
				board.board[row][column] = board.human 				
				board.currentPlayer = 'AIPlayer' 					
		print(board)	
		if board.checkWinner() != '':								
			result = board.checkWinner() 						
			if result != None:
				ans = board.scores[result]
				if ans == 10:
					winner = 'X'
				elif ans == -10:
					winner = 'O'
				else:
					Winner = 'Its a tie'			
			break


	print("Winner is: ",board.winner)								

		