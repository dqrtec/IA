# class Queue:
# 	def __init__(self):
# 		self.q = []
# 		self.length = 0

# 	def enqueue(self, vertex):
# 		self.q.append(vertex)
# 		self.length = len(self.q)

# 	def dequeue(self):
# 		u = self.q.pop(0)
# 		self.length = len(self.q)

# 		return u

class Game:
	def __init__(self, game_state):
		self.visited = False # TODO change visited property to visited property - True(Black) or False(White)
		self.level = 0
		self.predecessor = None
		self.successors = []
		self.state = game_state
		self.solutions_state = []

	def findSolutions(self):
		if (self.successor == None):
			return game.state
		else:
			self.solutions_state.append(game.predecessor.findSolutions)

	def sameAs(self, other_game):
		return self.state == other_game.state

	def find_possible_successors(self):
		coordinates = self.find_empty_space()
		
		# refazer calculo para troca(*) => nova_coordenada = atual + coordenada a ser trocada
		new_state = self.try_move_piece_left(coordinates)
		if (new_state != self.state):
			self.successors.append(Game(new_state))

		new_state = self.try_move_piece_right(coordinates)
		if (new_state != self.state):
			self.successors.append(Game(new_state))

		new_state = self.try_move_piece_up(coordinates)
		if (new_state != self.state):
			self.successors.append(Game(new_state))

		new_state = self.try_move_piece_down(coordinates)
		if (new_state != self.state):
			self.successors.append(Game(new_state))

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
			if (col > 0):
				copy_state[row][col-1], copy_state[row][col] = self.state[row][col], self.state[row][col-1] 
			return copy_state

	def try_move_piece_right(self, coordinates):
			row, col = coordinates
			copy_state = self.copy()
			if (col < 2):
				copy_state[row][col+1], copy_state[row][col] = self.state[row][col], self.state[row][col+1] 
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

	while Queue.length != 0:
		node = Queue.pop()

		if node.sameAs(goal_state):
			return node

		node.find_possible_successors()

		for successor in u.successors:
			if !successor.visited:
				successor.level = node.level + 1
				successor.predecessor = node
				Q.enqueue(v)
		node.visited = True

	return None

def main():
	
	#TESTE movimentação

	g = Game([[1, 2, '*'], 
			 [4, 5, 3],
			 [7, 8, 6]])

	# successors = g.play()
	# g.imprimir()
	# print()

	# for play in successors:
	# 	play.imprimir()
	# 	print()



main()
