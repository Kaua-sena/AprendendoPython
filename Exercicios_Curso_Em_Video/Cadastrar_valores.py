lista = []
while True:
    valor = int(input("Cadastre o valor: "))
    if valor not in lista:
        lista.append(valor)
    else:
        print("valores duplicados.")
    casos = str(input("Adicionar outro valor?: "))
    if casos != "s":
        break
lista.sort()
print(lista)
        