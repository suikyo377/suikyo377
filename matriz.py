def matrizes(l):
    matriz = []
    for i in range(len(l)):
        linha = []
        for j in range (len(l)):
            print('digite o valor da posição', i,',',j)
            linha.append(int(input()))
        matriz.append(linha)
    return matriz
def pares (p):
    somalinha=0
    for g in range (0,len(p)):
        for d in range (0, len(p)):
            if g%2!=0:
                somalinha += p[g][d]
    return somalinha
def diago(p):
    somadiago = 0
    for g in range (len(p)):
        for d in range(len(p)):
            if (g+d) == (len(p)-1):
                somadiago += p[g][d]
    return somadiago
