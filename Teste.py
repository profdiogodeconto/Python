from sklearn import tree
from sklearn import metrics

dados = [[0,1,2,3,1,0,2,3,4,0,5,0],[0,1,2,3,1,0,2,3,4,0,5,0],[0,1,2,3,1,0,2,3,4,0,5,0],[0,1,2,3,1,0,2,3,4,0,2,2]]
alvo = [1,0,1,1]

def main():
    classificador_j48 = tree.DecisionTreeClassifier()
    classificador_j48 = classificador_j48.fit(dados, alvo)

    print(classificador_j48.score(dados,alvo))



main()