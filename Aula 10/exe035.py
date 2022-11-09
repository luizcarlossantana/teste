reta1 = int(input('Dite o cumprimento da primara reta:  '))
reta2 = int(input('Dite o cumprimento da segunda reta:  '))
reta3 = int(input('Dite o cumprimento da terceira reta:  '))

soma1 = reta1 + reta2
soma2= reta2 + reta3
soma3 = reta1 + reta3

if soma1 > reta3 and soma2 > reta1 and soma3 > reta2:
    print(f'essas retas formam um triângulo')
else:
    print(f'Deu ruim pra tu, tuas retas não formam triângulos')

print(f'primeira reta:{reta1}\nsegunda reta:{reta2}\nterceira reta:{reta3}')
