'''
 Disclaimer: 
 	Esse código (e seus dependentes) são fortemente baseados no código do DQN-Atari-Tensorflow, do usuário Songrotek (https://github.com/songrotek/DQN-Atari-Tensorflow)
 	Pequenas modificações foram feitas para adequar o código ao workshop ministrado na XII Semana Acadêmica de Computação.
'''

# ### Libraries ### #
import tensorflow as tf 
import numpy as np 
import random
from collections import deque 

# ### Hyper Parameteres ### #
FRAME_PER_ACTION = 1		# Numéro de timesteps a esperar por uma ação
GAMMA = 0.95 				# Taxa de decaimento de observações anteriores
OBSERVE = 50000. 			# Timesteps dedicados a Observação
EXPLORE = 100000. 			# Timesteps dedicados a Exploração (modificação de Epsilon)
FINAL_EPSILON = 0.1			# Valor final de Epsilon (0.01)
INITIAL_EPSILON = 1.0		# Valor inicial de Epsilon
REPLAY_MEMORY = 200000 		# Tamanho do Replay Memory
BATCH_SIZE = 32 			# Tamanho do Minibatch de Memória para Treino
UPDATE_TIME = 10000			# Número de timesteps para copiar a Rede Neural Target

# ### Classes ### #
# Essa é a classe principal do nosso Workshop. Ela irá agregar todas as funções do nosso agente para o Deep Q-Learning.
class BrainDQN:
	# Construtor
	def __init__(self,actions):
		# 1º Passo: Inicialização dos parâmetros de treino
		
		# __Código aqui...
		
		# 2º Passo: Inicialização de toda a Rede Neural Convolucional do DQN (Função createQNetwork())
		
		# __Código aqui...

		# 3º Passo: Inicialização da Rede Neural Target para o treinamento
		
		# __Código aqui...
		
		# 4ª Passo: Inicialização do método de treinamento
		
		# __Código aqui...

		# 5º Passo: Criando sessão do Tensorflow e recarregando RedesNeurais pré-treinadas
		
		# __Código aqui...

	# Essa função será responsável por definir todas as camadas, pesos e bias da Rede Neural
	# Além disso, como o Tensorflow nos permite, também já definiremos os neurônios diretamente pelas suas operações de ativação
	def createQNetwork(self):
		# 1º Passo: Inicialização dos pesos e bias das Redes Neurais 
		# (permite configurar suas dimensões)
		
		# __Código aqui...

		# 2º Passo: Inicialização de um Placeholder para a informação de entrada (a imagem do estado)
		
		# __Código aqui...

		# 3º Passo: Inicialização dos neurônios de cada Camada Oculta de acordo com suas operações de ativação
		
		# __Código aqui...

		# 4º Passo: Inicialização dos neurônios da Camada Densa de acordo com suas operações de ativação
		# (Importante ressaltar que a saída final é, justamente, os Q-Values utilizados para o treino)
		
		# __Código aqui...

	# Essa função apenas define a execução, na sessão, da operação de cópia da Rede Neural para a Rede Neural Target
	def copyTargetQNetwork(self):
		# __Código aqui...

	# Essa função inicializa os parâmetros e operações do treinamento Q-Learning
	def createTrainingMethod(self):
		# 1º Passo: Inicialização da Entrada e Saída da Rede Neural
		
		# __Código aqui...
		
		# 2º Passo: Definição da operação de cálculo do Q-Value de acordo com o custo da ação tomada e o valor esperado
		
		# __Código aqui...

	# Essa função compreende a principal função de treinamento do nosso agente, que engloba tanto os conceitos de Deep Learning
	# como Q-Learning.
	def trainQNetwork(self):
		# 1º Passo: Selecionar, e organizar, uma amostra aleatória (batch) do Replay_Memory
		
		# __Código aqui...

		# 2º Passo: Calcular, para esse batch, os valores esperados de saída da Rede Neural (dado a Entrada)
		
		# __Código aqui...

		# 3º Passo: Realizamos um step de treinamento, utilizando as funções extraídas.
		
		# __Código aqui...

		# 4º Passo: Salvamos o estado da Rede Neural a cada 10000 Timesteps
		
		# __Código aqui...

		# 5º Passo: Copiamos o estado da Rede Neural para o Target, caso o Timestep seja igual ao tempo de atualização
		
		# __Código aqui...

	# Essa função será responsável por receber a informação de um estado do Emulador, e utilizar essas informações
	# como entradas para o Treinamento da Rede Neural.
	def setPerception(self, nextObservation, action, reward, terminal):
		# 1º Passo: Adicionamos o novo estado ao estado atual
		
		# __Código aqui...

		# 2º Passo: Realizamos um step de treinamento (caso estejamos no modo de treino)
		
		# __Código aqui...

		# 3º Passo (Visualização): Imprimimos o estado em que o algoritmo se encontra
		
		# __Código aqui...

		# 4º Passo: Atualizamos as informações de treino
		
		# __Código aqui...

	# Essa função será utilizada para selecionar a melhor ação possível dado o estado atual do Agente,
	# tendo em vista as ações permitidas e os parâmetros de treino circunstanciais.
	def getAction(self):
		# 1º Passo: Extraimos o vetor de Q-Values do nosso estado atual
		
		# __Código aqui...
		
		# 2º Passo: Selecionamos a melhor ação possível, uma ação aleatória ou não fazemos nada
		
		# __Código aqui...

		# 3º Passo: Atualizamos o EPSILON por cada ação tomada
		
		# __Código aqui...

	# #### Funções Auxiliares #### #
	def setInitState(self, observation):
		self.currentState = np.stack((observation, observation, observation, observation), axis = 2)

	def weight_variable(self, shape):
		initial = tf.truncated_normal(shape, stddev = 0.01)
		return tf.Variable(initial)

	def bias_variable(self, shape):
		initial = tf.constant(0.01, shape = shape)
		return tf.Variable(initial)

	def conv2d(self, x, W, stride):
		return tf.nn.conv2d(x, W, strides = [1, stride, stride, 1], padding = "VALID")