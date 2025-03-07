#Versão 1

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

def game():

    limpa_tela()

    print('\nBem-vindo(a) ao Jogo da Forca!')
    print('Adivinhe a palavra abaixo:\n')

    #lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    #escolhando randomicamente uma palavra da lista
    palavra = random.choice(palavras)

    #list comprehension
    letras_descobertas = ['_' for letra in palavra]

    #numero de chances
    chances = 6

    #lista para as letras erradas
    letras_erradas = []

    #loop enquanto numero de chances for maior que zero
    while chances > 0:

        print(' '.join(letras_descobertas))
        print('\nChances restantes: ', chances)
        print('Letras erradas:', ' '.join(letras_erradas))

        #tentativa
        tentativa = input('\nDigite uma letra: ').lower()

        #condição
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        if "_" not in letras_descobertas:
            print('\nVocê venceu, a palavra era: ', palavra)
            break
    
    if "_" in letras_descobertas:
        print('\nVocê perdeu, a palavra era: ', palavra)

#Bloco main
if __name__ == "__main__":
    game()
    print('\nParabéns. Você está aprendendo programação em Python com a DSA. :)\n')