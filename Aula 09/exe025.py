nome = input('digite seu nome completo  ')
existe = "silva" in nome
if existe == True: 
    print(f'no seu nome contém o sobre nome "silva"')
    print(nome)
else:
    print( 'deu ruim pa tu, não tem "silva" no nome ')