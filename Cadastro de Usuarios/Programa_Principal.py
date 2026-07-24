def Entrada_Arquivos_Nome():
    '''
        Entrada: Ler o nome do usuario.
        Saida: Envia a um arquivo "txt".
        Erros: Se ouver erros, volta na leitura do nome do usuario.
               Interrupções, Finaliza o programa.
    '''
    while True:
        try:
            arquivo = open("nome.txt", "a")
            nome = str(input("Escreva seu nome: ").title())
            arquivo.writelines(nome + ":")
            arquivo.close()
            break
        except FileNotFoundError:
            arquivo = open("nome.txt", "w")
            nome = str(input("Escreva seu nome: ").title())
            arquivo.write(nome + ":")
            arquivo.close()
            break
        except (ValueError, TypeError):
            print("\033[31mErro: Digite o seu nome. \033[m")
            continue
        except KeyboardInterrupt:
            print("\nErro: Nome não informado")
def Entrada_Arquivos_Idade():
    '''
        Entrada: Ler a idade do usuario em transfoma em formato String.
        Saida: Envia a um arquivo "txt".
        Erros: Se ouver erros, volta a leitura da idade do usuario.
               Interrupções, Finaliza o programa.
    '''
    while True:
        try:
            arquivo = open("idade.txt", "a")
            idade = int(input("Escreva sua idade: "))
            arquivo.write(str(idade) + ":")
            arquivo.close()
            break
        except FileNotFoundError:
            arquivo = open("idade.txt", "w")
            idade = int(input("Escreva sua idade: "))
            arquivo.write(idade + ":")
            arquivo.close()
            break
        except (ValueError, TypeError):
            print("\033[31mErro: Digite um número válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\nErro: Idade não informada.")
def Lista_Dados():
    '''
        Entrada: ler o arquivo "txt" transformando em lista.
        Saida: As listas "lista_nome" e lista_idade" transforma em dicionario.
        Erros: Sem exerções.
    '''
    nomes = open("nome.txt", "r")
    nomes = nomes.read()
    lista_nomes = list()
    lista_nomes = nomes.split(":")
    idade = open("idade.txt", "r")
    idade = idade.read()
    lista_idade = list()
    lista_idade = idade.split(":")
    Dados = dict(zip(lista_nomes, lista_idade))
    return Dados
def Menu_Principal():
    '''
        Cria o menu principal do programa.
    '''
    print("-"* 50)
    print(f"{"MENU PRINCIPAL":^35}")
    print("-"* 50)
    print("\033[33m1 \033[m- \033[34mVer Pessoa Cadastradas\033[m \n\033[33m2 \033[m- \033[34mCadastrar Novas Pessoas\033[m \n\033[33m3 \033[m- \033[34mSair Do Sistema\033[m")
    print("-"* 50)
def Tabela_Dados():
    '''
        Entrada: Recebe o dicionario "Dados".
        Saida: Cria uma Tabela organizada com os dados do dicionario.
    '''
    dados = Lista_Dados()
    print(f"{"PESSOAS CADASTRADAS":^48}")
    print("-"*50)
    dados = dict(sorted(dados.items()))
    del dados[""]
    for k, v in dados.items():
        print(f"{k:<40}{v:>3} Anos")
def opcao(opcao):
    '''
        Entrada: Recebe numeros de 1 a 3 como opções.
        Erros: Se ouver erros, Finaliza o programa.
    '''
    try:
        opcao = int(input("\033[1;32mSua opção: \033[m"))
        return opcao
    except Exception:
        return 3
    except KeyboardInterrupt:
        print()
        return 3