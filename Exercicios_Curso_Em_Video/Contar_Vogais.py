tupla = ("kaua", "bruna", "kaue", "Pedro")


for palavra in tupla:
    print(f"\nA palavra {palavra.upper()} contem", end=" ")
    for letra in palavra:
        if letra in "aeiou":
            print(letra, end=" ")