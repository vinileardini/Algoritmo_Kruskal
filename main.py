#Projeto realizado por Vinícius Camargo Leardini

from classAresta import Aresta

from classVertice import Vertice

def encontrar_arvore_geradora_minima(arestas,x):

    Arvore_geradora_minima = []
    subconjunto_arestas = []  #Subconjunto mínimo das arestas
    
    def procura_subconjunto(subconjuntos_arestas,i):
        if subconjuntos_arestas[i].elemento_pai != i:
            subconjuntos_arestas[i].elemento_pai = procura_subconjunto(subconjuntos_arestas,subconjuntos_arestas[i].elemento_pai)
        return subconjuntos_arestas[i].elemento_pai
    
    
    #Realiza a união de dois subconjuntos
    def unir_conjunto(subconjunto_arestas, a, b):
        encontra_a = procura_subconjunto(subconjunto_arestas, a)
        encontra_b = procura_subconjunto(subconjunto_arestas, b)

        #Caso o elemento a possua um ranking menor que o elemento b, o elemento a tem como elemento pai o elemento b  
        if subconjunto_arestas[encontra_a].ranking < subconjunto_arestas[encontra_b].ranking:
            subconjunto_arestas[encontra_a].elemento_pai = encontra_b
        
        # Caso o elemento a possua um ranking maior que o elemento b, o elemento b tem como elemento pai o elemento a
        elif subconjunto_arestas[encontra_a].ranking > subconjunto_arestas[encontra_b].ranking:
            subconjunto_arestas[encontra_b].elemento_pai = encontra_a
        
        else:
            subconjunto_arestas[encontra_b].elemento_pai = encontra_a
            subconjunto_arestas[encontra_a].ranking += 1
    

    # Ordena as arestas por peso

    arestas.sort(key=lambda a: a.peso) #key= lambda é uma função anonima

    # Insire as arestas existentes no array subconjunto_arestas
    for n in range(x):
        subconjunto_arestas.append(Aresta(n, 0))
    
    n = 0

    # Percorre a árvore geradora miníma 
    while len(Arvore_geradora_minima) < x - 1 and n < len(arestas):

        aresta = arestas[n]

        origem = procura_subconjunto(subconjunto_arestas, aresta.origem)
        destino =  procura_subconjunto(subconjunto_arestas, aresta.destino)

        # verifica a ocorrência de ciclo

        if origem != destino:
            Arvore_geradora_minima.append(aresta)
            unir_conjunto(subconjunto_arestas, origem, destino)

        n += 1


    print(f'A árvore geradora mínima possui as arestas:')
    for aresta in Arvore_geradora_minima:
        print(f'Aresta {aresta.origem} até Aresta {aresta.destino}, Peso = {aresta.peso}' )
        


arestas = [
Vertice(0, 2, 7),
Vertice(0, 4, 4),
Vertice(0, 5, 7),
Vertice(2, 1, 8),
Vertice(2, 4, 6),
Vertice(4, 1, 7),
Vertice(1, 5, 5),
Vertice(1, 3, 3),
Vertice(5, 3, 4),
]

encontrar_arvore_geradora_minima(arestas,6)
    
    










