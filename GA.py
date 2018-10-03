import random
import numpy

# array = [[1,1,1],[1,3,2],[1,1,2],[[1,1,3],[1,1,2],[1,1,2]]

def voto_majoritario(fitness):
    for i in fitness:   
        count = 0   
        for j in range(len(fitness)):
            if i == fitness[j]:
                count += 1
        if count > int(len(fitness) / 2):
            return j
    r = random.randint(0,len(fitness) - 1)
    return r
    
def crossover(array):
    nova_populacao = []
    for row in array:
        nova_populacao.append(list(row))
    for i in range(1, len(array), 2):
        r = 0
        while(r == 0):
            r = random.randint(0, len(nova_populacao[i]) - 1)
        primeiro_cromossomo = nova_populacao[i - i][:r]
        primeiro_cromossomo.extend(nova_populacao[i][r:])
        segundo_cromossomo = nova_populacao[i][:r]
        segundo_cromossomo.extend(nova_populacao[i - i][r:])
        nova_populacao.append(primeiro_cromossomo)
        nova_populacao.append(segundo_cromossomo)
        r = 0
    return nova_populacao

def mutacao(array, taxa_mutacao):
    taxa = taxa_mutacao * 100
    count = 0
    for i in array:
        count += 1
        r = random.randint(0,100)
        if r < taxa:
            for j in i:
                r = random.randint(0, len(i) - 1)
                if j == r:
                    if j == 0:
                        j = 1
                    else:
                        j = 0
                break
    return array

def cortar_populacao(cromossomos, fitness):
    metade = len(cromossomos) / 2
    populacao_final = []
    f = []

    while len(populacao_final) != metade:
        index = fitness.index(max(fitness))
        populacao_final.append(cromossomos[index])
        f.append(fitness[fitness.index(max(fitness))])
        fitness = numpy.delete(fitness, index, 0).tolist()
    return populacao_final, f