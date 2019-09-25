import _thread
import threading
import random as rdn

flag = False
def exitFlag():
	return flag

class myThread(threading.Thread):
	def __init__(self,n):
		threading.Thread.__init__(self)
		self.n = n
		self.temperatura = 50
		self.interacao = 1

	def temperaturaAtual(self, custoInicial, custoFinal):
		return 10**((custoInicial - custoFinal)/self.temperatura)

	def mudarTemperatura(self):
		self.temperatura = self.temperatura**(1/2)

	def copiarTabela(self, tabela):
		novaTabela = []
		for x in tabela:
			a = []
			for y in x:
				a.append(y)
			novaTabela.append(a)
		return novaTabela

	def copiarListas(self, lista):
		listaCopiada = []
		for x in lista:
			listaCopiada.append(x)
		return listaCopiada

	def mostrarTabela(self, tabela):
		print()
		for linha in tabela:
			print(linha)
		print()

	def custoColuna(self, tabela):
		custo = 0
		n = self.n
		for coluna in range(0,n):
			quantidadeRainhas = 0
			for linha in range(0,n):
				if tabela[linha][coluna] == 1 :
					quantidadeRainhas += 1
			custo += self.custoDasRainhas(quantidadeRainhas)
		return custo

	def custoDiagonal(self, tabela):
		return self.custoDiagonalEsquerda(tabela) + self.custoDiagonalDireita(tabela)

	def custoDiagonal2(self, tabela):
		if self.custoDiagonalEsquerda(tabela) != 0:
			print("diagonal E")
		if self.custoDiagonalDireita(tabela) != 0:
			print("diagonal D")
		return self.custoDiagonalEsquerda(tabela) + self.custoDiagonalDireita(tabela)

	def custoDiagonalEsquerda(self, tabela):
		custo = 0
		n = self.n
		for soma in [i for i in range(0,n*2)] :
			quantidadeRainhas = 0
			for linha in range(0,n):
				for coluna in range(0,n):
					if (linha + coluna) == soma:
						if tabela[linha][coluna] == 1:
							quantidadeRainhas+=1
			custo += self.custoDasRainhas(quantidadeRainhas)
		return custo

	def custoDiagonalDireita(self, tabela):
		custo = 0
		n = self.n
		for i in range(0,n):
			quantidadeRainhas = 0
			for j in range(0,n-i):
				if tabela[i+j][j] == 1:
					quantidadeRainhas += 1
			custo+= self.custoDasRainhas(quantidadeRainhas)

		for j in range(1,n):
			quantidadeRainhas = 0
			for i in range(0,n-j):
				if tabela[i][j+i] == 1:
					quantidadeRainhas += 1
			custo+= self.custoDasRainhas(quantidadeRainhas)
		return custo


	def custoDasRainhas(self, quantidadeRainhas):
		custo = 0
		if quantidadeRainhas > 1:
				custo = quantidadeRainhas -1
		return custo

	def funcaoCusto(self, tabela):
		return self.custoColuna(tabela) + self.custoDiagonal(tabela)

	def funcaoCusto2(self, tabela):
		if self.custoColuna(tabela)!= 0:
			print("coluna")
		if self.custoDiagonal2(tabela) !=0:
			print("diagonal")
		print("custo total = %d"%(self.custoDiagonal(tabela)+self.custoColuna(tabela)))

	def criarTabela(self):
		n = self.n
		tabela = []
		for linha in range(1,n+1):
			linhaOrdenada = [int(i/n) for i in range(1,n+1)]
			rdn.shuffle(linhaOrdenada)
			tabela.append(linhaOrdenada)
		return tabela

	def criarTabelas(self, quantidadeTabelas):
		listaTabelas = []
		for x in range(0,quantidadeTabelas):
			listaTabelas.append(self.criarTabela())
		return listaTabelas

	def run(self):
		n = self.n

		listaTabelas = self.criarTabelas(10)
		listaAuxiliar = []
		Resultado = []

		while not exitFlag():
			self.interacao+=1
			for indiceTabela in range(len(listaTabelas)):

				if exitFlag():
					break

				tabela = listaTabelas[indiceTabela]

				tabelaInicical = self.copiarTabela(tabela)
				custoInicial = self.funcaoCusto(tabelaInicical)

				tabelaFinal = self.copiarTabela(tabela)

				linhaAleatoria = rdn.randint(0,n-1)
				indiceRainha = tabelaFinal[linhaAleatoria].index(1)
				tabelaFinal[linhaAleatoria][indiceRainha] = 0
				colunaAleatoria = rdn.randint(0,n-1)
				tabelaFinal[linhaAleatoria][colunaAleatoria] = 1

				custoFinal = self.funcaoCusto(tabelaFinal)

				if custoFinal < custoInicial:
					listaTabelas[indiceTabela] = tabelaFinal
				elif self.temperaturaAtual(custoInicial,custoFinal) > rdn.random():
					listaTabelas[indiceTabela] = tabelaFinal
				else:
					listaTabelas[indiceTabela] = tabelaInicical

				if self.funcaoCusto(listaTabelas[indiceTabela]) == 0:
					Resultado = listaTabelas[indiceTabela]
					break

			print("%d - %d = %f"%(custoInicial, custoFinal, self.temperaturaAtual(custoInicial,custoFinal)))

			if Resultado != []:
				break
			self.mudarTemperatura()


		self.funcaoCusto(Resultado)
		self.mostrarTabela(Resultado)
		print(self.interacao)



threads=[]
for i in range(1):
	threads.append( myThread(8) )

for x in threads:
	x.start()
	
print ("Exiting Main Thread")
