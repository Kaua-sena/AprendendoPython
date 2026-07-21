# 1º cochetes são colunas 2º cochetes são linhas
matriz = [[], [], []]
indices = soma_pares = terceira_coluna = maior_linha = 0
while indices < 3:
    for i in range(0, 3):
        n = int(input(f"Digite um valor para [{indices}] [{i}]: "))
        # Soma da terceira coluna
        if i == 2:
            terceira_coluna += n
        matriz[indices].append(n)
        # Soma dos pares
        if n % 2 == 0:
            soma_pares += n
    indices += 1
# Maior numero da 2º linha
for i in matriz[1]:
    if i > maior_linha:
        maior_linha = i

print(matriz[0])
print(matriz[1])
print(matriz[2])
print("-="* 30)
print(f"A soma dos valores pares são: {soma_pares}")
print(f'A soma da terceira coluna: {terceira_coluna}')
print(f'O maior número da segunda linha: {maior_linha}')