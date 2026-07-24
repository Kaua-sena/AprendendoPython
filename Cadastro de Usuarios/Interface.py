import Programa_Principal
while True:
    Programa_Principal.Menu_Principal()
    op = Programa_Principal.opcao(input)
    print("-"*50)

    if op == 1:
        Programa_Principal.Tabela_Dados()
        continue
    if op == 2:
        Programa_Principal.Entrada_Arquivos_Nome()
        Programa_Principal.Entrada_Arquivos_Idade()
        continue
    if op == 3:
        print("\033[31mPrograma finalizado, Muito obrigado!\033[m")
        break
    else:
        print("\033[31mTente novamente. \033[m")
        continue