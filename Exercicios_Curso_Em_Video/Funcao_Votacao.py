
def votacao(d):
    from datetime import date
    d = date.today().year - d
    if d < 18:
        print(f"Com {d} anos, NAO PODE VOTAR. ")
    elif d >= 18 and d < 65:
        print(f"Com {d} anos, O VOTO E OBRIGATORIO. ")
    elif d >= 65:
        print(f"Com {d} anos, O VOTO NAO E OBRIGATORIO. ")
print("-" * 30) 
print(votacao(d = int(input("Qual o ano de seu nascimento: "))))