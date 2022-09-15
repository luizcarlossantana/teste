dias = int(input('quantos dias você alugou o carro ?'))
km = float(input('quantos km você percorreu ? '))
aluguel = (dias*60) + (km*0.15)
print(f'o total do aluguel do carro foi R${aluguel:.2f}')