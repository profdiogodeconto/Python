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
            print("Majoritario: ", j)
            return j
    r = random.randint(0,len(fitness) - 1)
    print("Random: ", r)
    return r
    
def crossover(array):
    for i in range(1, len(array), 2):
        r = 0
        while(r == 0):
            r = random.randint(0, len(array[i]) - 1)
        primeiro_cromossomo = array[i - i][:r].tolist()
        primeiro_cromossomo.extend(array[i][r:])
        segundo_cromossomo = array[i][:r].tolist()
        segundo_cromossomo.extend(array[i - i][r:])
        array.append(primeiro_cromossomo)
        array.append(segundo_cromossomo)
        print(len(primeiro_cromossomo))
        print(len(segundo_cromossomo))
        r = 0
    print(len(array))
# teste = numpy.delete(array,[0,2],0)
# print(teste)