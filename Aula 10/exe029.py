velo = int(input("qual a velocidade do seu carro agora ?  "))

multa = (velo - 80)*7

if velo > 80:
    print('você será multado')
    print(f'Sua multa será de R${multa},00' )