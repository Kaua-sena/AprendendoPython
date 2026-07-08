lista = []
while True:
    valor = int(input("Adicione um valor: "))
    if len(lista) < 1:
        lista.append(valor)
    elif len(lista) > 1:
        for i, e in enumerate(lista):
            if valor > e:
                lista.insert(i, valor) 
            opcao = str(input("Continuar?. "))
            if opcao != "s":
                break
print(lista)
    