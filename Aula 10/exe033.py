n1 = int(input('digite um número:  '))
n2 = int(input('digite um número:  '))
n3 = int(input('digite um número:  '))
    
if n1>n2 and n1>n3:
    print(n1)
    print('Esse é o maior número digitado')
elif n2>n1 and n2>n3:
    print(n2)
    print('Esse é o maior número digitado')
else:
    print(n3)
    print('Esse é o maior número digitado')



if n1<n2 and n1<n3:
    print(n1)
    print('Esse é o menor número digitado')
elif n2<n1 and n2<n3:
    print(n2)
    print('Esse é o menor número digitado')
else:
    print(n3)
    print('Esse é o menor número digitado')