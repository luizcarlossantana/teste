salario = int(input('Qual seu salário ?  '))
maior = salario*0.15
menor = salario*0.10

if salario>1250:
    print(maior)
elif salario<= 1250:
    print(menor)