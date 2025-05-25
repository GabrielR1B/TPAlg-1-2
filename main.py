from grafos import Grafo
from algoritmos import ford_fulkersson

with open('entrada.txt', 'r') as f:
        linhas = f.read().splitlines()
    
n, m = map(int, linhas[0].split())
mapa = [list(map(int, linhas[i+1].split())) for i in range(n)]
x, y = map(int, linhas[n+1].split())
x -= 1
y -= 1
    
g = Grafo(n, m, mapa, x, y)
resultado = ford_fulkersson(g.grafo, g.capacidades, g.entrada, g.destino)
print(resultado)
