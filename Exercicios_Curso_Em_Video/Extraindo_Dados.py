lista = []

while True:
    numero = int(input("adicionar numero: "))
    lista.append(numero)
    opcao = str(input("adicionar outro numero? [S/N]: "))
    if opcao in "Nn":
        break
print(30*"=-")
lista.sort(reverse=True)
print(f"A lista de forma decrescente: {lista}")
print(f"A lista contem {len(lista)} elementos")
if 5 in lista:
    print("Na lista tem o numero 5")
else:
    print("Nao tem o numero 5")