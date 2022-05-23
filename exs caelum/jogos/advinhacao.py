print('************************')
print('*   Adivinhar numero   *')
print('************************')

numero_secreto = 42



chute = int(input('Digite seu numero: \n'))
print('Seu chute: ', chute)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
    print('Voce acertou!')
elif(maior):
    print('Errou, seu chute foi maior que o numero secreto')
elif(menor):
    print('Errou, seu chute foi menor que o numero secreto')

