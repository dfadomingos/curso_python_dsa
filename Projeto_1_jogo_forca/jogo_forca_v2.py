import random
from os import system, name

#Função para limpar tela a cada execução
def limpa_tela():

    #windows
    if name == 'nt':
        _= system('cls')
    
    #mac ou linux
    else:
        _= system('clear')

#função que desenha a forca na tela
def display_hangman(chances):
    
    #lista de estagios
    stages = [
            #estagio 6
            """
                _________
                |       |    
                |       O
                |      \|/
                |       |    
                |      / \\
                |
                |
                |
            """,
            #estagio 5
            """
                _________
                |       |    
                |       O
                |      \|/
                |       |    
                |      / 
                |
                |
                |
            """,
            #estagio 4            
            """
                _________
                |       |    
                |       O
                |      \|/
                |       |    
                |       
                |
                |
                |
            """,
            #estagio 3
            """
                _________
                |       |    
                |       O
                |      \|
                |       |   
                |       
                |
                |
                |
            """,
            #estagio 2
            """
                _________
                |       |    
                |       O
                |       |
                |       |    
                |       
                |
                |
                |
            """,
            #estagio 1
            """
                _________
                |       |    
                |       O
                |      
                |           
                |       
                |
                |
                |
            """,
            #estagio 0
            """
                _________
                |       |    
                |       
                |      
                |           
                |       
                |
                |
                |
            """
    ]
    return stages[chances]

def game():

    limpa_tela()

    print('\nBem-vindo(a) ao Jogo da Forca!')
    print('Adivinhe a palavra abaixo:\n')

    #lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    #escolhando randomicamente uma palavra da lista
    palavra = random.choice(palavras)

    #lista de letras da palavra
    lista_letras_palavras = [letra for letra in palavra]

    #cria o tabuleiro com o caracter "_"
    tabuleiro = ["_"] * len(palavra)

    #numero de chances
    chances = 6

    #lista para as letras erradas
    letras_tentativas = []

    #loop enquanto numero de chances for maior que zero
    while chances > 0:

        print(display_hangman(chances))
        print('Palavra: ', tabuleiro)
        print('\n')

        #tentativa
        tentativa = input('Digite uma letra: ').lower()

        if tentativa in letras_tentativas:
            print('Você já tentou essa letra. Escolha outra!')
            continue

        #lista de tentativas(letras)
        letras_tentativas.append(tentativa)


        #condição
        if tentativa in lista_letras_palavras:

            print('Você acertou a letra!')

            #loop
            for indice in range(len(lista_letras_palavras)):

                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa

            #se todos os espaços forem preenchidos
            if "_" not in tabuleiro:
                print('\nVocê venceu! A palavra era: {}'.format(palavra))
                break
        
        else:
            print('Ops. Essa letra não está na palavra!')
            chances -= 1
    if "_" in tabuleiro:
        print(display_hangman(chances))
        print('\nVocê perdeu! A palavra era: {}'.format(palavra))

#Bloco main
if __name__ == "__main__":
    game()
    print('\nParabéns. Você está aprendendo programação em Python com a DSA. :)\n')