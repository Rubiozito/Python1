from random import random, randrange

def jogar():
    print('************************')
    print('*   Adivinhar numero   *')
    print('************************')

    numero_secreto = randrange(0, 100)
    rodada = 1

    print('Escolha a dificulade:')
    print('Digite 1 para ->Facil: 20 tentativas \n Digite 2 para ->Medio: 10 tentativas \n Digite 3 para ->Dificil: 5 tentativas')
    dificuldade = int(input())
    if dificuldade == 1:
        tentativas = 20

    if dificuldade == 2:
        tentativas = 10

    if dificuldade == 3:
        tentativas = 5

    print('Advinhe um numero entre 0 e 100')
    for rodada in range(1, tentativas +1):
        print('Tentativa {} de {}'.format(rodada, tentativas))
        chute = int(input('Digite seu numero: \n'))
        print('Seu chute: ', chute)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print('Voce acertou!')
            break
        elif(maior):
            print('Errou, seu chute foi maior que o numero secreto')
        elif(menor):
            print('Errou, seu chute foi menor que o numero secreto')

        rodada = rodada + 1 

    print('O numero secreto era {}'.format(numero_secreto))
    print('Game over')
