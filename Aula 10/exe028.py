from random import randint


n = []

n.append(randint(0,5))

busca = int(input('Digite um número entre 0 e 5 que vc acha q o computador escolheu:  '))

if busca == n:
    print('vc acertou Parabéns !!!')
else:
    print('deu ruim pra tua, acertasse não :(')


print(f'o número que o computador escolheu foi {n} ')