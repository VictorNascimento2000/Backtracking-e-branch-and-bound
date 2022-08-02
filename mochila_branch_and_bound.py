import numpy as np
import heapq
import time

start = time.process_time()

#Abrindo o arquivo
file = open("items.csv")
items = np.loadtxt(file, delimiter=" ")

#Separando o número de items o peso de restrição
N = int(items[0][0])
W = items[0][1]

#Criando a matriz com os valores e adicionando uma coluna referente ao valor por peso
items = np.delete(items, 0, 0)
valuePerWeight = np.zeros((np.shape(items)[0], 1))
for i in range(N):
    valuePerWeight[i][0] = items[i][0]/items[i][1]
items = np.c_[items, valuePerWeight]

#ordenando as linhas da matriz em ordem decrescente em relação ao valor por peso dos items
ind = np.argsort(items[:,2])
rind = ind[::-1]
items = items[rind]
newrow = np.zeros((1, np.shape(items)[1]))
items = np.vstack([items, newrow])

class Node:
    def __init__(self, level, value, weight, bound):
        self.level = level
        self.value = value
        self.weight = weight
        self.bound = bound

root = Node(0,0,0, W*items[0][2])
Q = []
heapq.heappush(Q, (0, 0, root))
count = 0
best = 0
while len(Q) > 0:
    node = heapq.heappop(Q)[2]
    if node.level == N:
        if best < node.value:
            best = node.value
    elif node.bound > best:
        withh = node.value + items[node.level][0] + (W - node.weight - items[node.level][1])*items[node.level+1][2]
        wout = node.value + (W - node.weight)*items[node.level+1][2]
    
        if node.weight + items[node.level][1] <= W and withh > best:
            v = Node(node.level+1, node.value + items[node.level][0], node.weight + items[node.level][1], withh)
            count = count + 1
            heapq.heappush(Q, (-withh, count, v))
        if wout > best:
            x = Node(node.level+1, node.value, node.weight, wout)
            count = count + 1
            heapq.heappush(Q, (-wout, count, x))
print(time.process_time() - start, end = '\n')
print(best)
    


