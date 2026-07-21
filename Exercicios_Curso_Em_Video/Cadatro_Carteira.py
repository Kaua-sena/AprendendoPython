from datetime import datetime
dic = {"Nome": str(input("Nome e Sobrenome: ").title()),
       "Idade": datetime.now().year - int(input("Ano de nascimentos: ")),
       "CTPS": int(input("Carteira de trabalho (0 não tem): "))}

if dic["CTPS"] > 0:
    dic |= {"Contratacao": int(input("Ano de contratação: ")),
           "Salário": int(input("Salário R$: ")),
            "Aposentadoria": 35}
    dic["Aposentadoria"] = (dic["Aposentadoria"] - (datetime.now().year - dic["Contratacao"])) + dic["Idade"]
else:
    dic["CTPS"] = "Nulo"
print(dic)
print("-="* 40)
for k, v in dic.items():
    print(f"{k:<15}|", end="")
    print(f"{v:^12}", end="")
    print(f"{"|":>10}")