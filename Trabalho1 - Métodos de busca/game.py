class Tree:
	def __init__(self, vertex_list, edge_list):
		self.vertex = vertex_list
		self.edge = edge_list

	def add_vertex(self, vertex):
		self.vertex.append(vertex)

	def add_edge(self, edge):
		self.edge.append(edge)

	def adj(self, vertex):
		adjacency = []
		for edge in self.edge:
			if edge.u.value == vertex.value:
				adjacency.append(edge.v)

		return adjacency

class Edge:
	def __init__(self, u, v):
		self.u = u # vertex
		self.v = v # vertex

class Vertex:
	def __init__(self, game):
		self.color = ''
		self.level = 0
		self.predecessor = None
		self.successor = []
		self.value = game

class Queue:
	def __init__(self):
		self.q = []
		self.length = 0

	def enqueue(self, vertex):
		self.q.append(vertex)
		self.length = len(self.q)

	def dequeue(self):
		u = self.q.pop(0)
		self.length = len(self.q)

		return u

class Game:
	def __init__(self, game_state):
		self.state = game_state
		self.plays = []

	def play(self):
		coordinates = self.find_empty_space()
		
		# refazer calculo para troca(*) => nova_coordenada = atual + coordenada a ser trocada
		self.move_piece(coordinates, (0, 1))
		self.move_piece(coordinates, (0, -1))
		self.move_piece(coordinates, (1, 0))
		self.move_piece(coordinates, (-1, 0))

		return self.plays

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


	def move_piece(self, coordinates, new_coordinates):
		
			# print('(', coordinates[0], ',', coordinates[1], ')', end='\n')
			# print('(', new_coordinates[0], ',', new_coordinates[1], ')', end='\n\n\n')
			copy_state = self.copy()

			old_x = coordinates[0]
			old_y = coordinates[1]

			# print(self.state[new_coordinates[0]][new_coordinates[1]], end=' ')
			# print(self.state[coordinates[0]][coordinates[1]])

			copy_state[coordinates[0]][coordinates[1]] = self.state[new_coordinates[0]][new_coordinates[1]]
			copy_state[new_coordinates[0]][new_coordinates[1]] = self.state[old_x][old_y]

			self.plays.append(Game(copy_state))

	def imprimir(self):
		for i in range(3):
			for j in range(3):
				print(self.state[i][j], end=' ')
			print()

def bsf(graph, s):
	for u in graph.vertex:
		u.color = 'white'
		u.level = float('inf')
		u.predecessor = None

	s.color = 'gray'
	s.level = 0
	s.predecessor = None

	Q = Queue()

	Q.enqueue(s)

	while Q.length != 0:
		u = Q.dequeue()

		for v in u.successor:
			if v.color == 'white':
				v.color = 'gray'
				v.level = u.level + 1
				v.predecessor = u
				Q.enqueue(v)

		u.color = 'black'


def main():
	
	g = Game([[1, 2, '*'], 
			 [4, 5, 3],
			 [7, 8, 6]])

	plays = g.play()
	g.imprimir()
	print()

	for play in plays:
		play.imprimir()
		print()

main()
