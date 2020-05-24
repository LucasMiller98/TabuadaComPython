from time import sleep
print('{:=^50}'.format(''))
print('{:^50}'.format(' Tabuada com python '))
print('{:=^50}'.format(''))
calc = 0
while True:
    tab = int(input('Digite um número inteiro para ver a sua tabuada (digite um número negativo para parar): '))
    # Se for um número negativo, para o loop
    if tab < 0:
        break
    # Já que o contador ignora o último laço, temos que sempre pensar com um a mais. 
    # O for vai começar do 1 até o 11, ignorando o último laço
    for c in range(1, 11):
        calc = tab * c
        print(f'{tab} x {c} = {calc}')
print('Finalizando tabuada...')
sleep(0.5)
print('Tabuada finalizada.')
print('{:=^50}'.format(''))