tupla = (int(input("Digite um numero: ")),
         int(input("Digite o segundo numero: ")),
         int(input("Digite o terceiro numero: ")),
         int(input("Digite o ultimo numero: ")))

print("Os valores digitados:", tupla)
if 9 in tupla:
    print("O valor 9 apareceu:", tupla.count(9))
else:
    print("O numero 9 nao foi encontrado")
if 3 in tupla:
    print(f"O valor 3 esta no indice", tupla.index(3))
else:
    print("O numero 3 nao foi encontrado")
cont = 0
for n in tupla:
    if n % 2 == 0:
        cont += 1
print(f"Na tupla foi encontrado {cont} numero pares")