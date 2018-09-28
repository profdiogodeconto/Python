import numpy

array1 = [1,1,1,1,2,2,2,2]
array2 = [3,3,3,3,4,4,4,4]

def main():
    array5 =  array1[4,:] + array2[:,4]
    print(array5)

main()