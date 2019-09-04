from heap import heap

# Recebe uma tabela e duplica ela
##NOTA: eu poderia tem feito simplismente: return list(tabela) ou tabela[:] 
## 		Mas simplismente nao rodava
def copiarTabela(tabela):
	novaTabela = []
	for x in tabela:
		a = []
		for y in x:
			a.append(y)
		novaTabela.append(a)
	return novaTabela	

# Printa a posicao das Pecas no tabuleiro
def mostrarTabela(tabela):
	print()
	for linha in tabela:
		print(linha)
	print()

# Funcao de custo Distancia Manhatan
def Fcusto(tabela):
	custo = 0
	for (i,j) in [(a,b) for a in range(0,len(tabela)) for b in range(0,len(tabela)) ]:
		if( (tabela[i][j] != i*len(tabela) + j+1) and (type(tabela[i][j])==int)):
			custo += (  abs(i - (tabela[i][j]//len(tabela))) + abs(j - (tabela[i][j]%len(tabela)))   )*tabela[i][j]
	return custo

# Cria uma lista com todas as possibilidade possiveis para a tabela de entrada
def criarFilhos(tabela):
	filhos=[]

	#encontrar a posicao da * e armazena em (i,j)
	for linha in range(0,len(tabela)):
		if '*' in tabela[linha]:

			i = linha
			j = tabela[linha].index('*')

	# anda a * em vertical e horizontal e gera filho para cada caso
	for ajusteY,ajusteX in [(1,0),(-1,0),(0,1),(0,-1)]:
		if 0<=i+ajusteY<len(tabela) and 0<=j+ajusteX<len(tabela) :

			t = copiarTabela(tabela)
			t[i][j] = t[i+ajusteY][j+ajusteX]
			t[i+ajusteY][j+ajusteX] = '*'
			filhos.append(t)

			t=[]
	return filhos


### DESCOMENTE UMA DAS LINHAS PARA RODAR
#### utilize o site https://www.helpfulgames.com/subjects/brain-training/sliding-puzzle.html
#### para criar novos exemplos (por definicao do jogo é possivel nao ter solucao)
#### esse site garante que havera solucao

## teste FACIL
# inicio = [[1,2,3],[4,5,6],[7,8,'*']]
inicio = [['*',2,3],[1,5,6],[4,7,8]]

## teste RAZOAVEL
#inicio = [[6,7,3],[2,5,8],[4,1,'*']]
# inicio = [[1,6,7],[8,5,2],[4,3,'*']]

## teste DIFICIL (nao resolve rapido)
# inicio = [[1,3,5,7],[9,11,13,15],[2,4,6,14],[8,12,10,'*']]
# inicio = [[1,3,5,7],[9,11,13,15],[2,4,6,14],[8,12,10,'*']]

# cria a uma heap com a configuracao inicial
r = heap(inicio,Fcusto(inicio))

# armazena todos os estados ja visitados
# evita minimos locais
EstadosVisitados = []

while True :

	# menor elemento da heap
	m = r.Menor()

	# remove o menor elemento da heap
	# evita revisitar estados 
	removido = r.remover(m)
	r = removido if removido is not None else r

	mostrarTabela(m.tabela)

	# Encerra se achar solucao
	if m.custo==0:
		mostrarTabela(m.tabela)
		break

	# Com base no no da heap
	# cria filhos e se o filho ainda nao foi visitado
	# coloca ele na heap
	for filho in criarFilhos(m.tabela):
		if filho not in EstadosVisitados:
			r.adicionar(heap(filho,Fcusto(filho)))
			EstadosVisitados.append(filho)