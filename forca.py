import random

class Forca():

    palavras = (
        'planeta', 'cidade',
        'carro', 'animal',
        'macaco', 'cachorro',
        'gato', 'cobra',
        'roda', 'quadrado',
        'cama', 'tapete',
        'cadeira', 'mesa',
        'cozinha', 'areia',
        'praia'
    )


    def exibição_letras(self, palavra = str, letras_acertadas = False) -> str:
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
    

    def letra_certa(self, letra = str, palavra = str) -> bool:
        '''
        Função que retorn True se a letra está na palavra ou False se a letra não está.
        '''
        return letra in palavra

            
    def jogar(self):
        '''
        Função que coloca o jogo para rodar.

        Essa função roda o jogo, utilizando todas as funções acima e criando variáveis.
        '''

        palavra = random.choice(self.palavras) #Pegando palavra aleatória
        tentativas = 6                         #Estabelecendo o número de tentativas
        letras_acertadas = ()                  #Criando tupla para adicionar letras acertadas
        
        print('*' * 27)
        print('Bem vindo ao jogo da forca!') #Tela de apresentação
        print('*' * 27)

        print('Será exibido para você uma palavra escondida, e seu objetivo é acerta-la.') #Instruções
        print('Você tem 6 chances e a cada letra errada você perde uma! Boa sorte!')

        while True:
            palavra_escondida = self.exibição_letras(palavra, letras_acertadas) #Criando palavra escondida
            print()
            print('Número de tentativas:', tentativas) #Exibindo número de tentativas
            print()

            if tentativas == 0:  #Checando se as tentativas acabaram
                print('Você não adivinhou a palavra :(')
                print('A palavra era', palavra)
                break

            print(palavra_escondida)

            if palavra_escondida == palavra: #Checando se acertou toda a palavra
                print()
                print('Você ganhou o jogo! Parabéns!')
                break
            print()
            letra = input('Insira uma letra: ')

            if self.letra_certa(letra, palavra): #Checando se acertou a letra
                letras_acertadas = letras_acertadas + (letra ,)
                
                print()
                print('Letra correta!')
                
                continue
            
            else: #se não acertou a letra:
                tentativas -= 1
                print()
                print('Esta letra não existe na palavra!')
                
        
        print()
        print('Deseja jogar novamente?')
        print()

        resposta = input('Digite s ou n: ')
        if resposta == 's':
            self.jogar()
        else:
            print('Fim de jogo!')


        

if __name__ == '__main__':
    game = Forca()
    game.jogar()