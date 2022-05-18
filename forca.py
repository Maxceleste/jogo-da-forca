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


    def exibição_letras(self, palavra = str, letras_acertadas = False):
        '''
        Função que retorna a exibição da palavra para o jogo da forca

        Tem dois argumentos, uma string que é a palavra selecionada e é pbrigatório, e uma tupla que indica
        quais as letras que o jogador chutou certo, não sendo obrigatório. Caso não tenha chutado certa nenhuma
        letra, o código não irá informar as letras acertadas, retornando apenas todas as palavras sublinhadas.
        '''
        
        if not letras_acertadas:
            palavra_escondida = ' _ ' * len(palavra)
            return palavra_escondida
        
        else:
            lista_de_letras = list(palavra)
            palavra_escondida = palavra
            
            for letra in lista_de_letras:
                if not letra in letras_acertadas:
                    palavra_escondida = palavra_escondida.replace(letra, ' _ ')
                    
            return palavra_escondida
    

    def letra_certa(self, letra = str, palavra = str):
        '''
        Função que retorn True se a letra está na palavra ou False se a letra não está.
        '''
        return letra in palavra
            


 

if __name__ == '__main__':
    j = Jogar()
    print(j.letra_certa('a', 'teste'))