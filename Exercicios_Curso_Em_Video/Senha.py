from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados: ', end="")
for n in tupla:
    print(n, end=' ')
print(f'\nO maior valor sorteado: {max(tupla)}')
print(f'O menor valor sorteado: {min(tupla)}')