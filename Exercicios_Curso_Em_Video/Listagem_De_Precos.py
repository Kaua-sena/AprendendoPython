print("-"*40)
print(f"{"LISTAGEM DE PREÇOS":^40}")
print("-" * 40)
tupla = ("Lápis", 1.75,
         "Borracha",2.0,
         "Caderno", 15.90,
         "Estôjo", 25.00,
         "Transferido", 4.20,
         "Compasso", 9.99,
         "Mochila", 120.32,
         "Caneta", 2.90,
         "Livros", 130.90)

for i in range(len(tupla)):
    if i % 2 == 0:
        print(f"{tupla[i]:.<30}", "R$ ", end="")
    else:
        print(f"{tupla[i]:>6.2f}")