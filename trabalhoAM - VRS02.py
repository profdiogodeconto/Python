# coding: utf-8
### Students: Davi Bernardo, Diogo Deconto, Vinicius Andrade

import csv           
import numpy  
from random import randint
from sklearn import tree
from sklearn.ensemble import BaggingClassifier

f = open('featv1_ANSI.csv', 'r')
training = []
validation = []
test = []
dataset = [None] * 1000

data_training = []
target_training = []
data_test = []
target_test = []


## load the file of characteristics
#####################################################################
def load_file():
    return csv.reader(f)
    
## count the number of instances in dataset
#####################################################################
def instances_count(data):
    total = sum(1 for row in data)
    f.seek(0)
    return total

## count the number of classes of dataset
#####################################################################
def classes_count(data):
    classes = []
    flag = False
    for row in data:
        flag = False
        for c in classes:            
            if row[len(row) - 1] == c:
                flag = True
        if flag == False:
            classes.append(row[len(row) - 1])
    f.seek(0)
    return len(classes)

## divide training dataset
#####################################################################
def divide_training(data, percentage):
    count_instances = instances_count(data)
    count_classes = classes_count(data)
    count_training = int((percentage / 100) * count_instances)
    count_instances_per_class_training = int((count_training / 100) * count_classes)
    instances = [0] * count_classes

    for i in range(0,count_training):
        flag = False
        while not flag:
            position = randint(0,999)
            flag = verify_position(position, "tr", count_instances_per_class_training, instances)

## divide validation dataset
#####################################################################
def divide_validation(data, percentage):
    count_instances = instances_count(data)
    count_classes = classes_count(data)
    count_validation = int((percentage / 100) * count_instances)
    count_instances_per_class_validation = int((count_validation / 100) * count_classes)
    instances = [0] * count_classes

    for i in range(0,count_validation):
        flag = False
        while not flag:
            position = randint(0,999)
            flag = verify_position(position, "va", count_instances_per_class_validation, instances)

## divide test dataset
#####################################################################
def divide_test(data, percentage):
    count_instances = instances_count(data)
    count_classes = classes_count(data)
    count_test = int((percentage / 100) * count_instances)
    count_instances_per_class_test = int((count_test / 100) * count_classes)
    instances = [0] * count_classes

    for i in range(0,count_test):
        flag = False
        while not flag:
            position = randint(0,999)
            flag = verify_position(position, "te", count_instances_per_class_test, instances)

def verify_position(position, t, count_per_class, instances):
    if dataset[position] is None and instances[int(position / 100) - 1] < count_per_class:
        dataset[position] = t
        instances[int(position / 100) - 1] += 1
        return True
    return False

## creates a vector of chromosomes with random values
#####################################################################
def create_chromosome():
    chromosome = []
    for i in range(827):
        chromosome.append(randint(0,1000)%2)
    return chromosome

## J48
#####################################################################
def execute_j48(array, chromosome):
    i = 0
    for row in array:
        if dataset[i] == 'tr':
            ## creates data training
            vetor = []
            for y in range(len(chromosome)):
                vetor.append(row[chromosome[y]])
            data_training.append(vetor)

            #creates target training
            target_training.append(row[len(array[0]) - 1])
        i += 1
    i = 0
    for row in array:
        if dataset[i] == 'te':
            ## creates data test
            vetor = []
            for y in range(len(chromosome)):
                vetor.append(row[chromosome[y]])
            data_test.append(vetor)

            #creates target test
            target_test.append(row[len(array[0]) - 1])
        i += 1
    clf = tree.DecisionTreeClassifier()
    clf.fit(data_training,target_training)
    print(clf.score(data_test,target_test))

def Teste():
    # j48 = tree.DecisionTreeClassifier()
    # j48 = j48.fit(data_training, target_training)
    bagging = BaggingClassifier(tree.DecisionTreeClassifier(), max_samples=1.0, max_features=0.5)
    bagging.fit(data_training, target_training)
    print(bagging.score(data_test,target_test))

## converte o CSV de características em matriz
#####################################################################
def converter_csv_para_vetor():
    return numpy.loadtxt(open("featv1_ANSI.csv", "rb"), delimiter=",", skiprows=0, dtype=str)
    
## main function
#####################################################################
def main():  
    vt_characteristics = load_file()
    vt_chromosome = create_chromosome()

    array = converter_csv_para_vetor()
    divide_training(vt_characteristics, 50)
    divide_validation(vt_characteristics, 25)
    divide_test(vt_characteristics,25)
    execute_j48(array, vt_chromosome)
    
main()

