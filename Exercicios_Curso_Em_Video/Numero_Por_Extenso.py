
tupla_string = ("Zero","Um", "Dois", "Tres", "Quatro", "Cinco",
                "Seis", "Sete", "Oito", "Nove", "Dez", "Onze",
                "Doze", "Treze", "Cartoze", "Quinze", "Dizesseis",
                "Dizessete", "Dezoito", "Dezenove", "Vinte")

while True:
    numero = int(input("Digite um numero entre 0 a 20: "))
    if numero <= 20 and numero >= 0:
        print(f"O número decimal {numero} representa por Extenso o número {tupla_string[numero]}!")
        break
    else:
        con = str(input("Quer Continuar?: "))
        if con == "nao":
            break
        if con != "sim":
            print("Nâo entendi. Tente novamente.")
            