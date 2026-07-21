from random import randint
import time

print('-'* 30)
print(f"{"JOGAR NA MEGA SENA":^30}")
print('-'* 30)
quantidade = int(input("Quantos jogos você deseja ser sorteado: "))
print(f"=-=-=  SORTEANDO {quantidade} JOGOS  =-=-=-=")

palpites = list()
jogos = list()
for q in range(1, quantidade + 1):
    for i in range(0, 5):
        i = randint(0, 60)
        # Comparação, caso i esteja na lista palpites
        if i in palpites:
            i = randint(0, 60)
            palpites.append(randint(0, 60))
        else:
            palpites.append(i)
            
    # Organizar a lista, e mostrar no terminal
    palpites.sort()
    print(f"Jogo {q}: {palpites}")
    time.sleep(0.5)
    jogos.append(palpites[:])
    palpites.clear()
print("-="*5, "< 5BOA SORTE! >", "-="*5)