import numpy
import random

array1 = [1,1,1,1,2,2,2,2]
array2 = [3,3,3,3,4,4,4,4]

def main():
    X = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    Y = [ 0,   3,   1,    5,   6,   4,   8,   7,   2]

    Z = [x for _,x in sorted(zip(Y,X))]
    print(Z)  # ["a", "d", "h", "b", "c", "e", "i", "f", "g"]
    # for i in range(500):
    #     print(random.randint(0,100))


main()