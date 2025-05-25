from collections import deque, defaultdict
import grafos as grf

#Busca em largura que vamos usar em conjunção ao nosso algoritmo
def bfs(grafo, capacidades, fluxo, source, sink, pai):
    visitado = set()
    fila = deque([source])
    visitado.add(source)
    while fila:
        u = fila.popleft()
        for v in grafo[u]:
            capacidade_restante = capacidades[(u,v)] - fluxo[(u,v)]
            if v not in visitado and capacidade_restante > 0:
                pai[v] = u
                if v == sink:
                    return True
                fila.append(v)
                visitado.add(v)
    return False

#Algoritmo de ford que vai retornar nosso corte minimo
def ford_fulkersson(grafo, capacidades, source, sink):
    fluxo = defaultdict(int)
    max_fluxo = 0
    pai = {}
    
    while bfs(grafo, capacidades, fluxo, source, sink, pai):
        caminho_fluxo = grf.INF
        v = sink
        while v != source:
            u = pai[v]
            caminho_fluxo = min(caminho_fluxo, capacidades[(u,v)] - fluxo[(u,v)])
            v = u
        
        v = sink
        while v != source:
            u = pai[v]
            fluxo[(u,v)] += caminho_fluxo
            fluxo[(v,u)] -= caminho_fluxo
            v = u
        
        max_fluxo += caminho_fluxo
    
    return max_fluxo
