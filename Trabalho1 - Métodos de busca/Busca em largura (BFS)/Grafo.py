#_*_ coding: utf8 _*_
class No(object):
	def __init__(self, state=[[1,2,0],[4,5,3],[7,8,6]], parent, action, path_cost=0):
		self.state = state
        self.parent = parent
        self.
		self.vizinhos = []
		self.atingido = False

	def addVizinho(self, no):
		if no not in self.vizinhos:
			self.vizinhos.append(no)
			no.vizinhos.append(self)

	def __str__(self):
		return str(self.id)
        
