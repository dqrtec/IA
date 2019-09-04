from heap import heap

class arvore:
	def __init__(self, tabela, custo):
		self.tabela = tabela
		self.custo = custo
		self.filhos = []
		self.heap = heap(self,self)

	def adicionarFilho(self,filho):
		self.filhos.append(filho)
		self.heap.adicionar(filho)

	def MenorValor(self):

		if self.filhos == []:
			return self
		else:
			menor=self.filhos[0].MenorValor()
			for filho in self.filhos:
				if menor.custo> (filho.MenorValor()).custo:
					menor = filho.MenorValor()
			return menor

	def Mostrar(self):
		self.heap.PassearHeap()