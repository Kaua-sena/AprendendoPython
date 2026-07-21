lista = []

for v in range(0, 5):
    item = int(input('adicionar valor: '))
    if v == 0 or item > lista[-1]:
        lista.append(item)
        print("adicionou no final da lista")
    else:
        pos = 0
        while pos < len(lista):
            if item <= lista[pos]:
                lista.insert(pos, item)
                print(f'adicionou o {item} na posicao {pos}')
                break
            pos += 1
print(lista)