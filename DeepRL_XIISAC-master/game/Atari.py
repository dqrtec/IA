# ### Libraries ### #
from ale_python_interface import ALEInterface
import numpy as np 
import cv2
from random import randrange

# ### Classes ### #
# Vamos definir uma classe para facilitar a comunicação com o Arcade Learning Environment.
# A função dessa classe será, basicamente, carregar os jogos e seus parâmetros, além de facilitar a representação
# de alguns dados para o programa principal
class Atari:
	# Constructor
	def __init__(self,rom_name):
		# 1º Passo: carregamos o jogo e definimos seus parâmetros
		
		# __Código aqui...

		# 2º Passo: criamos a janela para exibição
		
		# __Código aqui...

	# Essa função será utilizada para receber uma imagem do emulador, já em um formato esperado
	# por nosso algoritmo de treinamento.
	def get_image(self):
		
		# __Código aqui...

	# Simplesmente inicializa o jogo
	def newGame(self):
		
		# __Código aqui...

	# Essa função será responsável por retornar as informações da observação do estado após certa ação ser tomada.
	def next(self, action):
		
		# __Código aqui...
