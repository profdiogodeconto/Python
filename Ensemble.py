from sklearn import tree
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy


vetor = []
tamanho_populacao = 50
quantidade_genes = 827

## converte o CSV de características em matriz
#####################################################################
def converter_csv_para_vetor():
    return numpy.loadtxt(open("featv1_ANSI.csv", "rb"), delimiter=",", skiprows=0, dtype=str)

def gerar_cromossomos():
    populacao_cromossomo = (tamanho_populacao, quantidade_genes)
    return numpy.random.randint(0, 2, size=populacao_cromossomo)

# def dividir_treino(dados):



# def dividir_validacao_teste(dados):



def dividir_dados_alvo(vetor):
    return vetor[:, [0, len(vetor[0]) - 2]], vetor[:,len(vetor[0]) - 1]



def calcular_fitness(vetor):
    fitness = []
    for linha in vetor:
        fitness.append(sum(linha))
    return fitness

def main():
    # vetor_caracteristicas = converter_csv_para_vetor()
    numero_geracoes = 10
    numero_filhos = 25
    cromossomos = gerar_cromossomos()
    vetor = converter_csv_para_vetor()
    
    dados, alvo = dividir_dados_alvo(vetor)
    dados_treino, dados_teste_validacao, alvo_treino, alvo_teste_validacao = train_test_split(dados, alvo, test_size=0.5, random_state = 0, stratify=alvo)
    dados_teste, dados_validacao, alvo_teste, alvo_validacao  = train_test_split(dados_teste_validacao, alvo_teste_validacao, test_size=0.5, stratify=alvo_teste_validacao)    
    classificador_j48 = tree.DecisionTreeClassifier()
    classificador_j48 = classificador_j48.fit(dados_treino, alvo_treino)
    alvo_predicao = classificador_j48.predict(dados_validacao)

    print ("Accuracy:{0:.3f}".format(metrics.accuracy_score(alvo_validacao,alvo_predicao)),"\n")
    print ("Confusion matrix")
    print (metrics.confusion_matrix(alvo_validacao,alvo_predicao),"\n")
    # print(classificador_j48.score(dados_validacao,alvo_validacao))

    
    bagging = BaggingClassifier(tree.DecisionTreeClassifier(), max_samples=0.5, max_features=0.5)
    bagging.fit(dados_treino, alvo_treino)
    print(bagging.score(dados_validacao, alvo_validacao))

main()