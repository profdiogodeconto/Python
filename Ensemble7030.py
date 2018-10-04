from sklearn import tree
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy
import GA

vetor = []

## converte o CSV de características em matriz
#####################################################################
def converter_csv_para_vetor():
    return numpy.loadtxt(open("featv1_ANSI.csv", "rb"), delimiter=",", skiprows=0, dtype=str)

def gerar_cromossomos(tamanho_populacao, quantidade_genes):
    populacao_cromossomo = (tamanho_populacao, quantidade_genes)
    return numpy.random.randint(0, 2, size=populacao_cromossomo)

def remover_atributos(vetor, cromossomo):
    zeros = []
    for i in range(len(cromossomo)):
        if cromossomo[i] == 0:
            zeros.append(i)
    return numpy.delete(vetor,zeros,1)

# Revisar
def dividir_dados_alvo(vetor):    
    return list(vetor[:, 0:len(vetor[0]) - 2]), list(vetor[:,len(vetor[0]) - 1])

def calcular_fitness(vetor):
    fitness = []
    for linha in vetor:
        fitness.append(sum(linha))
    return fitness

def main():
    vetor = converter_csv_para_vetor()
    tamanho_populacao = 50
    geracoes = 10
    cromossomos = gerar_cromossomos(tamanho_populacao,len(vetor[0]) - 1 )
    classificador_j48 = tree.DecisionTreeClassifier()
    
    dados, alvo = dividir_dados_alvo(vetor)
    dados_treino, dados_teste, alvo_treino, alvo_teste = train_test_split(dados, alvo, test_size=0.3, random_state = 0, stratify=alvo)

    fitness = []
    print("\n########### Geracao  0 ###########\n")
    for cromossomo in cromossomos:
        treino = remover_atributos(dados_treino, cromossomo)
        validacao = remover_atributos(dados_teste, cromossomo)
        classificador_j48 = classificador_j48.fit(treino, alvo_treino)
        alvo_predicao = classificador_j48.predict(validacao)
        score = round(metrics.accuracy_score(alvo_teste,alvo_predicao), 2)
        fitness.append(score)
        print("Score: ", score)
    media = round(sum(fitness)/float(len(fitness)),3)
    print("Average: ", media)

    for i in range(geracoes):
        print("\n########### Geracao ", (i + 1) , "###########\n")

        nova_populacao = []
        for c in range(tamanho_populacao):
            index = GA.voto_majoritario(fitness)
            nova_populacao.append(cromossomos[index])
            fitness = numpy.delete(fitness,index,0)
            cromossomos = numpy.delete(cromossomos, index, 0)
        
        cromossomos = GA.crossover(nova_populacao)                   
        cromossomos = GA.mutacao(cromossomos, 0.01)       

        fitness = []       
        for cromossomo in cromossomos:
            treino = remover_atributos(dados_treino, cromossomo)
            validacao = remover_atributos(dados_teste, cromossomo)
            classificador_j48 = classificador_j48.fit(treino, alvo_treino)
            alvo_predicao = classificador_j48.predict(validacao)
            score = round(metrics.accuracy_score(alvo_teste,alvo_predicao), 2)
            fitness.append(score)
            print("Score: ", score)
        cromossomos, fitness = GA.cortar_populacao(cromossomos, fitness)
        media = round(sum(fitness)/float(len(fitness)),3)
        print("Average: ", media)


    cromossomo = cromossomos[fitness.index(max(fitness))]
    print("\nBest Accuracy: " + str(max(fitness)))

    treino = remover_atributos(dados_treino, cromossomo)
    validacao = remover_atributos(dados_teste, cromossomo)
    classificador_j48 = classificador_j48.fit(treino, alvo_treino)
    alvo_predicao = classificador_j48.predict(validacao)

    print ("\nMatriz de confusao")
    print (metrics.confusion_matrix(alvo_teste,alvo_predicao),"\n")

main()

# classificador_bagging = BaggingClassifier(tree.DecisionTreeClassifier(), max_samples=0.5, max_features=0.5)
# classificador_bagging.fit(dados_treino, alvo_treino)
# alvo_predicao_bagging = classificador_bagging.predict(dados_validacao)
# print ("Accuracy J48: {0:.3f}".format(metrics.accuracy_score(alvo_validacao,alvo_predicao_bagging)),"\n") 




# Ordenar
# tamanho  = len(f) - 1
# fitness.sort(key= lambda x:x[tamanho])