def fatorial(n):
    if n == 1:
        return 1
    if n > 1:
        return n * fatorial(n - 1)
n = int(input("Digite um numero retonar seu FATORIAL: "))
print(f"O fatorial de {n} é ", end="")
print(fatorial(n))
