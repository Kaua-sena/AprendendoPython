expressao = (input('digite a expressao: '))
parenteses = expressao.count('(')
parenteses2 = expressao.count(')')
if parenteses < 1 and parenteses2 < 1 :
    print("Expressao sem parenteses")
elif parenteses >= 1:
    if parenteses - parenteses2 == 0:
        print("Expressao correta")
    else:
        print("Expressao incorreta")