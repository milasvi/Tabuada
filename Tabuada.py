#Tabuada
print('Bem-vinde ao Tabuada Master2000.\n')
tabuada = int(input('Deseja ler a tabuada de que número? '))
print('\n')
contador = 0

while contador < 10:
    contador = contador + 1
    multi = tabuada * contador
    print(f'{tabuada} x {contador} = {multi}')
print('\nObrigada por utilizar o Tabuada Master2000! \nAté mais!')