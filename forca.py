'''
Primeiramente vamos dividir o jogo da forca em funções menores:
- Gerar a palavra aleatória
- Esconder a palavra do jogador
- mapear as letras da palavra e suas respectivas posições
- checar se a letra existe ou não, retornando True ou False
- Se True, preencher os espaços vazios
- Se False, Perder uma das 6 chances
- Perder se acabar as chances, ganhar se acertar todas as letras

Posteriormente adicionar um personagem igual o jogo da forca clássico
'''
import random

class Jogar():

    palavras = (
        'planeta',
        'cidade',
        'carro',
        'animal'
    )

    palavra = random.choice(palavras)

    def exibição_letras(self, palavra, letras_acertadas = (False ,)):
        pass
 