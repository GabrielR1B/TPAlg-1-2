from collections import defaultdict
import math as math

#Infinito usado para o destino e entrada
INF = math.inf

#Classe do nosso grafo de fluxos
class Grafo:
    def __init__(self, n, m, mapa, capital_x, capital_y):
        self.n = n
        self.m = m
        self.mapa = mapa
        self.capital_x = capital_x
        self.capital_y = capital_y
        
        self.entrada = 2 * n * m
        self.destino = 2 * n * m + 1
        
        self.capacidades = defaultdict(int)
        self.grafo = defaultdict(list)
        self._construir_grafo()
    
#Vertices de Entrada
    def node_in(self, i, j):
        return (i * self.m + j) * 2
#Vertices de Saida
    def node_out(self, i, j):
        return (i * self.m + j) * 2 + 1
#Criando as arestas com os fluxos
    def add_aresta(self, u, v, capacidade):
        self.capacidades[(u, v)] = capacidade
        self.capacidades[(v, u)] = 0  # capacidade reversa inicial zero
        self.grafo[u].append(v)
        self.grafo[v].append(u)
#Construindo o grafo em si    
    def _construir_grafo(self):
        for i in range(self.n):
            for j in range(self.m):
                custo = self.mapa[i][j]
                if custo == 0:
                    # Montanha bloqueia a passagem de soldados, não criamos nós nem arestas
                    continue
                
                u_in = self.node_in(i, j)
                u_out = self.node_out(i, j)
                
                # Aresta interna com capacidade igual ao valor da célula
                self.add_aresta(u_in, u_out, custo)
                
                # Arestas para células vizinhas
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < self.n and 0 <= nj < self.m and self.mapa[ni][nj] != 0:
                        v_in = self.node_in(ni, nj)
                        self.add_aresta(u_out, v_in, INF)
                
                # Conectando entradas às células da borda (entrada inimiga)
                if i == 0 or i == self.n-1 or j == 0 or j == self.m-1:
                    self.add_aresta(self.entrada, u_in, INF)
                
                # Conectando células da capital ao destino
                if i == self.capital_x and j == self.capital_y:
                    self.add_aresta(u_out, self.destino, INF)
