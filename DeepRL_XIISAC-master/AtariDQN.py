# ### System Configuration ### #
import sys
sys.path.append("game/")

# ### Libraries ### #
import cv2
from Atari import Atari 
from BrainDQN_Nature import *
import numpy as np 

# ### Functions ### #
# Vamos implementar, primeiramente, a função que implementa o Pré-processamento descrito
# pela técnica do Deep Q-Learning
def preprocess(observation):
	
	# __Código aqui...

# Vamos implementar a função principal que inicializará os nossos agentes e os colocarão
# para aplicar o Deep Q-Learning no treinamento.
def playAtari():
	# 1º Passo: Inicializar o Jogo e o Agente

	# __Código aqui...
	
	# 2º Passo: Obter estado inicial
	
	# __Código aqui...

	# 3º Passo: Realizar treinamento indefenidamente
	
	# __Código aqui...

# ### Main Program ### #
def main():
	playAtari()

if __name__ == '__main__':
	main()