class Game:
	def __init__(self, game_state):
		self.visited = False
		self.level = 0
		self.predecessor = None
		self.successors = []
		self.state = game_state
		self.solutions_state = []

	def show_solutions(self):
		if (self.predecessor == None):
			self.browse()
			print()
		else:
			self.solutions_state.append(self.predecessor.show_solutions())
			self.browse()
			print()

	def sameAs(self, other_game):
		return self.state == other_game.state

	def find_possible_successors(self):
		coordinates = self.find_empty_space()
		
		# new_state = self.try_move_piece_left(coordinates)
		# if (new_state != self.state):
		# 	self.successors.append(Game(new_state))

		# new_state = self.try_move_piece_right(coordinates)
		# if (new_state != self.state):
		# 	self.successors.append(Game(new_state))

		# new_state = self.try_move_piece_up(coordinates)
		# if (new_state != self.state):
		# 	self.successors.append(Game(new_state))

		# new_state = self.try_move_piece_down(coordinates)
		# if (new_state != self.state):
		# 	self.successors.append(Game(new_state))

		self.try_move_piece(coordinates)

		return self.successors

	def find_empty_space(self):
		for i in range(3):
			for j in range(3):
				if self.state[i][j] == '*':
					return (i, j)

	def copy(self):
		new_game = []
		for i in self.state:
			a = []
			for j in i:
				a.append(j)
			new_game.append(a)

		return new_game


	def try_move_piece_left(self, coordinates):
			row, col = coordinates
			copy_state = self.copy()
			
			return copy_state

	def try_move_piece_right(self, coordinates):
			row, col = coordinates
			copy_state = self.copy()
			
			return copy_state

	def try_move_piece_up(self, coordinates):
			row, col = coordinates
			copy_state = self.copy()
			if (row > 0):
				copy_state[row-1][col], copy_state[row][col] = self.state[row][col], self.state[row-1][col] 
			return copy_state

	def try_move_piece_down(self, coordinates):
			row, col = coordinates
			copy_state = self.copy()
			if (row < 2):
				copy_state[row+1][col], copy_state[row][col] = self.state[row][col], self.state[row+1][col] 
			return copy_state

	def try_move_piece(self, coordinates):
		row, col = coordinates

		if (row < 2):
			copy_state = self.copy()
			copy_state[row+1][col], copy_state[row][col] = self.state[row][col], self.state[row+1][col]
			if self.predecessor == None or copy_state != self.predecessor.state: 
				self.successors.append(Game(copy_state))

		if (row > 0):
			copy_state = self.copy()
			copy_state[row-1][col], copy_state[row][col] = self.state[row][col], self.state[row-1][col]
			if self.predecessor == None or copy_state != self.predecessor.state:
				self.successors.append(Game(copy_state))

		if (col > 0):
			copy_state = self.copy()
			copy_state[row][col-1], copy_state[row][col] = self.state[row][col], self.state[row][col-1] 
			if self.predecessor == None or copy_state != self.predecessor.state:
				self.successors.append(Game(copy_state))

		if (col < 2):
			copy_state = self.copy()
			copy_state[row][col+1], copy_state[row][col] = self.state[row][col], self.state[row][col+1] 
			if self.predecessor == None or copy_state != self.predecessor.state:
				self.successors.append(Game(copy_state))

	def browse(self):
		for i in range(3):
			for j in range(3):
				print(self.state[i][j], end=' ')
			print()

def bfs(initial_state, goal_state):
	initial_state.level = 0
	initial_state.predecessor = None

	Queue = []
	Queue.append(initial_state)

	while len(Queue) != 0:
		node = Queue.pop(0)

		if node.sameAs(goal_state):
			return node

		node.find_possible_successors()

		for successor in node.successors:
			if not(successor.visited):
				successor.level = node.level + 1
				successor.predecessor = node
				Queue.append(successor)
		node.visited = True

def main():
	
	g = Game([[2, '*', 4], 
			 [3, 1, 6],
			 [7, 5, 8]])
	
	g1 = Game([[1, '*', 2], 
			 [4, 5, 3],
			 [7, 8, 6]])

	goal = Game([[1, 2, 3],
				 [4, 5, 6],
				 [7, 8, '*']])

	sol = bfs(g, goal)

	sol.show_solutions()

main()
