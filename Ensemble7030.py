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
    return vetor[:, 0:len(vetor[0]) - 2], vetor[:,len(vetor[0]) - 1]

def calcular_fitness(vetor):
    fitness = []
    for linha in vetor:
        fitness.append(sum(linha))
    return fitness

def main():
    vetor = converter_csv_para_vetor()
    tamanho_populacao = 6
    geracoes = 10
    quantidade_genes = len(vetor[0]) - 1    
    cromossomos = gerar_cromossomos(tamanho_populacao,quantidade_genes)
    classificador_j48 = tree.DecisionTreeClassifier()
    
    dados, alvo = dividir_dados_alvo(vetor)
    dados_treino_completo, dados_validacao_completo, alvo_treino, alvo_validacao = train_test_split(dados, alvo, test_size=0.3, random_state = 0, stratify=alvo)
    # dados_teste_completo, dados_validacao_completo, alvo_teste, alvo_validacao  = train_test_split(dados_teste_validacao_completo, alvo_teste_validacao, test_size=0.5, stratify=alvo_teste_validacao)    
    
    fitness = []
    print("\n########### Geracao  0 ###########\n")
    for cromossomo in cromossomos:
        dados_treino = dados_treino_completo
        dados_validacao = dados_validacao_completo
        dados_treino = remover_atributos(dados_treino, cromossomo)
        dados_validacao = remover_atributos(dados_validacao, cromossomo)
        classificador_j48 = classificador_j48.fit(dados_treino, alvo_treino)
        alvo_predicao_j48 = classificador_j48.predict(dados_validacao)

        score = round(metrics.accuracy_score(alvo_validacao,alvo_predicao_j48), 2)
        fitness.append(score)
        print("Score: ", score)

    for i in range(geracoes):
        print("\n########### Geracao ", (i + 1) , "###########\n")

        nova_populacao = []
        for c in range(len(cromossomos)):
            index = GA.voto_majoritario(fitness)
            fitness = numpy.delete(fitness,index,0)
            nova_populacao.append(cromossomos[index])
        
        cromossomos = GA.crossover(nova_populacao)                   
        cromossomos = GA.mutacao(cromossomos, 0.05)
       
        fitness = []       
        for cromossomo in cromossomos:
            dados_treino = dados_treino_completo
            dados_validacao = dados_validacao_completo
            dados_treino = remover_atributos(dados_treino, cromossomo)
            dados_validacao = remover_atributos(dados_validacao, cromossomo)
            classificador_j48 = classificador_j48.fit(dados_treino, alvo_treino)
            alvo_predicao_j48 = classificador_j48.predict(dados_validacao)

            score = round(metrics.accuracy_score(alvo_validacao,alvo_predicao_j48), 2)
            fitness.append(score)
            print("Score: ", score)
        cromossomos, fitness = GA.cortar_populacao(cromossomos, fitness)

    cromossomo = cromossomos[fitness.index(max(fitness))]
    print("Best Accuracy: " + str(max(fitness)))

main()

# classificador_bagging = BaggingClassifier(tree.DecisionTreeClassifier(), max_samples=0.5, max_features=0.5)
# classificador_bagging.fit(dados_treino, alvo_treino)
# alvo_predicao_bagging = classificador_bagging.predict(dados_validacao)
# print ("Accuracy J48: {0:.3f}".format(metrics.accuracy_score(alvo_validacao,alvo_predicao_bagging)),"\n") 


# print ("Confusion matrix")
# print (metrics.confusion_matrix(alvo_validacao,alvo_predicao),"\n")
# # print(classificador_j48.score(dados_validacao,alvo_validacao))

# Ordenar
# tamanho  = len(f) - 1
# fitness.sort(key= lambda x:x[tamanho])