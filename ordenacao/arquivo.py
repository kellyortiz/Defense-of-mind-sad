def ler_pontos():
    arquivo = open("pontos.txt", "r")
    pontos = []
    for line in arquivo:
        pontos.append(int(line.rstrip()))
    arquivo.close()
    return pontos

def ordenar(vetor):
    for j in range(len(vetor)):
        for i in range(len(vetor)-1):
            if(vetor[i] < vetor[i+1]):
                vetor[i+1], vetor[i] = vetor[i], vetor[i+1]
    return vetor
    

def get_pontos():
    atual = ler_pontos()
    ordenado = ordenar(atual)
    for p in ordenado:
        print(p)

def guardar_pontos(pontuacao):
    atual = ler_pontos()
    ordenado = ordenar(atual)
    arquivo = open("pontos.txt", "w")
    aux = False
    for i in range(len(ordenado)-1, -1, -1):
        print(ordenado[i])
        print(pontuacao)
        if(pontuacao > ordenado[i]):
            ordenado[i] = pontuacao
            aux = True
            break
    if(aux):
        for i in ordenado:
            arquivo.writeline(i)
    arquivo.close()
        
guardar_pontos(2)
