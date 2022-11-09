ano = int(input('Digite um ano para saber se é Bissexto  '))

if ano%4 == 0 and ano%100 == 0 and ano%400 == 0:
    print(ano)
    print('o ano que vc digitou é BISSEXTO')
else:
    print(ano)
    print('o ano que vc digitou não é BISSEXTO')
    
