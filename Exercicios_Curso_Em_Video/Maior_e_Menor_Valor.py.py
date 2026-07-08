valores = [int(input("Digite o primero numero: ")),
           int(input("Digite o segundo numero: ")),
           int(input("Digite o terceiro numero: ")),
           int(input("Digite o quarto numero: ")),
           int(input("Digite o quinto numero: "))]

# encontrar o maior valor na lista
maior = 0
for e in valores:
    if maior < e:
        maior = e
        
# encontrar o menor valor na lista  
menor = maior
for e in valores:
    if menor > e:
        menor = e
        
# output do maior valor e posicao na tela    
print(f'O maior valor {maior} na posicao => ', end="")               
for i, e in enumerate(valores):
    if e == maior:
        print(i+1, end=" ")

# output do menor valor e posicao na tela        
print(f"\nO menor valor {menor} na posicao => ", end="")
for i, e in enumerate(valores):
    if e == menor:
        print(i+1, end=" ")
 
    
