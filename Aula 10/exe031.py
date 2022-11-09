km = int(input('Qual a distância em KM para onde vc vai?  '))
pass1 = km*0.5
pass2= km*0.45

if km <= 200:
   
    print(f'Sua passagem será de R${pass1:.2f}')
else:
    print(f'Sua passagem será de R${pass2:.2f}')