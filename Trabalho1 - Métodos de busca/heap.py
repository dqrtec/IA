class heap:
	#nosE -> heap esquerda
	#nosD -> heap direita
	#custo -> custo da tabela
	#root -> root de todas as heaps(é a mesma em todas as heaps)
	def __init__(self,tabela,custo):
		self.tabela = tabela
		self.nosE = None
		self.nosD = None
		self.custo = custo
		self.root = self

	# Adiciona noNovo na heap
	# chame essa funcao na raiz
	def adicionar(self,noNovo):

	 	if noNovo.custo > self.custo:
	 		if self.nosD is None:
	 			self.nosD = noNovo
	 			self.nosD.root = self.root
	 		else:
	 			self.nosD.adicionar(noNovo)
	 			
	 	else:
	 		if self.nosE is None:
	 			self.nosE = noNovo
	 			self.nosE.root = self.root
	 		else:
	 			self.nosE.adicionar(noNovo)

	# retorna a referencia do no mais a esquerda(menor)
	def Menor(self):
		if self.nosE is None:
			return self
		return self.nosE.Menor()

	# remover elemento noRemover da heap
	# como eu sempre so irei remover o menor
	# so é implementado a remorcao a esquerda e root
	# RETORNA A raiz da HEAP
	def remover(self,noRemover):
		# se for remover a raiz
		# subistitua a raiz pelo filho direito ou
		# crie uma heap nova que so tera filho esquerdo
		if self.root.nosE is None:
			if self.root.nosD is None:
				self = heap(self.tabela,99999)
				self.root = self
			else:
				self = self.nosD
				self.mudarRoot(self)
			return self.root

		# se tiver filho a esquerda => Desca a esquerda
		elif( (self.nosE is not None) and  (self.nosE.nosE is not None) ):
			self.nosE.remover(noRemover)

		# se nao tiver filho a esquerda
		# 	troque o no removido pelo filho a direita(se tiver)
		#	senao simplismente remova o no
		elif( (self.nosE is not None) and (self.nosE.nosE is None) ):
			if self.nosE.nosD is None:
				self.nosE = None
			else:
				self.nosE = self.nosE.nosD
			return self.root

	# em caso de a raiz ser removida
	# chame essa funcao para mudar
	# todas as root de todas as heaps
	def mudarRoot(self,novoRoot):
		self.root = novoRoot
		if self.nosE is not None:
			self.nosE.mudarRoot(novoRoot)
		if self.nosD is not None:
			self.nosD.mudarRoot(novoRoot)

	# mostra todos os elementos da heap
	def PassearHeap(self):
		if self.nosE is not None:
			self.nosE.PassearHeap()
		if self.custo is not None:
			print(self.custo,end=" - ")
		if self.nosD is not None:
			self.nosD.PassearHeap()