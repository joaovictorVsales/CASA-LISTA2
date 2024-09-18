sal= float(input('Digite seu salário bruto: '))
h= int(input('Digite horas trabalhadas no mês: '))
i= float(input('Digite o imposto de renda: '))
e= float(input('Digite o encargo: '))

if(sal<800):
    print(f'Seu salário é R${sal}')

if(800<=sal<=1600):
    print(f'Seu salário é R${sal-(i+(i*8/100))- (e+(e*5/100))}')

if(sal>1600):
    print(f'Seu salário é {sal-(i+(i*15/100))- (e+(e*7/100))}')

if(h>160):
    print(f'Seu salário é {sal/160 + ((h-160)*0.5)}')

