import os
os.system('cls')



numeros = [0,0,0,0,0]
nota=1
soma=0
x=0
while x<5:
      numeros[x]=(input(f'aluno {x+1}: '))
      x+=1
escolha=int(input(f'digite o nome do aluno que vc quer ver: '))
print(f'{numeros[escolha-1]}')
esc=int(input(f'vc quer adicionar as notas do aluno {numeros[escolha-1]}? (se sim,digite 1, se não, digite 0): '))

if esc==0:
      print('programa finalizado: ')
if esc==1:
      while nota < 4:
            media=int(input(f'digite a nota do {nota}°bimestre: '))
            nota+=1
            soma+=media
            