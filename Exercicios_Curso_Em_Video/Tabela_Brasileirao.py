Tabela = ("Palmeiras", "Flamengo", "Fluminense", "Paranaense",
          "Bragantino", "Bahia", "Coritiba", "Sao Paulo", "Atletico-MG",
          "Corithians", "Cruzeiro", "Botafogo", "Vitoria", "Internacional", "Santos", "Gremio",
          "Vasco", "Remo", "Mirassol", "Chapecoense")
def quebra_linha():
    print("====================================")


print("PRIMEIROS COLOCADOS")
quebra_linha()
print(Tabela[0:5])
quebra_linha()
print("ULTIMOS COLOCADOS")
quebra_linha()
print(Tabela[15:])
quebra_linha()
print("TABELA EM ORDEM ALFABETICA")
quebra_linha()
print(sorted(Tabela))
quebra_linha()
print("COLOCACAO DO CHAPECOENSE")
Posicao = (Tabela.index("Chapecoense")) +1
print("NA POSICAO", Posicao)
