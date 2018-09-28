import random
import numpy

array = [[1,1,3],[1,1,2],[1,1,2]]

def voto_majoritario(array, usados):
    index = 0
    for i in array:   
        count = 0   
        for j in range(len(array)):
            if i[len(i) - 1] == array[j][len(i) - 1]:
                count += 1
        if count > int(len(array) / 2):
            print("Majoritario: ", j)
            index = j
    r = random.randint(0,len(array) - 1)
    print("Random: ", r)
    index = r
    return index
teste = numpy.delete(array,[0,2],0)
print(teste)