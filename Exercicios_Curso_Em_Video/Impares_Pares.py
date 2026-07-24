

lista = [[], []]
valores = []
for n in range(1, 8):
    n = int(input(f"Digite um numero {n}º: "))
    valores.append(n)
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
valores.sort()
print('-='* 30)
print('Os valores digitados foram:', valores)
print('Os valores pares foi:', lista[0])
print('Os valores impares foi:', lista[1])