alunos = list()
nomes_media = list()
# Entrada de dados
while True:
    nomes_media.append(str(input("Nome do Aluno: ")))
    nomes_media.append(float(input("1º Nota do Aluno: ")))
    nomes_media.append(float(input("2º Nota do Aluno: ")))
    alunos.append(nomes_media[:])
    nomes_media.clear()
    resp = str(input("Deseja Continua [S/N]: "))
    if resp in "nN":
        break

# Planilha dos Dados
print("=-"* 30)
print("No. NOME    MÉDIA.")
cont = 0
for i in alunos:
    print(f"{cont:<}{i[0].upper():^12}{(i[1] + i[2]) / 2:>}")
    cont += 1
while True:
    print("-"* 60)
    mostrar_notas = int(input("Mostrar notas de qual aluno: (999 imterrope): "))
    for i in alunos:
        i = mostrar_notas
        print(f"Notas do aluno {alunos[i][0].upper()} são {alunos[i][1:]}.")
        break
    if mostrar_notas == 999:
        break
