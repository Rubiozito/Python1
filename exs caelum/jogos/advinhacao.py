print('************************')
print('*   Adivinhar numero   *')
print('************************')

numero_secreto = 42
tentativas = 3
rodada = 1


while(rodada <= tentativas):
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

print('Game over')
