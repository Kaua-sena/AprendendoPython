# adicionar clientes a lista usuarios
cliente = []
usuarios = []
maior = menor = 0
while True:
    cliente.append(str(input('Nome: ')))
    cliente.append(float(input("peso: ")))
    
    if len(usuarios) == 0:
        maior = menor = cliente[1]
    if cliente[1] > maior:
        maior = cliente[1]
    if cliente[1] < menor:
        menor = cliente[1]
    usuarios.append(cliente[:])
    cliente.clear()
    opcoes = str(input("Deseja continuar [N/S]: "))
    if opcoes in "Nn":
        break
print('=-'*30)   
print(f"Total de clientes: {len(usuarios)}")
print(f'O maior peso {maior}.', end=" ")
for i in usuarios:
    if i[1] == maior:
        print(i[0], end=' ')
print(f"\nO menor peso {menor}.", end=" ")
for i in usuarios:
    if i[1] == menor:
        print(i[0], end=' ')
