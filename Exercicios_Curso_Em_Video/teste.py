def notas(*n, sit = False):
    r = dict()
    r["Tamanho"] = len(n)
    r["Maior"] = max(n)
    r["Menor"] = min(n)
    r["Media"] = sum(n)/ len(n)
    if sit:
        if r["Media"] >= 7:
            r["Situacao"] = "BOA"
        elif r["Media"] > 5:
            r["Situacao"] = "RAZOAVEL"
        else:
            r["Situacao"] = "RUIM"          
    return r
resp = notas(2, 5, 6, sit=True)   
print(resp)

    